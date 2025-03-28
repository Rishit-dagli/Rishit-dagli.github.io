---
title: "A Collection of 3D Reconstruction Scenes and Trained Splats"
date: 2025-03-28
excerpt: "A dataset of 3D reconstruction scenes."
image: /assets/nerf-gs-datasets/cover.jpg
---

{% include cover.html url="/assets/nerf-gs-datasets/cover.jpg" description="Some scenes from the dataset." %}

<div style="text-align: center; margin: 30px 0;">
  <a href="https://huggingface.co/datasets/rishitdagli/nerf-gs-datasets" target="_blank" rel="noopener" style="background-color: #000; color: #fff; padding: 10px 20px; border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; gap: 8px;">
    <span class="icon" style="font-size:18px">🤗</span> Dataset
  </a>
</div>

The data required for training NeRFs and Gaussian Splats is often much smaller than what used to be required for doing 3D reconstruction. There are quite quite a few formats for the per-scene datasets for training these methods. I often had problems on training such radiance fields on multiple datasets while working on any training, thus I share a collection of 3D reconstruction scenes gathered from various sources, each accompanied by a pre-trained Gaussian Splat model.

Each scene in the dataset usually includes:

- Multi-view image sequences with camera parameters
- Calibration information
- A pre-trained Gaussian Splat model optimized for the scene

{% include bibtex.html %}