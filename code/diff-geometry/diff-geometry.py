from manim import *
import numpy as np

class SpringMassSystemBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"
            self.spring_color = "#4a90e2"
            self.mass_color = "#e74c3c"
            self.label_color = "#f39c12"
            self.origin_color = "#ecf0f1"
            self.mass_label_color = WHITE
        else:
            self.camera.background_color = WHITE
            self.spring_color = "#2980b9"
            self.mass_color = "#c0392b"
            self.label_color = "#d35400"
            self.origin_color = "#2c3e50"
            self.mass_label_color = WHITE

    def construct(self):
        spring_length = 6
        num_coils = 12
        amplitude = 0.5
        
        def spring_func(t):
            x = t * spring_length
            y = amplitude * np.sin(num_coils * 2 * PI * t)
            return np.array([x, y, 0])
        
        spring = ParametricFunction(
            spring_func,
            t_range=[0, 1, 0.005],
            stroke_width=4,
            color=self.spring_color
        )
        
        mass = Rectangle(
            width=1.2,
            height=1.2,
            fill_color=self.mass_color,
            fill_opacity=0.8,
            stroke_color=self.mass_label_color,
            stroke_width=3
        ).move_to([spring_length, 0, 0])
        
        mass_label = Text("m", font_size=48, color=self.mass_label_color).move_to(mass.get_center())
        origin = Dot([0, 0, 0], radius=0.15, color=self.origin_color)
        distance_label = Text("q", font_size=48, color=self.label_color).move_to([spring_length/2, -1.5, 0])
        distance_line = Line([0, -1.2, 0], [spring_length, -1.2, 0], color=self.label_color, stroke_width=3)
        left_marker = Line([0, -1.0, 0], [0, -1.4, 0], color=self.label_color, stroke_width=3)
        right_marker = Line([spring_length, -1.0, 0], [spring_length, -1.4, 0], color=self.label_color, stroke_width=3)
        
        everything = VGroup(origin, spring, mass, mass_label, distance_line, left_marker, right_marker, distance_label)
        everything.move_to(ORIGIN)
        everything.scale(2.0)
        
        self.add(everything)

class SpringMassSystem(SpringMassSystemBase):
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class SpringMassSystemDark(SpringMassSystemBase):
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)


class TangentCovectorSpaceBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"
            self.ellipse_color = "#4a90e2"
            self.point_color = "#e74c3c"
            self.tangent_color = "#2ecc71"
            self.covector_color = "#f39c12"
            self.label_color = WHITE
        else:
            self.camera.background_color = WHITE
            self.ellipse_color = "#2980b9"
            self.point_color = "#c0392b"
            self.tangent_color = "#27ae60"
            self.covector_color = "#d35400"
            self.label_color = BLACK

    def construct(self):
        ellipse = Ellipse(
            width=6, 
            height=4, 
            color=self.ellipse_color, 
            stroke_width=4
        )
        
        ellipse_label = MathTex("X", font_size=48, color=self.ellipse_color).move_to([0, 0.5, 0])
        
        t_param = PI/4
        point_q_coords = np.array([
            3 * np.cos(t_param),
            2 * np.sin(t_param),
            0
        ])
        
        point_q = Dot(point_q_coords, radius=0.12, color=self.point_color)
        point_q_label = MathTex("q", font_size=36, color=self.point_color).next_to(point_q, DR, buff=0.2)
        
        a, b = 3, 2
        x_q, y_q = point_q_coords[0], point_q_coords[1]
        tangent_slope = -(b**2 * x_q) / (a**2 * y_q) if y_q != 0 else float('inf')
        
        if tangent_slope != float('inf'):
            tangent_direction = np.array([1, tangent_slope, 0])
            tangent_direction = tangent_direction / np.linalg.norm(tangent_direction[:2])
        else:
            tangent_direction = np.array([0, 1, 0])
        
        perp_direction = np.array([-tangent_direction[1], tangent_direction[0], 0])
        
        rect_width = 2.0
        rect_height = 0.8
        
        tangent_rect = Rectangle(
            width=rect_width,
            height=rect_height,
            color=self.tangent_color,
            fill_color=self.tangent_color,
            fill_opacity=0.3,
            stroke_width=3
        )
        
        tangent_rect.move_to(point_q_coords + 0.8 * tangent_direction)
        angle = np.arctan2(tangent_direction[1], tangent_direction[0])
        tangent_rect.rotate(angle)
        
        tangent_label = MathTex("T_q X", font_size=36, color=self.tangent_color).next_to(
            tangent_rect, UP if tangent_direction[1] >= 0 else DOWN, buff=0.2
        )
        
        normal_direction = np.array([-tangent_direction[1], tangent_direction[0], 0])
        covector_length = 1.5
        
        covector_start = point_q_coords
        covector_end = point_q_coords + covector_length * normal_direction
        
        covector_arrow = Arrow(
            covector_start, 
            covector_end, 
            color=self.covector_color, 
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        covector_label = MathTex("p", font_size=36, color=self.covector_color).next_to(covector_end, LEFT, buff=0.2)
        
        everything = VGroup(
            ellipse, ellipse_label, point_q, point_q_label, 
            tangent_rect, tangent_label, covector_arrow, covector_label
        )
        everything.scale(1.3)
        
        self.add(everything)

class TangentCovectorSpace(TangentCovectorSpaceBase):
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class TangentCovectorSpaceDark(TangentCovectorSpaceBase):
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)


class CylindricalCrossProductBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"
            self.ellipse_color = "#4a90e2"
            self.line_color = "#2ecc71"
            self.special_line_color = "#e74c3c"
            self.config_point_color = "#f39c12"
            self.state_point_color = "#9b59b6"
            self.label_color = WHITE
        else:
            self.camera.background_color = WHITE
            self.ellipse_color = "#2980b9"
            self.line_color = "#27ae60"
            self.special_line_color = "#c0392b"
            self.config_point_color = "#d35400"
            self.state_point_color = "#8e44ad"
            self.label_color = BLACK

    def construct(self):
        ellipse = Ellipse(
            width=4, 
            height=3, 
            color=self.ellipse_color, 
            stroke_width=4
        )
        
        ellipse_label = MathTex("S^1", font_size=36, color=self.ellipse_color).next_to(ellipse, DOWN, buff=0.3)
        
        lines = VGroup()
        num_lines = 24
        line_length = 2.5
        
        a, b = 2, 1.5
        perspective_direction = np.array([0.3, 1, 0])
        
        special_line_index = 6
        special_line = None
        configuration_point = None
        
        for i in range(num_lines):
            t = i * 2 * PI / num_lines
            
            ellipse_point = np.array([
                a * np.cos(t),
                b * np.sin(t),
                0
            ])
            
            line_start = ellipse_point - line_length * perspective_direction
            line_end = ellipse_point + line_length * perspective_direction
            
            if i == special_line_index:
                line = Line(
                    line_start,
                    line_end,
                    color=self.special_line_color,
                    stroke_width=4,
                    stroke_opacity=1.0
                )
                special_line = line
                configuration_point = ellipse_point
            else:
                line = Line(
                    line_start,
                    line_end,
                    color=self.line_color,
                    stroke_width=2,
                    stroke_opacity=0.8
                )
            
            lines.add(line)
        
        top_ellipse = Ellipse(
            width=4, 
            height=3, 
            color=self.line_color,
            stroke_width=3,
            stroke_opacity=0.8
        )
        
        bottom_ellipse = Ellipse(
            width=4, 
            height=3, 
            color=self.line_color,
            stroke_width=3,
            stroke_opacity=0.8
        )
        
        top_ellipse.shift(line_length * perspective_direction)
        bottom_ellipse.shift(-line_length * perspective_direction)
        
        connecting_lines = VGroup()
        num_surface_lines = 8
        
        for i in range(num_surface_lines):
            t = i * 2 * PI / num_surface_lines
            
            middle_point = np.array([a * np.cos(t), b * np.sin(t), 0])
            top_point = middle_point + line_length * perspective_direction
            bottom_point = middle_point - line_length * perspective_direction
            
            top_surface_line = Line(
                middle_point,
                top_point,
                color=self.line_color,
                stroke_width=1.5,
                stroke_opacity=0.4
            )
            
            bottom_surface_line = Line(
                middle_point,
                bottom_point,
                color=self.line_color,
                stroke_width=1.5,
                stroke_opacity=0.4
            )
            
            connecting_lines.add(top_surface_line, bottom_surface_line)
        
        config_dot = Dot(configuration_point, radius=0.10, color=self.config_point_color)
        config_label = Text("configuration", font_size=24, color=self.config_point_color).next_to(config_dot, LEFT, buff=0.3)
        
        state_position = configuration_point + 1.2 * perspective_direction
        state_dot = Dot(state_position, radius=0.10, color=self.state_point_color)
        state_label = Text("state", font_size=24, color=self.state_point_color).next_to(state_dot, RIGHT, buff=0.2)
        
        cross_product_label = MathTex("S^1 \\times \\mathbb{R}", font_size=42, color=self.label_color).to_edge(UP, buff=0.5)
        
        everything = VGroup(
            bottom_ellipse, connecting_lines, lines, ellipse, ellipse_label, top_ellipse, 
            cross_product_label, config_dot, config_label, state_dot, state_label
        )
        everything.scale(0.9)
        
        self.add(everything)

class CylindricalCrossProduct(CylindricalCrossProductBase):
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class CylindricalCrossProductDark(CylindricalCrossProductBase):
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)


class SkewSymmetricMatrixBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"
            self.basis_color = "#2ecc71"
            self.matrix_color = WHITE
            self.arrow_color = "#f39c12"
            self.form_color = "#4a90e2"
            self.label_color = WHITE
        else:
            self.camera.background_color = WHITE
            self.basis_color = "#27ae60"
            self.matrix_color = BLACK
            self.arrow_color = "#d35400"
            self.form_color = "#2980b9"
            self.label_color = BLACK

    def construct(self):
        basis_vectors = VGroup()
        n = 3
        
        for i in range(n):
            basis_p = MathTex(f"\\frac{{\\partial}}{{\\partial p_{i+1}}}", font_size=28, color=self.basis_color)
            basis_vectors.add(basis_p)
        
        dots1 = MathTex("\\vdots", font_size=28, color=self.basis_color)
        basis_vectors.add(dots1)
        
        for i in range(n):
            basis_q = MathTex(f"\\frac{{\\partial}}{{\\partial q^{i+1}}}", font_size=28, color=self.basis_color)
            basis_vectors.add(basis_q)
        
        basis_vectors.arrange(DOWN, buff=0.3)
        
        beta_label = MathTex("\\beta", "=", font_size=36, color=self.basis_color)
        beta_label.next_to(basis_vectors, LEFT, buff=0.5)
        beta_label.align_to(basis_vectors, UP).shift(DOWN * basis_vectors.height / 2)
        
        matrix_latex = MathTex(
            r"\begin{pmatrix}"
            r"0 & \cdots & 0 & 1 & \cdots & 0 \\"
            r"\vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\"
            r"0 & \cdots & 0 & 0 & \cdots & 1 \\"
            r"-1 & \cdots & 0 & 0 & \cdots & 0 \\"
            r"\vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\"
            r"0 & \cdots & -1 & 0 & \cdots & 0"
            r"\end{pmatrix}",
            font_size=32,
            color=self.matrix_color
        )
        
        equation_left = MathTex("_\\beta[\\omega]_\\beta", "=", font_size=36, color=self.matrix_color)
        equation_left.next_to(matrix_latex, LEFT, buff=0.8)
        
        basis_with_beta = VGroup(beta_label, basis_vectors)
        basis_with_beta.next_to(matrix_latex, RIGHT, buff=1.5)
        
        basis_arrow = Arrow(
            basis_vectors.get_top() + RIGHT * 0.5,
            basis_vectors.get_bottom() + RIGHT * 0.5,
            color=self.arrow_color, stroke_width=3
        )
        basis_label_text = Text("ordered\nbasis", font_size=24, color=self.arrow_color).next_to(basis_arrow, RIGHT, buff=0.3)
        
        matrix_left = matrix_latex.get_left()[0]
        matrix_right = matrix_latex.get_right()[0]
        matrix_center = (matrix_left + matrix_right) / 2
        matrix_bottom = matrix_latex.get_bottom()[1] - 0.8
        
        left_arrow = DoubleArrow(
            [matrix_left, matrix_bottom, 0], 
            [matrix_center, matrix_bottom, 0], 
            color=self.arrow_color, stroke_width=2
        )
        n_label_left = MathTex("n", color=self.arrow_color, font_size=32).next_to(left_arrow, DOWN, buff=0.2)
        
        right_arrow = DoubleArrow(
            [matrix_center, matrix_bottom, 0], 
            [matrix_right, matrix_bottom, 0], 
            color=self.arrow_color, stroke_width=2
        )
        n_label_right = MathTex("n", color=self.arrow_color, font_size=32).next_to(right_arrow, DOWN, buff=0.2)
        
        diff_form = MathTex("dp_i \\wedge dq^i", font_size=36, color=self.form_color)
        diff_form.next_to(matrix_latex, DOWN, buff=2.5)
        
        brace = Brace(diff_form, DOWN, color=self.form_color)
        brace_label = Text("skew-symmetric\nbilinear form", font_size=24, color=self.form_color).next_to(brace, DOWN, buff=0.2)
        
        bilinear_form = MathTex("(\\cdot, \\cdot)", font_size=36, color=self.form_color).next_to(diff_form, RIGHT, buff=0.5)
        
        all_elements = VGroup(
            equation_left, matrix_latex,
            left_arrow, right_arrow, n_label_left, n_label_right,
            basis_with_beta, basis_arrow, basis_label_text, 
            diff_form, brace, brace_label, bilinear_form
        )
        
        all_elements.move_to(ORIGIN)
        all_elements.scale(0.75)
        
        self.add(all_elements)

class SkewSymmetricMatrix(SkewSymmetricMatrixBase):
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class SkewSymmetricMatrixDark(SkewSymmetricMatrixBase):
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)


class HamiltonianVectorFieldBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"
            self.blob_color = "#4a90e2"
            self.blob_fill_color = "#2c3e50"
            self.vector_color = "#e74c3c"
            self.curve_color = "#f39c12"
            self.point_color = "#9b59b6"
            self.label_color = WHITE
        else:
            self.camera.background_color = WHITE
            self.blob_color = "#2980b9"
            self.blob_fill_color = "#d6eaf8"
            self.vector_color = "#c0392b"
            self.curve_color = "#d35400"
            self.point_color = "#8e44ad"
            self.label_color = BLACK

    def construct(self):
        def blob_func(t):
            base_radius = 4.0
            irregularity = 0.4 * (np.sin(3*t) + 0.5*np.sin(7*t) + 0.3*np.sin(11*t))
            radius = base_radius + irregularity
            x = radius * np.cos(t)
            y = radius * np.sin(t)
            return np.array([x, y, 0])
        
        blob = ParametricFunction(
            blob_func,
            t_range=[0, 2*PI, 0.05],
            color=self.blob_color,
            fill_color=self.blob_fill_color,
            fill_opacity=0.3,
            stroke_width=2
        )
        
        vectors = VGroup()
        vector_labels = VGroup()
        num_vectors = 15
        
        for i in range(num_vectors):
            angle = i * 2 * PI / num_vectors
            radius_factor = 0.3 + 0.4 * (i % 3) / 2
            base_pos_x = radius_factor * 3.0 * np.cos(angle)
            base_pos_y = radius_factor * 3.0 * np.sin(angle)
            vector_start = np.array([base_pos_x, base_pos_y, 0])
            
            vector_direction = np.array([-np.sin(angle), np.cos(angle), 0])
            vector_length = 0.8
            vector_end = vector_start + vector_length * vector_direction
            
            vector_arrow = Arrow(
                vector_start,
                vector_end,
                color=self.vector_color,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.25
            )
            vectors.add(vector_arrow)
            
            if i % 4 == 0:
                label = MathTex("X_H", font_size=18, color=self.vector_color)
                label.next_to(vector_end, direction=vector_direction, buff=0.15)
                vector_labels.add(label)
        
        def integral_curve_func(s):
            start_x, start_y = -1.5, -1.0
            end_x, end_y = 2.0, 1.5
            
            t = s
            x = start_x + (end_x - start_x) * t + 0.8 * np.sin(PI * t) * (1 - t)
            y = start_y + (end_y - start_y) * t + 0.6 * np.cos(PI * t) * t
            return np.array([x, y, 0])
        
        integral_curve = ParametricFunction(
            integral_curve_func,
            t_range=[0, 1, 0.01],
            color=self.curve_color,
            stroke_width=4
        )
        
        m_point = integral_curve_func(0.2)
        m_dot = Dot(m_point, radius=0.08, color=self.point_color)
        m_label = MathTex("m", font_size=28, color=self.point_color).next_to(m_dot, DOWN, buff=0.2)
        
        mt_point = integral_curve_func(0.7)
        mt_dot = Dot(mt_point, radius=0.08, color=self.point_color)
        mt_label = MathTex("m(t)", font_size=28, color=self.point_color).next_to(mt_dot, UP, buff=0.2)
        
        curve_label = Text("integral curve of ", font_size=20, color=self.curve_color)
        xh_part = MathTex("X_H", font_size=20, color=self.vector_color)
        curve_full_label = VGroup(curve_label, xh_part).arrange(RIGHT, buff=0.1)
        curve_full_label.to_edge(UP, buff=0.7)
        
        everything = VGroup(
            blob, vectors, vector_labels, integral_curve,
            m_dot, m_label, mt_dot, mt_label,
            curve_full_label
        )
        everything.scale(0.8)
        
        self.add(everything)

class HamiltonianVectorField(HamiltonianVectorFieldBase):
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class HamiltonianVectorFieldDark(HamiltonianVectorFieldBase):
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)


class CotangentBundleVisualizationBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"
            self.line_q_color = "#4a90e2"
            self.crossing_line_color = "#e74c3c"
            self.rectangle_color = "#2ecc71"
            self.fiber_color = "#f39c12"
            self.arrow_color = "#f39c12"
            self.label_color = WHITE
        else:
            self.camera.background_color = WHITE
            self.line_q_color = "#2980b9"
            self.crossing_line_color = "#c0392b"
            self.rectangle_color = "#27ae60"
            self.fiber_color = "#d35400"
            self.arrow_color = "#d35400"
            self.label_color = BLACK

    def construct(self):
        line_q_length = 4.0
        line_q = Line(
            [-line_q_length/2, 0, 0],
            [line_q_length/2, 0, 0],
            color=self.line_q_color,
            stroke_width=4
        )
        
        q_label = MathTex("Q", font_size=42, color=self.line_q_color).next_to(line_q, DOWN, buff=0.4)
        
        angle_deg = 35
        angle_rad = angle_deg * DEGREES
        crossing_line_length = 3.0
        
        direction = np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
        
        crossing_line = Line(
            -crossing_line_length/2 * direction,
            crossing_line_length/2 * direction,
            color=self.crossing_line_color,
            stroke_width=4
        )
        
        q1_label = MathTex("q^1", font_size=36, color=self.crossing_line_color).next_to(
            crossing_line.get_end(), UR, buff=0.2
        )
        
        left_side = VGroup(line_q, q_label, crossing_line, q1_label)
        left_side.shift(LEFT * 3.5)
        
        rect_width = 3.5
        rect_height = 2.5
        rectangle = Rectangle(
            width=rect_width,
            height=rect_height,
            color=self.rectangle_color,
            stroke_width=4,
            fill_color=self.rectangle_color,
            fill_opacity=0.15
        )
        
        tstar_q_label = MathTex("T^*Q", font_size=42, color=self.rectangle_color).next_to(rectangle, UP, buff=0.3)
        
        horizontal_line_length = rect_width * 0.7
        horizontal_line = Line(
            [-horizontal_line_length/2, 0, 0],
            [horizontal_line_length/2, 0, 0],
            color=self.fiber_color,
            stroke_width=3
        )
        horizontal_line.move_to(rectangle.get_center() + UP * 0.3)
        
        arrows = VGroup()
        num_arrows_x = 7
        num_arrows_y = 4
        arrow_length = 0.5
        
        flow_width = rect_width * 0.8
        flow_height = rect_height * 0.7
        
        for i in range(num_arrows_x):
            for j in range(num_arrows_y):
                x_pos = -flow_width/2 + i * flow_width / (num_arrows_x - 1)
                y_pos = -flow_height/2 + j * flow_height / (num_arrows_y - 1)
                
                arrow_start = np.array([x_pos, y_pos, 0])
                arrow_end = arrow_start + DOWN * arrow_length
                
                arrow = Arrow(
                    arrow_start,
                    arrow_end,
                    color=self.arrow_color,
                    stroke_width=2.5,
                    max_tip_length_to_length_ratio=0.2,
                    buff=0
                )
                arrows.add(arrow)
        
        arrows.move_to(rectangle.get_center())
        
        right_side = VGroup(rectangle, tstar_q_label, horizontal_line, arrows)
        right_side.shift(RIGHT * 3.5)
        
        everything = VGroup(left_side, right_side)
        everything.scale(0.9)
        
        self.add(everything)

class CotangentBundleVisualization(CotangentBundleVisualizationBase):
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class CotangentBundleVisualizationDark(CotangentBundleVisualizationBase):
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)


class DegreeOneFlowBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"
            self.axis_color = "#ecf0f1"
            self.arrow_color = "#4a90e2"
            self.label_color = WHITE
        else:
            self.camera.background_color = WHITE
            self.axis_color = "#2c3e50"
            self.arrow_color = "#2980b9"
            self.label_color = BLACK

    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=12,
            y_length=7,
            axis_config={
                "color": self.axis_color,
                "stroke_width": 3,
                "include_tip": True,
                "tip_width": 0.25,
                "tip_height": 0.25,
            },
        )
        
        x_label = MathTex("q", font_size=48, color=self.label_color).next_to(axes.x_axis.get_end(), RIGHT, buff=0.3)
        y_label = MathTex("p", font_size=48, color=self.label_color).next_to(axes.y_axis.get_end(), LEFT, buff=0.3)
        
        arrows = VGroup()
        num_arrows_x = 11
        num_arrows_y = 8
        arrow_length = 0.55
        
        x_range = [-3.7, 3.7]
        y_range = [-2.7, 2.7]
        
        for i in range(num_arrows_x):
            for j in range(num_arrows_y):
                x_pos = x_range[0] + i * (x_range[1] - x_range[0]) / (num_arrows_x - 1)
                y_pos = y_range[0] + j * (y_range[1] - y_range[0]) / (num_arrows_y - 1)
                
                arrow_start = axes.c2p(x_pos, y_pos)
                arrow_end = axes.c2p(x_pos + arrow_length, y_pos)
                
                arrow = Arrow(
                    arrow_start,
                    arrow_end,
                    color=self.arrow_color,
                    stroke_width=3,
                    max_tip_length_to_length_ratio=0.2,
                    buff=0
                )
                arrows.add(arrow)
        
        self.add(axes)
        self.add(x_label)
        self.add(y_label)
        self.add(arrows)

class DegreeOneFlow(DegreeOneFlowBase):
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class DegreeOneFlowDark(DegreeOneFlowBase):
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)


class CosphereBundleBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"
            self.curve_color = "#4a90e2"
            self.plane_color = "#2ecc71"
            self.level_set_color = "#f39c12"
            self.cosphere_color = "#f39c12"
            self.axis_color = "#ecf0f1"
            self.label_color = WHITE
        else:
            self.camera.background_color = WHITE
            self.curve_color = "#2980b9"
            self.plane_color = "#27ae60"
            self.level_set_color = "#d35400"
            self.cosphere_color = "#d35400"
            self.axis_color = "#2c3e50"
            self.label_color = BLACK

    def construct(self):
        def curve_q(t):
            x = 5 * t - 2.5
            y = 0.8 * np.sin(t * PI)
            return np.array([x, y, 0])
        
        curve = ParametricFunction(
            curve_q,
            t_range=[0, 1, 0.01],
            color=self.curve_color,
            stroke_width=5
        )
        
        FONT_SIZE = 36
        
        num_planes = 4
        tangent_planes = VGroup()
        level_sets_all = VGroup()
        cosphere_lines = VGroup()
        labels = VGroup()
        
        outermost_ellipses = []
        
        for i in range(num_planes):
            t_param = i * 1.0 / (num_planes - 1)
            point_on_curve = curve_q(t_param)
            
            dt = 0.01
            tangent_vec = (curve_q(t_param + dt) - curve_q(t_param - dt)) / (2 * dt)
            tangent_vec = tangent_vec / np.linalg.norm(tangent_vec[:2])
            
            normal_vec = np.array([-tangent_vec[1], tangent_vec[0], 0])
            
            plane_width = 2.8
            plane_height = 2.2
            
            plane = Rectangle(
                width=plane_width,
                height=plane_height,
                color=self.plane_color,
                stroke_width=3,
                fill_opacity=0.05,
                fill_color=self.plane_color
            )
            
            plane.move_to(point_on_curve)
            angle = np.arctan2(normal_vec[1], normal_vec[0])
            plane.rotate(angle)
            
            tangent_planes.add(plane)
            
            num_ellipses = 3
            ellipses_at_point = []
            
            for j in range(1, num_ellipses + 1):
                ellipse_width = plane_width * 0.55 * j / num_ellipses
                ellipse_height = plane_height * 0.55 * j / num_ellipses
                
                ellipse = Ellipse(
                    width=ellipse_width,
                    height=ellipse_height,
                    color=self.level_set_color,
                    stroke_width=3
                )
                
                ellipse.move_to(plane.get_center())
                ellipse.rotate(angle)
                
                level_sets_all.add(ellipse)
                ellipses_at_point.append(ellipse)
            
            if ellipses_at_point:
                outermost_ellipses.append(ellipses_at_point[-1])
        
        for i in range(len(outermost_ellipses) - 1):
            ellipse1 = outermost_ellipses[i]
            ellipse2 = outermost_ellipses[i + 1]
            
            for angle_frac in [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]:
                point1 = ellipse1.point_from_proportion(angle_frac)
                point2 = ellipse2.point_from_proportion(angle_frac)
                
                line = Line(point1, point2, color=self.cosphere_color, stroke_width=2, stroke_opacity=0.7)
                cosphere_lines.add(line)
        
        q_point = curve_q(0.5)
        q_label = MathTex("Q", font_size=FONT_SIZE, color=self.curve_color)
        q_label.move_to(q_point + DOWN * 1.8)
        q_arrow = Arrow(q_label.get_top(), q_point + DOWN * 0.1, color=self.curve_color, stroke_width=3, max_tip_length_to_length_ratio=0.15)
        labels.add(q_label, q_arrow)
        
        first_plane = tangent_planes[0]
        tq_label = MathTex("T^*Q", font_size=FONT_SIZE, color=self.plane_color)
        tq_label.move_to(first_plane.get_left() + LEFT * 2.0 + UP * 0.5)
        tq_arrow = Arrow(tq_label.get_right(), first_plane.get_left() + UP * 0.3, color=self.plane_color, stroke_width=3, max_tip_length_to_length_ratio=0.12)
        labels.add(tq_label, tq_arrow)
        
        last_ellipse = outermost_ellipses[-1]
        level_label = Text("level sets", font_size=FONT_SIZE, color=self.level_set_color)
        level_label.move_to(last_ellipse.get_right() + RIGHT * 2.2)
        level_arrow = Arrow(level_label.get_left(), last_ellipse.get_right(), color=self.level_set_color, stroke_width=3, max_tip_length_to_length_ratio=0.12)
        labels.add(level_label, level_arrow)
        
        middle_connection = cosphere_lines[len(cosphere_lines)//2].get_center()
        cosphere_label = Text("cosphere bundle", font_size=FONT_SIZE, color=self.cosphere_color)
        cosphere_label.to_edge(UP, buff=0.4)
        cosphere_arrow = Arrow(cosphere_label.get_bottom(), middle_connection + UP * 0.8, color=self.cosphere_color, stroke_width=3, max_tip_length_to_length_ratio=0.12)
        labels.add(cosphere_label, cosphere_arrow)
        
        axes_position = np.array([-5.5, -2.8, 0])
        
        axis_length = 1.4
        q_axis = Arrow(
            axes_position,
            axes_position + RIGHT * axis_length,
            color=self.axis_color,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
            buff=0
        )
        q_axis_label = MathTex("q^i", font_size=FONT_SIZE, color=self.label_color).next_to(q_axis.get_end(), RIGHT, buff=0.2)
        
        p_axis = Arrow(
            axes_position,
            axes_position + UP * axis_length,
            color=self.axis_color,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
            buff=0
        )
        p_axis_label = MathTex("p_i", font_size=FONT_SIZE, color=self.label_color).next_to(p_axis.get_end(), UP, buff=0.2)
        
        self.add(cosphere_lines)
        self.add(curve)
        self.add(tangent_planes)
        self.add(level_sets_all)
        self.add(q_axis, q_axis_label)
        self.add(p_axis, p_axis_label)
        self.add(labels)

class CosphereBundle(CosphereBundleBase):
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class CosphereBundleDark(CosphereBundleBase):
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)


class EnergyLevelCircleBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"
            self.axis_color = "#ecf0f1"
            self.top_circle_color = "#4a90e2"
            self.bottom_circle_color = "#e74c3c"
            self.intersection_color = "#f39c12"
            self.label_color = WHITE
        else:
            self.camera.background_color = WHITE
            self.axis_color = "#2c3e50"
            self.top_circle_color = "#2980b9"
            self.bottom_circle_color = "#c0392b"
            self.intersection_color = "#d35400"
            self.label_color = BLACK

    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3.5, 3.5, 1],
            x_length=10,
            y_length=7,
            axis_config={
                "color": self.axis_color,
                "stroke_width": 3,
                "include_tip": True,
                "tip_width": 0.25,
                "tip_height": 0.25,
            },
        )
        
        x_label = MathTex("x", font_size=48, color=self.label_color).next_to(axes.x_axis.get_end(), RIGHT, buff=0.3)
        p_label = MathTex("p", font_size=48, color=self.label_color).next_to(axes.y_axis.get_end(), LEFT, buff=0.2)
        
        circle_radius = 2.5
        
        origin_point = axes.c2p(0, 0)
        right_point = axes.c2p(circle_radius, 0)
        screen_radius = np.linalg.norm(right_point - origin_point)
        
        top_semicircle = Arc(
            radius=screen_radius,
            start_angle=0,
            angle=PI,
            color=self.top_circle_color,
            fill_color=self.top_circle_color,
            fill_opacity=0.5,
            stroke_width=4
        )
        top_semicircle.move_arc_center_to(origin_point)
        
        bottom_semicircle = Arc(
            radius=screen_radius,
            start_angle=PI,
            angle=PI,
            color=self.bottom_circle_color,
            fill_color=self.bottom_circle_color,
            fill_opacity=0.5,
            stroke_width=4
        )
        bottom_semicircle.move_arc_center_to(origin_point)
        
        right_intersection = Dot(axes.c2p(circle_radius, 0), radius=0.10, color=self.intersection_color)
        left_intersection = Dot(axes.c2p(-circle_radius, 0), radius=0.10, color=self.intersection_color)
        
        right_label = MathTex(r"\sqrt{2E}", font_size=36, color=self.intersection_color).next_to(right_intersection, DR, buff=0.3)
        left_label = MathTex(r"-\sqrt{2E}", font_size=36, color=self.intersection_color).next_to(left_intersection, DL, buff=0.3)
        
        self.add(axes)
        self.add(x_label)
        self.add(p_label)
        self.add(top_semicircle)
        self.add(bottom_semicircle)
        self.add(right_intersection)
        self.add(left_intersection)
        self.add(right_label)
        self.add(left_label)

class EnergyLevelCircle(EnergyLevelCircleBase):
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class EnergyLevelCircleDark(EnergyLevelCircleBase):
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)


class GeodesicComparisonBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"
            self.axis_color = "#ecf0f1"
            self.geodesic_color = "#e74c3c"
            self.magnetic_line_color = "#4a90e2"
            self.magnetic_curve_color = "#e74c3c"
            self.label_color = WHITE
        else:
            self.camera.background_color = WHITE
            self.axis_color = "#2c3e50"
            self.geodesic_color = "#c0392b"
            self.magnetic_line_color = "#2980b9"
            self.magnetic_curve_color = "#c0392b"
            self.label_color = BLACK

    def construct(self):
        # Left side - Geodesics
        left_axes = Axes(
            x_range=[-2, 3.5, 1],
            y_range=[-2, 3.5, 1],
            x_length=4.5,
            y_length=4.5,
            axis_config={
                "color": self.axis_color,
                "stroke_width": 2,
                "include_tip": True,
                "tip_width": 0.2,
                "tip_height": 0.2,
            },
        )
        
        x_label_left = MathTex("x", font_size=36, color=self.label_color).next_to(left_axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label_left = MathTex("y", font_size=36, color=self.label_color).next_to(left_axes.y_axis.get_end(), UP, buff=0.2)
        
        # Create several parallel 45-degree arrows (geodesics) with different y-intercepts
        geodesic_arrows = VGroup()
        num_arrows = 5
        for i in range(num_arrows):
            # Different y-intercept for each arrow: y = x + c
            y_intercept = -2.0 + i * 1.0  # -2, -1, 0, 1, 2
            
            # Start and end x positions
            x_start = -1.5
            x_end = 2.5
            
            # Calculate y positions: y = x + y_intercept
            y_start = x_start + y_intercept
            y_end = x_end + y_intercept
            
            arrow_start = left_axes.c2p(x_start, y_start)
            arrow_end = left_axes.c2p(x_end, y_end)
            
            arrow = Arrow(
                arrow_start,
                arrow_end,
                color=self.geodesic_color,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15,
                buff=0
            )
            geodesic_arrows.add(arrow)
        
        geodesics_label = Text("geodesics", font_size=32, color=self.label_color)
        
        left_group = VGroup(left_axes, x_label_left, y_label_left, geodesic_arrows, geodesics_label)
        geodesics_label.next_to(left_axes, UP, buff=0.6)
        left_group.shift(LEFT * 3.5)
        
        # Right side - Magnetic Geodesics
        right_axes = Axes(
            x_range=[-2, 3.5, 1],
            y_range=[-2, 3.5, 1],
            x_length=4.5,
            y_length=4.5,
            axis_config={
                "color": self.axis_color,
                "stroke_width": 2,
                "include_tip": True,
                "tip_width": 0.2,
                "tip_height": 0.2,
            },
        )
        
        x_label_right = MathTex("x", font_size=36, color=self.label_color).next_to(right_axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label_right = MathTex("y", font_size=36, color=self.label_color).next_to(right_axes.y_axis.get_end(), UP, buff=0.2)
        
        # Blue dashed line going to top right
        dashed_line_start = right_axes.c2p(0.5, 0.5)
        dashed_line_end = right_axes.c2p(2.8, 2.8)
        dashed_line = DashedLine(
            dashed_line_start,
            dashed_line_end,
            color=self.magnetic_line_color,
            stroke_width=3,
            dash_length=0.15
        )
        
        # Red curve winding around the dashed line
        def magnetic_curve(t):
            # Base line: y = x (45 degrees)
            base_x = 0.5 + t * 2.3
            base_y = 0.5 + t * 2.3
            
            # Add helical winding
            radius = 0.25
            frequency = 8
            offset_x = radius * np.cos(frequency * 2 * PI * t)
            offset_y = radius * np.sin(frequency * 2 * PI * t)
            
            # Rotate the offset to be perpendicular to the 45-degree line
            rotated_offset_x = (offset_x - offset_y) / np.sqrt(2)
            rotated_offset_y = (offset_x + offset_y) / np.sqrt(2)
            
            point = right_axes.c2p(
                base_x + rotated_offset_x,
                base_y + rotated_offset_y
            )
            return point
        
        magnetic_geodesic = ParametricFunction(
            magnetic_curve,
            t_range=[0, 1, 0.005],
            color=self.magnetic_curve_color,
            stroke_width=3
        )
        
        magnetic_label = Text("magnetic geodesics", font_size=32, color=self.label_color)
        
        right_group = VGroup(right_axes, x_label_right, y_label_right, dashed_line, magnetic_geodesic, magnetic_label)
        magnetic_label.next_to(right_axes, UP, buff=0.6)
        right_group.shift(RIGHT * 3.5)
        
        # Add everything
        self.add(left_group)
        self.add(right_group)

class GeodesicComparison(GeodesicComparisonBase):
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class GeodesicComparisonDark(GeodesicComparisonBase):
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)


class LightConeBase(ThreeDScene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"
            self.cone_color = "#4a90e2"
            self.spacelike_color = "#e74c3c"
            self.timelike_color = "#2ecc71"
            self.lightlike_color = "#f39c12"
            self.label_color = WHITE
        else:
            self.camera.background_color = WHITE
            self.cone_color = "#2980b9"
            self.spacelike_color = "#c0392b"
            self.timelike_color = "#27ae60"
            self.lightlike_color = "#d35400"
            self.label_color = BLACK

    def construct(self):
        # Set camera orientation
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        
        # Create the double cone (light cone)
        def cone_surface(u, v):
            t = v
            r = abs(t)
            x = r * np.cos(u)
            y = r * np.sin(u)
            z = t
            return np.array([x, y, z])
        
        # Upper cone
        upper_cone = Surface(
            lambda u, v: cone_surface(u, v),
            u_range=[0, 2*PI],
            v_range=[0, 2.5],
            resolution=(24, 12),
            fill_opacity=0.3,
            stroke_width=1,
            stroke_color=self.cone_color,
            fill_color=self.cone_color
        )
        
        # Lower cone
        lower_cone = Surface(
            lambda u, v: cone_surface(u, -v),
            u_range=[0, 2*PI],
            v_range=[0, 2.5],
            resolution=(24, 12),
            fill_opacity=0.3,
            stroke_width=1,
            stroke_color=self.cone_color,
            fill_color=self.cone_color
        )
        
        # Create arrows from origin
        arrow_length = 2.0
        
        # Space-like arrow (pointing in x direction)
        spacelike_arrow = Arrow3D(
            start=ORIGIN,
            end=[arrow_length, 0, 0],
            color=self.spacelike_color,
            thickness=0.02,
            height=0.15,
            base_radius=0.04
        )
        
        # Time-like arrow (pointing in z direction, up)
        timelike_arrow = Arrow3D(
            start=ORIGIN,
            end=[0, 0, arrow_length],
            color=self.timelike_color,
            thickness=0.02,
            height=0.15,
            base_radius=0.04
        )
        
        # Light-like arrow (pointing along the cone edge at 45 degrees)
        # The cone edge is at r = |t|, so for positive t: x = t*cos(θ), y = t*sin(θ), z = t
        # We'll use θ = π/4 for a nice visible angle
        light_angle = PI/4
        light_direction = np.array([
            arrow_length * np.cos(light_angle) / np.sqrt(2),
            arrow_length * np.sin(light_angle) / np.sqrt(2),
            arrow_length / np.sqrt(2)
        ])
        
        lightlike_arrow = Arrow3D(
            start=ORIGIN,
            end=light_direction,
            color=self.lightlike_color,
            thickness=0.02,
            height=0.15,
            base_radius=0.04
        )
        
        # Create labels (they need to be added as 2D overlays)
        spacelike_label = Text("space-like", font_size=24, color=self.spacelike_color)
        spacelike_label.to_corner(UR, buff=0.5).shift(DOWN * 0)
        
        timelike_label = Text("time-like", font_size=24, color=self.timelike_color)
        timelike_label.to_corner(UR, buff=0.5).shift(DOWN * 0.8)
        
        lightlike_label = Text("light-like", font_size=24, color=self.lightlike_color)
        lightlike_label.to_corner(UR, buff=0.5).shift(DOWN * 1.6)
        
        # Add everything to the scene
        self.add(lower_cone)
        self.add(upper_cone)
        self.add(spacelike_arrow)
        self.add(timelike_arrow)
        self.add(lightlike_arrow)
        self.add_fixed_in_frame_mobjects(spacelike_label, timelike_label, lightlike_label)

class LightCone(LightConeBase):
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class LightConeDark(LightConeBase):
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)
