#!/usr/bin/env python3
"""Refresh the Goodreads fields in _data/fun_facts.yml.

- books_read / books_year: from the public "Year in Books" page for the current year.
- current_book*: of the books on the profile's "Currently Reading" list, the one
  with the most recent progress update. Goodreads status IDs only increase, so
  the highest /user_status/show/<id> is the latest update. Books without any
  progress update are ignored.

Any failure leaves the existing values untouched and exits 0, so it never
breaks the site build. Standard library only.
"""

import datetime
import html
import json
import re
import sys
import urllib.request
from pathlib import Path

USER_ID = "121501165"
PROFILE_URL = f"https://www.goodreads.com/user/show/{USER_ID}"
YEAR_URL = "https://www.goodreads.com/user/year_in_books/{year}/" + USER_ID
DATA_FILE = Path(__file__).resolve().parent.parent / "_data" / "fun_facts.yml"
UA = "Mozilla/5.0 (compatible; personal-site-build)"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def books_read(year):
    page = fetch(YEAR_URL.format(year=year))
    m = re.search(r"([\d,]+)\s*books read", re.sub(r"<[^>]+>", " ", page))
    return int(m.group(1).replace(",", "")) if m else None


def current_book():
    page = fetch(PROFILE_URL)
    start = page.find("Currently Reading</a>")
    if start < 0:
        return None
    # The section ends where the next profile box starts.
    end = page.find('class="h2Container', start)
    section = page[start : end if end > 0 else len(page)]

    best = None
    for block in section.split('<div class="Updates')[1:]:
        title = re.search(r'class="bookTitle" href="([^"]+)">([^<]+)</a>', block)
        author = re.search(r'class="authorName" href="[^"]+">([^<]+)</a>', block)
        statuses = [int(s) for s in re.findall(r"/user_status/show/(\d+)", block)]
        if not (title and statuses):
            continue
        latest = max(statuses)
        if best is None or latest > best[0]:
            best = (
                latest,
                {
                    "current_book": html.unescape(title.group(2)).strip(),
                    "current_book_author": html.unescape(author.group(1)).strip() if author else "",
                    "current_book_url": "https://www.goodreads.com" + title.group(1),
                },
            )
    return best[1] if best else None


def load(path):
    """Read the flat key: value file (values are ints or JSON-style strings)."""
    lines, data = path.read_text(encoding="utf-8").splitlines(), {}
    for line in lines:
        m = re.match(r"^(\w+):\s*(.+)$", line)
        if m:
            data[m.group(1)] = json.loads(m.group(2)) if m.group(2)[0] in '"0123456789' else m.group(2)
    return lines, data


def save(path, lines, updates):
    out, seen = [], set()
    for line in lines:
        m = re.match(r"^(\w+):", line)
        if m and m.group(1) in updates:
            key = m.group(1)
            line = f"{key}: {json.dumps(updates[key], ensure_ascii=False)}"
            seen.add(key)
        out.append(line)
    out += [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in updates.items() if k not in seen]
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def main():
    lines, old = load(DATA_FILE)
    updates = {}
    year = datetime.date.today().year

    try:
        n = books_read(year)
        if n is not None:
            updates.update(books_read=n, books_year=year)
        else:
            print("fun facts: books-read count not found; keeping old value")
    except Exception as e:  # noqa: BLE001 - never fail the build
        print(f"fun facts: year-in-books fetch failed ({e}); keeping old value")

    try:
        book = current_book()
        if book:
            updates.update(book)
        else:
            print("fun facts: no current book with a progress update; keeping old value")
    except Exception as e:  # noqa: BLE001
        print(f"fun facts: profile fetch failed ({e}); keeping old value")

    if updates:
        save(DATA_FILE, lines, updates)
    print("fun facts:", {**old, **updates})
    return 0


if __name__ == "__main__":
    sys.exit(main())
