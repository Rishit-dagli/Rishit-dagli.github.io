---
title: "Reconstruct-It! A Collection of 3D Reconstruction Datasets and Trained Splats"
date: 2025-03-28
excerpt: "This collection brings together 77 carefully curated scenes with multi-view sequences, camera parameters, and pre-trained Gaussian Splats—everything you need to jump into radiance field training."
image: /assets/nerf-gs-datasets/cover.jpg
tags: [3d-reconstruction, machine-learning]
---

{% include cover.html url="/assets/nerf-gs-datasets/cover.jpg" description="Some scenes from the dataset." %}

<div style="text-align: center; margin: 30px 0;">
  <a href="https://huggingface.co/datasets/rishitdagli/nerf-gs-datasets" target="_blank" rel="noopener" style="background-color: #000; color: #fff; padding: 10px 20px; border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; gap: 8px;">
    <span class="icon" style="font-size:18px">🤗</span> Dataset
  </a>
</div>

The data required for training NeRFs and Gaussian Splats is often much smaller than what used to be required for doing 3D reconstruction. There are quite quite a few formats for the per-scene datasets for training these methods. I often had problems on training such radiance fields on multiple datasets while working on any training, thus I share a collection of 3D reconstruction scenes gathered from various sources, each accompanied by a trained Gaussian Splat.

There are 77 scenes in this collection. Each scene in the dataset usually includes:

- Multi-view image sequences with camera parameters
- Calibration information
- A pre-trained Gaussian Splat model optimized for the scene

All the datasets in the collection are taken from various different sources and have different licenses.

{% include bibtex.html %}
