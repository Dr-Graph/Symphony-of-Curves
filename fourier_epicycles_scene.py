"""
Symphony of Curves
Vertical 9:16 (1080x1920) @ 60 FPS
"""

import sys
import os

from manim import *
import numpy as np
from typst_math import tex_to_svg

OLED_BLACK = "#000000"
MATH_CYAN = "#00E5FF"
MATH_GOLD = "#FFD700"
MATH_AMBER = "#F59E0B"
TITANIUM_WHITE = "#F4F4F6"
MUTED_SLATE = "#94A3B8"

# 9:16 format (1080x1920)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.background_color = OLED_BLACK

class SymphonyOfCurves(Scene):
    def construct(self):
        self.camera.background_color = OLED_BLACK
        
        watermark = Text("@Dr.Graph", font="Arial", weight=BOLD, font_size=24)
        watermark.set_color("#282838").to_edge(DOWN, buff=0.8)
        self.add(watermark)
        
        title = Text(
            "SYMPHONY OF CURVES",
            font="Arial",
            weight=BOLD,
            font_size=42,
            color=TITANIUM_WHITE
        ).move_to(UP * 6.8)
        
        current_formula = tex_to_svg(
            r"z(theta) = 3.5 e^(i theta)",
            font_size=32,
            fill_color="F4F4F6",
            max_width=5.5,
            max_height=0.7
        ).move_to(UP * 5.4)
        
        self.play(
            FadeIn(title, shift=UP * 0.2),
            FadeIn(current_formula, shift=UP * 0.1),
            run_time=0.6
        )
        
        center_pt = DOWN * 0.8
        
        def get_joint_positions(theta_val, freqs, radii, scale=1.0):
            pts = [center_pt.copy()]
            curr = np.array([center_pt[0], center_pt[1]])
            for f, r in zip(freqs, radii):
                r_scaled = r * scale
                curr = curr + np.array([r_scaled * np.cos(f * theta_val), r_scaled * np.sin(f * theta_val)])
                pts.append(np.array([curr[0], curr[1], 0.0]))
            return pts

        def make_closed_curve(freqs, radii, scale=1.0, color=MATH_CYAN, stroke_width=3.2, num_pts=3000):
            thetas = np.linspace(0, 2 * np.pi, num_pts)
            pts = []
            for th in thetas:
                joints = get_joint_positions(th, freqs, radii, scale)
                pts.append(joints[-1])
            curve = VMobject()
            curve.set_points_smoothly(pts)
            curve.set_stroke(color=color, width=stroke_width)
            return curve

        # Stage 1
        s1_freqs = [1]
        s1_radii = [3.4]
        s1_scale = 1.0
        
        theta_s1 = ValueTracker(0.0)
        s1_linkage = always_redraw(lambda: self.build_linkage(
            get_joint_positions(theta_s1.get_value(), s1_freqs, s1_radii, s1_scale),
            arm_color=MATH_CYAN,
            pivot_color=TITANIUM_WHITE
        ))
        s1_curve = make_closed_curve(s1_freqs, s1_radii, s1_scale, color=MATH_CYAN, stroke_width=3.5)
        
        self.add(s1_linkage)
        self.play(
            Create(s1_curve, rate_func=linear),
            theta_s1.animate(rate_func=linear).set_value(2 * np.pi),
            run_time=2.0
        )
        self.wait(0.3)
        
        # Stage 2
        s2_freqs = [1, -3]
        s2_radii = [2.7, 0.9]
        s2_scale = 1.0
        
        new_formula_s2 = tex_to_svg(
            r"z(theta) = 2.7 e^(i theta) + 0.9 e^(-3 i theta)",
            font_size=30,
            fill_color="F4F4F6",
            max_width=6.0,
            max_height=0.7
        ).move_to(UP * 5.4)
        
        self.play(
            FadeOut(s1_curve, run_time=0.35),
            Transform(current_formula, new_formula_s2, run_time=0.35),
        )
        
        theta_s2 = ValueTracker(0.0)
        self.remove(s1_linkage)
        
        s2_linkage = always_redraw(lambda: self.build_linkage(
            get_joint_positions(theta_s2.get_value(), s2_freqs, s2_radii, s2_scale),
            arm_color=MATH_CYAN,
            pivot_color=TITANIUM_WHITE
        ))
        s2_curve = make_closed_curve(s2_freqs, s2_radii, s2_scale, color=MATH_CYAN, stroke_width=3.5)
        
        self.add(s2_linkage)
        self.play(
            Create(s2_curve, rate_func=linear),
            theta_s2.animate(rate_func=linear).set_value(2 * np.pi),
            run_time=6.05
        )
        self.wait(0.3)
        
        # Stage 3
        s3_freqs = [27, -17, 11]
        s3_radii = [1.0, 3.0, 9.0]
        s3_scale = 3.4 / 13.0
        
        new_formula_s3 = tex_to_svg(
            r"z(theta) = e^(27 theta i) + 3 e^(-17 theta i) + 9 e^(11 theta i)",
            font_size=30,
            fill_color="F4F4F6",
            max_width=6.5,
            max_height=0.7
        ).move_to(UP * 5.4)
        
        self.play(
            FadeOut(s2_curve, run_time=0.35),
            Transform(current_formula, new_formula_s3, run_time=0.35),
        )
        self.wait(0.05)
        
        theta_s3 = ValueTracker(0.0)
        self.remove(s2_linkage)
        
        s3_linkage = always_redraw(lambda: self.build_linkage(
            get_joint_positions(theta_s3.get_value(), s3_freqs, s3_radii, s3_scale),
            arm_color=MATH_CYAN,
            pivot_color=TITANIUM_WHITE,
            stroke_width=2.5
        ))
        s3_curve = make_closed_curve(s3_freqs, s3_radii, s3_scale, color=TITANIUM_WHITE, stroke_width=2.8, num_pts=3000)
        
        self.add(s3_linkage)
        self.play(
            Create(s3_curve, rate_func=linear),
            theta_s3.animate(rate_func=linear).set_value(2 * np.pi),
            run_time=6.6
        )
        self.wait(0.3)
        
        # Stage 4
        s4_freqs = [33, -23, 13, -3]
        s4_radii = [1.0, 2.5, 4.0, 6.0]
        s4_scale = 3.5 / 13.5
        
        new_formula_s4 = tex_to_svg(
            r"z(theta) = sum_(k=1)^4 r_k e^(i omega_k theta)",
            font_size=48,
            fill_color="FFD700",
            max_width=7.2,
            max_height=1.35
        ).move_to(UP * 5.4)
        
        self.play(
            FadeOut(s3_curve, run_time=0.35),
            Transform(current_formula, new_formula_s4, run_time=0.35),
        )
        
        theta_s4 = ValueTracker(0.0)
        self.remove(s3_linkage)
        
        s4_linkage = always_redraw(lambda: self.build_linkage(
            get_joint_positions(theta_s4.get_value(), s4_freqs, s4_radii, s4_scale),
            arm_color=MATH_GOLD,
            pivot_color=TITANIUM_WHITE,
            stroke_width=2.0
        ))
        s4_curve = make_closed_curve(s4_freqs, s4_radii, s4_scale, color=MATH_GOLD, stroke_width=2.4, num_pts=4000)
        
        self.add(s4_linkage)
        self.play(
            Create(s4_curve, rate_func=linear),
            theta_s4.animate(rate_func=linear).set_value(2 * np.pi),
            run_time=6.6
        )
        self.wait(0.3)
        
        # Stage 5
        s5_freqs = [1, -7, 17, -31, 49]
        s5_radii = [4.0, 2.2, 1.2, 0.7, 0.4]
        s5_scale = 3.5 / 8.5
        
        new_formula_s5 = tex_to_svg(
            r"z(theta) = sum_(k=1)^5 r_k e^(i omega_k theta)",
            font_size=48,
            fill_color="F59E0B",
            max_width=7.2,
            max_height=1.35
        ).move_to(UP * 5.4)
        
        self.play(
            FadeOut(s4_curve, run_time=0.35),
            Transform(current_formula, new_formula_s5, run_time=0.35),
        )
        
        theta_s5 = ValueTracker(0.0)
        self.remove(s4_linkage)
        
        s5_linkage = always_redraw(lambda: self.build_linkage(
            get_joint_positions(theta_s5.get_value(), s5_freqs, s5_radii, s5_scale),
            arm_color=MATH_AMBER,
            pivot_color=TITANIUM_WHITE,
            stroke_width=1.8
        ))
        s5_curve = make_closed_curve(s5_freqs, s5_radii, s5_scale, color=TITANIUM_WHITE, stroke_width=2.2, num_pts=5000)
        
        self.add(s5_linkage)
        self.play(
            Create(s5_curve, rate_func=linear),
            theta_s5.animate(rate_func=linear).set_value(2 * np.pi),
            run_time=7.0
        )
        self.wait(0.3)
        
        # Stage 6
        s6_freqs = [1, -11, 25, -35, 49, -59]
        s6_radii = [3.5, 2.0, 1.2, 0.7, 0.4, 0.2]
        s6_scale = 3.5 / 8.0
        
        new_formula_s6 = tex_to_svg(
            r"z(theta) = sum_(k=1)^6 r_k e^(i omega_k theta)",
            font_size=48,
            fill_color="00E5FF",
            max_width=7.2,
            max_height=1.35
        ).move_to(UP * 5.4)
        
        self.play(
            FadeOut(s5_curve, run_time=0.35),
            Transform(current_formula, new_formula_s6, run_time=0.35),
        )
        
        theta_s6 = ValueTracker(0.0)
        self.remove(s5_linkage)
        
        s6_linkage = always_redraw(lambda: self.build_linkage(
            get_joint_positions(theta_s6.get_value(), s6_freqs, s6_radii, s6_scale),
            arm_color=MATH_CYAN,
            pivot_color=TITANIUM_WHITE,
            stroke_width=1.6
        ))
        s6_curve = make_closed_curve(s6_freqs, s6_radii, s6_scale, color=MATH_CYAN, stroke_width=2.4, num_pts=6000)
        
        self.add(s6_linkage)
        self.play(
            Create(s6_curve, rate_func=linear),
            theta_s6.animate(rate_func=linear).set_value(2 * np.pi),
            run_time=7.2
        )
        self.wait(0.3)
        
        # Stage 7
        s7_freqs = [1, -15, 17, -31]
        s7_radii = [3.2, 1.4, 0.9, 0.4]
        s7_scale = 3.5 / 5.9
        
        new_formula_s7 = tex_to_svg(
            r"z(theta) = 3.2 e^(i theta) + 1.4 e^(-15 i theta) + 0.9 e^(17 i theta) + 0.4 e^(-31 i theta)",
            font_size=28,
            fill_color="FFD700",
            max_width=6.6,
            max_height=0.7
        ).move_to(UP * 5.4)
        
        self.play(
            FadeOut(s6_curve, run_time=0.35),
            Transform(current_formula, new_formula_s7, run_time=0.35),
        )
        
        theta_s7 = ValueTracker(0.0)
        self.remove(s6_linkage)
        
        s7_linkage = always_redraw(lambda: self.build_linkage(
            get_joint_positions(theta_s7.get_value(), s7_freqs, s7_radii, s7_scale),
            arm_color=MATH_GOLD,
            pivot_color=TITANIUM_WHITE,
            stroke_width=1.8
        ))
        s7_curve = make_closed_curve(s7_freqs, s7_radii, s7_scale, color=MATH_GOLD, stroke_width=2.8, num_pts=6000)
        
        self.add(s7_linkage)
        self.play(
            Create(s7_curve, rate_func=linear),
            theta_s7.animate(rate_func=linear).set_value(2 * np.pi),
            run_time=7.0
        )
        
        # Outro
        fourier_formula = tex_to_svg(
            r"lim_(N -> oo) sum_(k=-N)^N c_k e^(i k omega_0 t) = f(t)",
            font_size=48,
            fill_color="F4F4F6",
            max_width=7.5,
            max_height=1.35
        ).move_to(UP * 5.4)
        
        self.remove(s7_linkage)
        
        self.play(
            Transform(current_formula, fourier_formula),
            s7_curve.animate.set_stroke(color=TITANIUM_WHITE, width=3.2),
            run_time=1.0
        )
        
        self.play(
            s7_curve.animate.set_stroke(color=MATH_CYAN, width=3.5),
            run_time=1.0
        )
        
        self.play(
            FadeOut(title),
            FadeOut(current_formula),
            FadeOut(s7_curve),
            FadeOut(watermark),
            run_time=1.0
        )

    def build_linkage(self, pts, arm_color=MATH_CYAN, pivot_color=TITANIUM_WHITE, stroke_width=3.0):
        group = VGroup()
        for i in range(len(pts) - 1):
            p1, p2 = pts[i], pts[i+1]
            line = Line(p1, p2, stroke_color=arm_color, stroke_width=stroke_width, stroke_opacity=0.9)
            pivot = Dot(p1, radius=0.07, color=pivot_color)
            group.add(line, pivot)
        tip_dot = Dot(pts[-1], radius=0.08, color=MATH_GOLD)
        group.add(tip_dot)
        return group
