---
layout: page
title: LatentWardrobe
description: Diffusion-based texture generation to diversify clothing on 3D crowds (MSc dissertation)
img: assets/img/projects/latentwardrobe.jpg
importance: 1
category: research
---

<p><a href="https://github.com/jjzsilva9/LatentWardrobe">Code</a></p>

My MSc dissertation at Trinity College Dublin, supervised by [Rachel McDonnell](https://www.scss.tcd.ie/Rachel.McDonnell/).

Given a single theme prompt such as _"medieval villagers"_, LatentWardrobe generates a crowd of textured 3D garment meshes that stay on-theme while remaining perceptually diverse: no two members should read as clones.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/latentwardrobe_pipeline.png" title="LatentWardrobe pipeline" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">The pipeline: a per-member prompt, a garment mesh selected against it, and Paint3D texturing from a chosen initial latent.</div>

## Motivation

Texture-diffusion pipelines such as Paint3D (Zeng et al., CVPR 2024) can paint a garment mesh from a text prompt. However, conditional diffusion models systematically under-deliver diversity when sampled repeatedly under the same conditioning, so a naively generated crowd collapses toward near-duplicate outfits.

Perceptual crowd research (McDonnell et al., _Clone Attack!_, SIGGRAPH 2008) shows that viewers reliably detect such appearance clones, and that variation in clothing colour and texture is precisely what masks them. This project studies **training-free interventions** that restore appearance diversity without sacrificing theme coherence.

## Method

Each crowd member is an outfit (top and bottom, or a full-body garment) drawn from a 139-piece CC0 MakeHuman garment library and textured by Paint3D (Stable Diffusion 1.5 with a depth ControlNet). Interventions are applied at three independent points and compared factorially:

| Factor                 | Levels                                                                        |
| ---------------------- | ----------------------------------------------------------------------------- |
| Garment mesh selection | uniform random · CLIP similarity to the theme                                 |
| Initial latent noise   | white · pink                                                                  |
| Per-member prompt      | plain theme · CLIP-sampled clothing description · LLM-evolved description     |

CLIP mesh selection draws outfits pair-coherently, so a top and bottom fit each other as well as the theme.

The LLM method is a WANDER-inspired novelty search: a local Llama 3.1 8B evolves structured clothing descriptions (colour, formality, material, pattern, condition, accessories), keeping mutations only when they increase novelty in CLIP text space. An early version optimised text the renderer can't see and produced a near-monochrome crowd; restricting it to renderable clothing attributes fixed this.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/latentwardrobe_wander.png" title="failed vs corrected novelty search" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">Same theme, same pipeline: the first search optimised text the renderer cannot see (top); restricting evolution to renderable clothing attributes recovers colour and pattern diversity (bottom).</div>

## Evaluation

The evaluation separates three questions: what mesh selection changes on its own, what texturing changes when the meshes are held fixed, and the end-to-end result. Diversity is measured with DINOv2, DreamSim, LPIPS, colour histograms and Vendi scores, alongside CLIPScore for theme coherence, all on masked turntable renders.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/latentwardrobe_comparison.jpg" title="texturing methods on identical meshes" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">Texturing methods on identical meshes. Every column is the same garment mesh and diffusion seed; rows differ only in texturing method (prompt strategy × initial noise), so reading down a column shows exactly, and only, what each method changes.</div>

## Results

- With meshes fixed, CLIP-sampled clothing descriptions are the strongest texture diversifier (Vendi 3.46 vs 3.22 for a plain prompt).
- The WANDER method trades some diversity for the best perceived quality (HPSv2) and theme coherence.
- Theme coherence stays flat across methods: no method pays for diversity with theme drift.
- CLIP-anchored mesh selection costs some silhouette diversity relative to random selection: the expected trade-off between coherence and diversity, made measurable.
