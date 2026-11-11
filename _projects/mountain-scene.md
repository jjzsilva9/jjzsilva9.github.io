---
layout: page
title: mountain scene
description: OpenGL scene with animated griffins, normal mapping and a day–night cycle
img: assets/img/projects/mountain.png
importance: 2
category: graphics
---

<p>
<a href="https://github.com/jjzsilva9/opengl-graphics">Code</a> ·
<a href="https://www.youtube.com/watch?v=HNvmNoOzFQk">Demo video</a>
</p>

The individual OpenGL project for the Computer Graphics module (CS7GV6) at Trinity College Dublin: a mountainous scene with animated griffins.

- **Blinn–Phong shading** with directional lighting computed in tangent space.
- **Tangent-space normal mapping**, with the TBN matrix built in the vertex shader using Gram–Schmidt and a runtime intensity control.
- **Day–night cycle** interpolating light colour, intensity and position through night, dawn, day and dusk. The time of day also drives the fog colour and the skybox hue.
- A **GUI** for changing scene parameters live.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/mountain.png" title="scene overview" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/mountain_daynight.png" title="day-night cycle" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">Scene overview (top) and the day–night cycle (bottom).</div>
