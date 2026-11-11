---
layout: page
title: roulette predictor
description: End-to-end video model that predicts where a roulette ball will land
importance: 2
category: research
---

<p>
<a href="https://github.com/jjzsilva9/roulette-predictor">Code</a> ·
<a href="https://github.com/jjzsilva9/roulette-predictor/blob/main/Predicting-Roulette.pdf">Talk slides (PDF)</a>
</p>

Roulette has been beaten before, by Thorp and Shannon's wearable computer, Small and Tse's deterministic-chaos model, and image-processing approaches. All of them hand-engineer the physics: ball and wheel velocity, tilt, deceleration. This project asks a different question: **can a video model learn the relevant dynamics end-to-end?**

Given a short clip of the ball spinning before it drops, an `r3d_18` 3D CNN pretrained on Kinetics-400 outputs a distribution over the 37 pockets. The backbone is frozen except for its last block, with a small MLP head, and it is trained on the 1,703-video RouletteVision dataset with manually labelled landing pockets.

| Strategy                                 | Test accuracy | Player edge |
| ---------------------------------------- | ------------- | ----------- |
| Top-1 betting                            | 3.12%         | **+12.0%**  |
| Top-5 equal betting                      | 14.84%        | **+6.8%**   |
| Top-5 proportional (stake by confidence) | —             | **+8.4%**   |

The break-even accuracy for top-1 betting is 2.78%. These edges come from a small held-out set filmed on a single wheel, and they vary across runs about as much as the effect size, so they are an interesting signal rather than a reliable strategy.

_Research and educational purposes only._
