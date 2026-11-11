---
layout: page
title: LatentWardrobe
description: Diffusion-based texture generation to diversify clothing on 3D crowds (MSc dissertation)
importance: 0
category: research
# img: assets/img/projects/latentwardrobe.png  # add a teaser image and uncomment to show it on the projects card
---

MSc dissertation at Trinity College Dublin, supervised by [Rachel McDonnell](https://www.scss.tcd.ie/Rachel.McDonnell/).

Given a single theme prompt such as _"medieval villagers"_, LatentWardrobe generates a crowd of textured 3D garment meshes that stay on-theme while remaining perceptually diverse: no two members should read as clones.

{% comment %}
Add the mesh-fixed comparison figure here once it's in assets/img/projects/, e.g.
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/latentwardrobe_comparison.png" title="texturing methods on identical meshes" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">Texturing methods on identical meshes. Every column is the same garment mesh and diffusion seed; rows differ only in texturing method (prompt strategy × initial noise), so reading down a column shows exactly, and only, what each method changes.</div>
{% endcomment %}

## Motivation

Texture-diffusion pipelines such as Paint3D (Zeng et al., CVPR 2024) can paint a garment mesh from a text prompt. However, conditional diffusion models systematically under-deliver diversity when sampled repeatedly under the same conditioning, so a naively generated crowd collapses toward near-duplicate outfits.

Perceptual crowd research (McDonnell et al., _Clone Attack!_, SIGGRAPH 2008) shows that viewers reliably detect such appearance clones, and that variation in clothing colour and texture is precisely what masks them. This project studies **training-free interventions** that restore appearance diversity without sacrificing theme coherence.
