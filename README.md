# Joseph Silva — academic website

Personal academic portfolio built with [al-folio](https://github.com/alshedivat/al-folio) (Jekyll, MIT licence) and hosted on GitHub Pages at <https://jjzsilva9.github.io>.

## Where things live

| What                         | File                                                                 |
| ---------------------------- | -------------------------------------------------------------------- |
| Bio, photo, headline         | `_pages/about.md`, `assets/img/prof_pic.jpg`                         |
| Publications (currently off) | `_bibliography/papers.bib`; restore `_pages/publications.md` from al-folio to show the page |
| Projects                     | one Markdown file per project in `_projects/` (images in `assets/img/projects/`) |
| CV page                      | `assets/pdf/cv.pdf` (shown on /cv/ by `_pages/cv.md`) |
| Social links                 | `_data/socials.yml`                                                  |
| Site name, URL, features     | `_config.yml`                                                        |
| News items (optional)        | add files to `_news/` and set `announcements.enabled: true` in `_pages/about.md` |

Project categories shown on `/projects/` are set by `display_categories` in `_pages/projects.md`; each project picks one with `category:` and is ordered by `importance:`.

## Deploying

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site and pushes the output to the `gh-pages` branch. One-time setup on GitHub:

1. Rename this repository to `jjzsilva9.github.io` (Settings → General).
2. Settings → Actions → General → Workflow permissions: **Read and write**.
3. After the first workflow run finishes, Settings → Pages → Source: **Deploy from a branch**, branch **`gh-pages`**, folder `/ (root)`.

## Local preview

With Docker installed: `docker compose up`, then open <http://localhost:8080>. Or with Ruby 3.3: `bundle install && bundle exec jekyll serve`.
