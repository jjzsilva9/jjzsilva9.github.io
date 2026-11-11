---
layout: page
title: viewpoint motion prediction
description: Predicting player viewpoint motion for cloud gaming, and using it to guide the video encoder (BEng project with AMD)
img: assets/img/projects/viewpoint_qpmap.png
importance: 1
category: research
---

<p>
<a href="https://github.com/jjzsilva9/viewpoint-prediction">Code</a> ·
<a href="https://github.com/jjzsilva9/viewpoint-prediction/blob/main/Final_Year_Project%20(5).pdf">Report (PDF)</a>
</p>

My final-year research project at the University of York, completed in partnership with AMD. It received a mark of 82% and was presented at the **2025 AMD Global Technical Authors Conference**, where it won **second place** in its stream.

Cloud gaming adds a network round trip between a player's input and the frame they see. If we can predict where the player's viewpoint will move, the server can render and deliver those frames ahead of time. This project builds predictive models trained on speedruns of _Doom_, and uses the predictions to help the video encoder too.

## Models

A baseline seq2seq LSTM predicts future motion vectors from past motion alone. The main multimodal model adds the semantic segmentation map and depth map of each frame: a _content_ LSTM encodes the convolved image features, an _inertia_ LSTM encodes past motion, and a _fusion_ LSTM combines the two before decoding motion predictions one frame at a time.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/viewpoint_arch.png" title="multimodal seq2seq architecture" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">The multimodal seq2seq architecture: content, inertia and fusion LSTMs in both encoder and decoder.</div>

## Encoder assistance

Predicted motion tells us which pixels are likely to stay in view. Each frame's depth map is lifted to a point cloud, transformed by the predicted motion and reprojected. This produces heatmaps that are blurred, weighted and passed to the encoder as QP maps, so regions that will remain visible are compressed less.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/viewpoint.png" title="point cloud reprojection" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="row">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/viewpoint_qpmap.png" title="QP map" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/viewpoint_vmaf.png" title="H.265 VMAF" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">Top: frame with reprojected point cloud. Bottom left: QP map derived from predictions. Bottom right: VMAF for H.265 encodes.</div>

## Results

- The image model beats the motion-only model in MSE and percentage error over the prediction windows that matter for cloud gaming (round trips under about 200 ms).
- Accounting for inference time, it could mask up to **171 ms** of round-trip latency, a 51 ms increase over the 120 ms reported by Outatime.
- Prediction-guided QP maps improve VMAF over a vanilla encode for H.264, H.265 and AV1.
