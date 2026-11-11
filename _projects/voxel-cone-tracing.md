---
layout: page
title: voxel cone tracing
description: Real-time global illumination in Sponza with a sparse voxel octree (C++/OpenGL)
img: assets/img/projects/vct.jpg
importance: 1
category: graphics
---

<p><a href="https://github.com/jjzsilva9/real-time-rendering">Code</a></p>

The final project for the Real-Time Rendering module at Trinity College Dublin: real-time diffuse and specular global illumination in the Sponza atrium. It implements the core of Crassin et al.'s _Interactive Indirect Illumination Using Voxel Cone Tracing_ on a sparse voxel octree based on Laine and Karras's _Efficient Sparse Voxel Octrees_.

<div style="position: relative; width: 100%; aspect-ratio: 16 / 9; margin-bottom: 1rem;">
  <iframe src="https://www.youtube-nocookie.com/embed/weibWkdd3cc" title="Voxel cone tracing demo" style="position: absolute; inset: 0; width: 100%; height: 100%; border: 0;" allowfullscreen loading="lazy"></iframe>
</div>

## Pipeline

- **CPU voxelisation** of the static scene into a sparse voxel octree at startup (128³ by default).
- **Light-view pass** rendering albedo and shadow from the light's point of view.
- **Radiance injection** using a pull-style per-voxel projection into the light-view map, avoiding the atomics of the paper's push-style splat.
- **Mip filtering**: bottom-up propagation of radiance through the octree.
- **G-buffer and deferred shading**, tracing diffuse and specular cones through the octree for indirect light.

## Earlier labs

The same repository builds up to this through four labs, each with an ImGui panel for live parameters: Phong, Gooch and Oren–Nayar shading; reflection and refraction with chromatic dispersion and a Schlick Fresnel term; tangent-space normal mapping; and a comparison of mipmap filtering modes.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/rtr_lab1.jpg" title="shading models lab" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">Lab 1: Phong, Gooch and Oren–Nayar shading on the Utah teapot.</div>
