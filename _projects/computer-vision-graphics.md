---
layout: page
title: vision & graphics practicals
description: From camera geometry and SIFT to photometric stereo, path tracing and relighting
img: assets/img/projects/vico.png
importance: 3
category: graphics
---

<p><a href="https://github.com/jjzsilva9/vico">Code</a></p>

Practical notebooks from the third-year Computer Vision and Graphics module at the University of York (I scored 83% in the exam). They move from first principles in image formation to the more visual side of the subject:

- **Image and geometry fundamentals**: meshes, perspective projection, colour, homographies and stereo.
- **Vision and reconstruction**: SIFT features, matching, robust estimation, photometric stereo and 3D recovery.
- **Rendering and appearance**: BRDFs, non-photorealistic rendering, ray tracing, Monte Carlo integration and relighting.

<div class="row">
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/vico_cat.png" title="relit cat" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/vico.png" title="environment relighting" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/vico_dragon.png" title="dragon render" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">A photometric-stereo reconstruction of a cat relit with a new light; Suzanne under environment lighting; a dragon rendered in Mitsuba compared with a MatCap approximation.</div>
