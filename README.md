# 🎻 Symphony of Curves — 7-Axis Fourier Epicycle Engine

Official Python animation code for the YouTube Short: **[Symphony of Curves](https://youtube.com/shorts/4eq2YjiiyaM)** by **[@DrGraph](https://youtube.com/@DrGraph-dxdy)**.

Parametric curve decomposition into rotating circular epicycles:
$$z(\theta) = \sum_{k=1}^{n} r_k \, e^{i (\omega_k \theta + \phi_k)}$$

---

## 🚀 Quickstart

### 1. Requirements
- Python 3.10+
- [Manim Community Edition](https://docs.manim.community/)
- [Typst](https://typst.app/)

```bash
pip install -r requirements.txt
```

### 2. Render the 60 FPS Video
```bash
manim -qh -r 1080,1920 --fps 60 fourier_epicycles_scene.py SymphonyOfCurves
```

---

## 🎬 Channel
- **YouTube**: [@DrGraph-dxdy](https://youtube.com/@DrGraph-dxdy)
- **Soundtrack**: *"Can You Hear The Music"* – Ludwig Göransson
