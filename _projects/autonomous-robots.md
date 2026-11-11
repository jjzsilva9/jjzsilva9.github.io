---
layout: page
title: autonomous retrieval robots
description: Decentralised multi-robot item collection with ROS 2 and Nav2
img: assets/img/projects/auro.jpg
importance: 1
category: robotics
---

<p>
<a href="https://github.com/jjzsilva9/auro-assessment">Code</a> ·
<a href="https://github.com/jjzsilva9/auro-assessment/blob/main/AURO_Report.pdf">Report (PDF)</a>
</p>

Coursework for the final-year Autonomous Robotics module at the University of York: a team of robots that find, retrieve and deposit items efficiently.

The system is a decentralised, homogeneous multi-robot system with explicit communication to aid planning. It uses a deliberative architecture with reactive elements for navigation, and borrows from microservice architecture to stay modular. Each robot's controller runs a finite state machine, with Nav2's behaviour tree handling navigation. Separate nodes detect items, estimate their 3D positions and maintain a shared list of observed items that the controllers query to choose their next target.

<div class="row">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/auro.jpg" title="simulation world" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/auro_arch.png" title="architecture" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">The simulated arena (left) and the system architecture (right).</div>
