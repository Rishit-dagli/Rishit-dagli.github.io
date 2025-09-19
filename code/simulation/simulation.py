from manim import *
import numpy as np

class SpringMassSystemBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"  # Dark background
            self.spring_color = "#4a90e2"  # Blue spring
            self.mass_color = "#e74c3c"    # Red mass
            self.label_color = "#f39c12"   # Orange labels
            self.origin_color = "#ecf0f1"  # Light gray origin
            self.mass_label_color = WHITE
        else:  # light theme
            self.camera.background_color = WHITE  # Light background
            self.spring_color = "#2980b9"  # Darker blue spring
            self.mass_color = "#c0392b"    # Darker red mass
            self.label_color = "#d35400"   # Darker orange labels
            self.origin_color = "#2c3e50"  # Dark gray origin
            self.mass_label_color = WHITE

    def construct(self):
        # Create the spring using parametric function
        spring_length = 5  # Length of the spring (reduced for better centering)
        num_coils = 12     # Number of coils for visibility
        amplitude = 0.5    # Amplitude of the oscillations
        
        # Define spring position offset to center the system
        spring_offset = -spring_length / 2
        
        def spring_func(t):
            # t goes from 0 to 1
            x = spring_offset + t * spring_length  # horizontal stretch with centering
            y = amplitude * np.sin(num_coils * 2 * PI * t)  # vertical oscillation
            return np.array([x, y, 0])
        
        spring = ParametricFunction(
            spring_func,
            t_range=[0, 1, 0.005],  # More points for smoother curve
            stroke_width=4,         # Thick stroke for visibility
            color=self.spring_color
        )
        
        # Create mass as a rectangle at the end of the spring
        mass = Rectangle(
            width=1.2,
            height=1.2,
            fill_color=self.mass_color,
            fill_opacity=0.8,
            stroke_color=self.mass_label_color,
            stroke_width=3
        ).move_to([spring_offset + spring_length, 0, 0])
        
        # Add label 'm' for mass using LaTeX
        mass_label = MathTex("m", font_size=48, color=self.mass_label_color).move_to(mass.get_center())
        
        # Create origin point (fixed end of spring)
        origin = Dot([spring_offset, 0, 0], radius=0.15, color=self.origin_color)
        
        # Define consistent label height below the elements
        label_height = -1.0
        
        # Add label 'x=0' at the origin using LaTeX, positioned at consistent height
        origin_label = MathTex("x=0", font_size=40, color=self.label_color).move_to([spring_offset, label_height, 0])
        
        # Add label 'x(t)' under the mass using LaTeX, positioned at consistent height
        position_label = MathTex("x(t)", font_size=40, color=self.label_color).move_to([spring_offset + spring_length, label_height, 0])
        
        # Create a group with all elements and scale it
        system_group = VGroup(spring, mass, mass_label, origin, origin_label, position_label)
        system_group.scale(2)  # Scale everything by 2
        
        # Add the scaled group to the scene
        self.add(system_group)

class SpringMassSystem(SpringMassSystemBase):
    """Light theme version (default)"""
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class SpringMassSystemDark(SpringMassSystemBase):
    """Dark theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)

class PhaseSpaceBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"  # Dark background
            self.axis_color = "#ecf0f1"  # Light gray axes
            self.trajectory_color = "#4a90e2"  # Blue trajectories
            self.arrow_color = "#e74c3c"  # Red arrows
            self.label_color = WHITE
        else:  # light theme
            self.camera.background_color = WHITE  # Light background
            self.axis_color = "#2c3e50"  # Dark gray axes
            self.trajectory_color = "#2980b9"  # Darker blue trajectories
            self.arrow_color = "#c0392b"  # Darker red arrows
            self.label_color = BLACK

    def construct(self):
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3, 0.5],
            y_range=[-3, 3, 0.5],
            x_length=10,
            y_length=10,
            axis_config={"color": self.axis_color, "stroke_width": 2},
            tips=True,
        )
        
        # Add axis labels with professional formatting
        x_label = MathTex("q", font_size=56, color=self.label_color).next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
        y_label = MathTex(r"\dot{q}", font_size=56, color=self.label_color).next_to(axes.y_axis.get_end(), LEFT, buff=0.2)
        
        # Create phase space trajectories (circles for different energy levels)
        trajectories = VGroup()
        
        # Different energy levels create circles of different radii
        radii = [0.6, 1.2, 1.8, 2.4]
        
        for i, radius in enumerate(radii):
            # Parametric circle in phase space
            def circle_func(t, r=radius):
                q = r * np.cos(t)  # position
                v = r * np.sin(t)  # velocity
                return axes.coords_to_point(q, v)
            
            # Make outer circles slightly thicker and more prominent
            stroke_width = 2.5 if i < 2 else 2.0
            alpha = 0.8 if i < 2 else 0.6
            
            circle = ParametricFunction(
                circle_func,
                t_range=[0, 2*PI, 0.01],
                stroke_width=stroke_width,
                color=self.trajectory_color,
                stroke_opacity=alpha
            )
            trajectories.add(circle)
        
        # Create a dense vector field
        vector_field = VGroup()
        
        # Grid of points for vector field
        for q_val in np.arange(-2.5, 2.6, 0.4):
            for v_val in np.arange(-2.5, 2.6, 0.4):
                # Skip points too close to origin to avoid clutter
                if np.sqrt(q_val**2 + v_val**2) < 0.3:
                    continue
                
                # Vector field for mass-spring: dq/dt = v, dv/dt = -k/m * q
                # Direction vector is (v, -k/m * q)
                direction_q = v_val
                direction_v = -q_val  # assuming k/m = 1
                
                # Normalize and scale
                magnitude = np.sqrt(direction_q**2 + direction_v**2)
                if magnitude > 0:
                    direction_q /= magnitude
                    direction_v /= magnitude
                
                # Scale for visibility - smaller arrows for cleaner look
                scale = 0.15
                start_point = axes.coords_to_point(q_val, v_val)
                end_point = axes.coords_to_point(
                    q_val + scale * direction_q,
                    v_val + scale * direction_v
                )
                
                # Create arrow with appropriate opacity
                arrow = Arrow(
                    start_point,
                    end_point,
                    color=self.arrow_color,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.4,
                    stroke_opacity=0.7
                )
                vector_field.add(arrow)
        
        # Add a few key trajectory arrows on the circles for clarity
        key_arrows = VGroup()
        key_positions = [PI/4, 3*PI/4, 5*PI/4, 7*PI/4]
        
        for angle in key_positions:
            # Use middle radius circle
            radius = radii[1]
            q = radius * np.cos(angle)
            v = radius * np.sin(angle)
            
            # Direction tangent to circle
            direction_q = v
            direction_v = -q
            
            # Normalize
            magnitude = np.sqrt(direction_q**2 + direction_v**2)
            if magnitude > 0:
                direction_q /= magnitude
                direction_v /= magnitude
            
            scale = 0.25
            start_point = axes.coords_to_point(q, v)
            end_point = axes.coords_to_point(
                q + scale * direction_q,
                v + scale * direction_v
            )
            
            arrow = Arrow(
                start_point,
                end_point,
                color=self.trajectory_color,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.3
            )
            key_arrows.add(arrow)
        
        # Add center point (equilibrium)
        equilibrium = Dot(
            axes.coords_to_point(0, 0),
            radius=0.06,
            color=self.arrow_color
        )
        
        # Group everything
        phase_portrait = VGroup(
            axes, x_label, y_label, vector_field, trajectories, key_arrows, equilibrium
        )
        
        self.add(phase_portrait)

class PhaseSpace(PhaseSpaceBase):
    """Light theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class PhaseSpaceDark(PhaseSpaceBase):
    """Dark theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)

class EulerInstabilityBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"  # Dark background
            self.axis_color = "#ecf0f1"  # Light gray axes
            self.true_solution_color = "#2ecc71"  # Green for true solution
            self.euler_color = "#e74c3c"  # Red for unstable Euler
            self.label_color = WHITE
        else:  # light theme
            self.camera.background_color = WHITE  # Light background
            self.axis_color = "#2c3e50"  # Dark gray axes
            self.true_solution_color = "#27ae60"  # Darker green for true solution
            self.euler_color = "#c0392b"  # Darker red for unstable Euler
            self.label_color = BLACK

    def construct(self):
        # Create coordinate system
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=9,
            y_length=9,
            axis_config={"color": self.axis_color, "stroke_width": 2},
            tips=True,
        )
        
        # Add axis labels
        x_label = MathTex("q", font_size=48, color=self.label_color).next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
        y_label = MathTex(r"\dot{q}", font_size=48, color=self.label_color).next_to(axes.y_axis.get_end(), LEFT, buff=0.2)
        
        # Simulation parameters
        dt = 0.3  # Larger time step to show instability clearly
        k_over_m = 1.0  # k/m ratio
        total_time = 6.0
        steps = int(total_time / dt)
        
        # Initial conditions
        q0, v0 = 2.0, 0.0  # Start at maximum displacement
        
        # True solution (analytical circle)
        def true_solution_func(t):
            omega = np.sqrt(k_over_m)
            q = q0 * np.cos(omega * t)
            v = -q0 * omega * np.sin(omega * t)
            return axes.coords_to_point(q, v)
        
        true_trajectory = ParametricFunction(
            true_solution_func,
            t_range=[0, total_time, 0.01],
            stroke_width=4,
            color=self.true_solution_color
        )
        
        # Forward Euler simulation
        euler_points = []
        q_euler, v_euler = q0, v0
        
        for i in range(steps + 1):
            euler_points.append(axes.coords_to_point(q_euler, v_euler))
            
            # Forward Euler update
            v_new = v_euler - dt * k_over_m * q_euler
            q_new = q_euler + dt * v_euler
            
            q_euler, v_euler = q_new, v_new
        
        # Create Euler trajectory as a path through points
        euler_trajectory = VMobject(stroke_width=4, color=self.euler_color)
        euler_trajectory.set_points_as_corners(euler_points)
        
        # Add starting point marker
        start_point = Dot(
            axes.coords_to_point(q0, v0),
            radius=0.08,
            color=self.axis_color
        )
        
        # Add legend
        legend_true = VGroup(
            Line(ORIGIN, RIGHT * 0.5, color=self.true_solution_color, stroke_width=4),
            MathTex(r"\text{True solution}", font_size=32, color=self.label_color)
        ).arrange(RIGHT, buff=0.2)
        
        legend_euler = VGroup(
            Line(ORIGIN, RIGHT * 0.5, color=self.euler_color, stroke_width=4),
            MathTex(r"\text{Forward Euler}", font_size=32, color=self.label_color)
        ).arrange(RIGHT, buff=0.2)
        
        legend = VGroup(legend_true, legend_euler).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        legend.to_corner(UR, buff=0.5)
        
        # Add some reference circles to show energy levels
        reference_circles = VGroup()
        for radius in [1.0, 2.0, 3.0]:
            circle = Circle(
                radius=radius * axes.x_axis.unit_size,
                color=self.axis_color,
                stroke_width=1,
                stroke_opacity=0.3
            ).move_to(axes.coords_to_point(0, 0))
            reference_circles.add(circle)
        
        # Group everything
        instability_plot = VGroup(
            reference_circles, axes, x_label, y_label, 
            true_trajectory, euler_trajectory, start_point, legend
        )
        
        self.add(instability_plot)

class EulerInstability(EulerInstabilityBase):
    """Light theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class EulerInstabilityDark(EulerInstabilityBase):
    """Dark theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)

class BackwardEulerBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"  # Dark background
            self.axis_color = "#ecf0f1"  # Light gray axes
            self.true_solution_color = "#2ecc71"  # Green for true solution
            self.backward_euler_color = "#3498db"  # Blue for damped Backward Euler
            self.label_color = WHITE
        else:  # light theme
            self.camera.background_color = WHITE  # Light background
            self.axis_color = "#2c3e50"  # Dark gray axes
            self.true_solution_color = "#27ae60"  # Darker green for true solution
            self.backward_euler_color = "#2980b9"  # Darker blue for damped Backward Euler
            self.label_color = BLACK

    def construct(self):
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=9,
            y_length=9,
            axis_config={"color": self.axis_color, "stroke_width": 2},
            tips=True,
        )
        
        # Add axis labels
        x_label = MathTex("q", font_size=48, color=self.label_color).next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
        y_label = MathTex(r"\dot{q}", font_size=48, color=self.label_color).next_to(axes.y_axis.get_end(), LEFT, buff=0.2)
        
        # Simulation parameters
        dt = 0.25  # Time step
        k_over_m = 1.0  # k/m ratio
        total_time = 8.0
        steps = int(total_time / dt)
        
        # Initial conditions
        q0, v0 = 2.0, 0.0  # Start at maximum displacement
        
        # True solution (analytical circle)
        def true_solution_func(t):
            omega = np.sqrt(k_over_m)
            q = q0 * np.cos(omega * t)
            v = -q0 * omega * np.sin(omega * t)
            return axes.coords_to_point(q, v)
        
        true_trajectory = ParametricFunction(
            true_solution_func,
            t_range=[0, total_time, 0.01],
            stroke_width=4,
            color=self.true_solution_color
        )
        
        # Backward Euler simulation
        backward_euler_points = []
        q_be, v_be = q0, v0
        
        for i in range(steps + 1):
            backward_euler_points.append(axes.coords_to_point(q_be, v_be))
            
            # Backward Euler update: solve (I - dt^2 K) v^{t+1} = M v^t + dt f(q^t)
            # For our system: v^{t+1} + dt^2 * (k/m) * q^{t+1} = v^t
            #                 q^{t+1} - dt * v^{t+1} = q^t
            # This gives us: (1 + dt^2 * k/m) * v^{t+1} = v^t - dt * (k/m) * q^t
            #                q^{t+1} = q^t + dt * v^{t+1}
            
            denominator = 1 + dt**2 * k_over_m
            v_new = (v_be - dt * k_over_m * q_be) / denominator
            q_new = q_be + dt * v_new
            
            q_be, v_be = q_new, v_new
        
        # Create Backward Euler trajectory as a path through points
        backward_euler_trajectory = VMobject(stroke_width=4, color=self.backward_euler_color)
        backward_euler_trajectory.set_points_as_corners(backward_euler_points)
        
        # Add starting point marker
        start_point = Dot(
            axes.coords_to_point(q0, v0),
            radius=0.08,
            color=self.axis_color
        )
        
        # Add equilibrium point marker
        equilibrium_point = Dot(
            axes.coords_to_point(0, 0),
            radius=0.06,
            color=self.backward_euler_color
        )
        
        # Add legend
        legend_true = VGroup(
            Line(ORIGIN, RIGHT * 0.5, color=self.true_solution_color, stroke_width=4),
            MathTex(r"\text{True solution}", font_size=32, color=self.label_color)
        ).arrange(RIGHT, buff=0.2)
        
        legend_backward_euler = VGroup(
            Line(ORIGIN, RIGHT * 0.5, color=self.backward_euler_color, stroke_width=4),
            MathTex(r"\text{Backward Euler}", font_size=32, color=self.label_color)
        ).arrange(RIGHT, buff=0.2)
        
        legend = VGroup(legend_true, legend_backward_euler).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        legend.to_corner(UR, buff=0.5)
        
        # Add some reference circles to show energy levels
        reference_circles = VGroup()
        for radius in [0.5, 1.0, 1.5, 2.0]:
            circle = Circle(
                radius=radius * axes.x_axis.unit_size,
                color=self.axis_color,
                stroke_width=1,
                stroke_opacity=0.3
            ).move_to(axes.coords_to_point(0, 0))
            reference_circles.add(circle)
        
        # Group everything
        damping_plot = VGroup(
            reference_circles, axes, x_label, y_label, 
            true_trajectory, backward_euler_trajectory, start_point, equilibrium_point, legend
        )
        
        self.add(damping_plot)

class BackwardEuler(BackwardEulerBase):
    """Light theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class BackwardEulerDark(BackwardEulerBase):
    """Dark theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)

class SymplecticEulerBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"  # Dark background
            self.axis_color = "#ecf0f1"  # Light gray axes
            self.true_solution_color = "#2ecc71"  # Green for true solution
            self.symplectic_color = "#9b59b6"  # Purple for symplectic Euler
            self.label_color = WHITE
        else:  # light theme
            self.camera.background_color = WHITE  # Light background
            self.axis_color = "#2c3e50"  # Dark gray axes
            self.true_solution_color = "#27ae60"  # Darker green for true solution
            self.symplectic_color = "#8e44ad"  # Darker purple for symplectic Euler
            self.label_color = BLACK

    def construct(self):
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=9,
            y_length=9,
            axis_config={"color": self.axis_color, "stroke_width": 2},
            tips=True,
        )
        
        # Add axis labels
        x_label = MathTex("q", font_size=48, color=self.label_color).next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
        y_label = MathTex(r"\dot{q}", font_size=48, color=self.label_color).next_to(axes.y_axis.get_end(), LEFT, buff=0.2)
        
        # Simulation parameters
        dt = 0.2  # Time step
        k_over_m = 1.0  # k/m ratio
        total_time = 12.0  # Longer time to show stability
        steps = int(total_time / dt)
        
        # Initial conditions
        q0, v0 = 2.0, 0.0  # Start at maximum displacement
        
        # True solution (analytical circle)
        def true_solution_func(t):
            omega = np.sqrt(k_over_m)
            q = q0 * np.cos(omega * t)
            v = -q0 * omega * np.sin(omega * t)
            return axes.coords_to_point(q, v)
        
        true_trajectory = ParametricFunction(
            true_solution_func,
            t_range=[0, total_time, 0.01],
            stroke_width=4,
            color=self.true_solution_color
        )
        
        # Symplectic Euler simulation
        symplectic_points = []
        q_se, v_se = q0, v0
        
        for i in range(steps + 1):
            symplectic_points.append(axes.coords_to_point(q_se, v_se))
            
            # Symplectic Euler update:
            # 1. First take an explicit velocity step
            v_new = v_se - dt * k_over_m * q_se
            # 2. Next take an implicit position step using the NEW velocity
            q_new = q_se + dt * v_new
            
            q_se, v_se = q_new, v_new
        
        # Create Symplectic Euler trajectory as a path through points
        symplectic_trajectory = VMobject(stroke_width=4, color=self.symplectic_color)
        symplectic_trajectory.set_points_as_corners(symplectic_points)
        
        # Add starting point marker
        start_point = Dot(
            axes.coords_to_point(q0, v0),
            radius=0.08,
            color=self.axis_color
        )
        
        # Add legend
        legend_true = VGroup(
            Line(ORIGIN, RIGHT * 0.5, color=self.true_solution_color, stroke_width=4),
            MathTex(r"\text{True solution}", font_size=32, color=self.label_color)
        ).arrange(RIGHT, buff=0.2)
        
        legend_symplectic = VGroup(
            Line(ORIGIN, RIGHT * 0.5, color=self.symplectic_color, stroke_width=4),
            MathTex(r"\text{Symplectic Euler}", font_size=32, color=self.label_color)
        ).arrange(RIGHT, buff=0.2)
        
        legend = VGroup(legend_true, legend_symplectic).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        legend.to_corner(UR, buff=0.5)
        
        # Add some reference circles to show energy levels
        reference_circles = VGroup()
        for radius in [0.5, 1.0, 1.5, 2.0, 2.5]:
            circle = Circle(
                radius=radius * axes.x_axis.unit_size,
                color=self.axis_color,
                stroke_width=1,
                stroke_opacity=0.3
            ).move_to(axes.coords_to_point(0, 0))
            reference_circles.add(circle)
        
        # Add equilibrium point
        equilibrium_point = Dot(
            axes.coords_to_point(0, 0),
            radius=0.06,
            color=self.axis_color
        )
        
        # Group everything
        symplectic_plot = VGroup(
            reference_circles, axes, x_label, y_label, 
            true_trajectory, symplectic_trajectory, start_point, equilibrium_point, legend
        )
        
        self.add(symplectic_plot)

class SymplecticEuler(SymplecticEulerBase):
    """Light theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class SymplecticEulerDark(SymplecticEulerBase):
    """Dark theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)

class MatrixAssemblyBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"  # Dark background
            self.node_color = "#ecf0f1"  # Light gray nodes
            self.spring_color = "#4a90e2"  # Blue springs
            self.highlight_spring_color = "#e74c3c"  # Red for highlighted spring
            self.matrix_color = "#2c3e50"  # Dark matrix elements
            self.highlight_color = "#e74c3c"  # Red highlights
            self.label_color = WHITE
        else:  # light theme
            self.camera.background_color = WHITE  # Light background
            self.node_color = "#2c3e50"  # Dark gray nodes
            self.spring_color = "#2980b9"  # Darker blue springs
            self.highlight_spring_color = "#c0392b"  # Darker red for highlighted spring
            self.matrix_color = "#34495e"  # Dark matrix elements
            self.highlight_color = "#c0392b"  # Darker red highlights
            self.label_color = BLACK

    def construct(self):
        # Create a simple 3x2 mesh for visualization
        mesh_width = 3
        mesh_height = 2
        node_spacing = 1.2
        
        # Position the mesh on the left side
        mesh_center = LEFT * 4
        
        # Create nodes
        nodes = VGroup()
        node_positions = {}
        
        for j in range(mesh_height):
            for i in range(mesh_width):
                node_idx = j * mesh_width + i
                pos = mesh_center + RIGHT * (i * node_spacing) + UP * (j * node_spacing - 0.5)
                node = Circle(
                    radius=0.15,
                    fill_color=self.node_color,
                    fill_opacity=0.8,
                    stroke_color=self.node_color,
                    stroke_width=2
                ).move_to(pos)
                
                # Add node index label
                label = MathTex(str(node_idx), font_size=24, color=self.label_color).move_to(pos)
                
                nodes.add(VGroup(node, label))
                node_positions[node_idx] = pos
        
        # Create springs (edges)
        springs = VGroup()
        spring_data = []  # Store spring connectivity
        
        # Horizontal springs
        for j in range(mesh_height):
            for i in range(mesh_width - 1):
                node1 = j * mesh_width + i
                node2 = j * mesh_width + (i + 1)
                
                spring = Line(
                    node_positions[node1],
                    node_positions[node2],
                    stroke_width=3,
                    color=self.spring_color
                )
                springs.add(spring)
                spring_data.append((node1, node2))
        
        # Vertical springs
        for j in range(mesh_height - 1):
            for i in range(mesh_width):
                node1 = j * mesh_width + i
                node2 = (j + 1) * mesh_width + i
                
                spring = Line(
                    node_positions[node1],
                    node_positions[node2],
                    stroke_width=3,
                    color=self.spring_color
                )
                springs.add(spring)
                spring_data.append((node1, node2))
        
        # Highlight one specific spring for demonstration
        highlight_spring_idx = 2  # Choose a horizontal spring
        highlighted_spring = springs[highlight_spring_idx].copy()
        highlighted_spring.set_color(self.highlight_spring_color)
        highlighted_spring.set_stroke_width(5)
        
        # Create matrix visualization on the right side
        matrix_center = RIGHT * 3.5
        total_dofs = mesh_width * mesh_height  # Each node has 1 DOF for simplicity
        
        # Create global stiffness matrix representation
        matrix_size = 2.5
        cell_size = matrix_size / total_dofs
        
        # Matrix background
        matrix_bg = Rectangle(
            width=matrix_size,
            height=matrix_size,
            stroke_color=self.matrix_color,
            stroke_width=2,
            fill_opacity=0
        ).move_to(matrix_center)
        
        # Create matrix grid
        matrix_grid = VGroup()
        for i in range(total_dofs + 1):
            # Vertical lines
            line = Line(
                matrix_center + LEFT * matrix_size/2 + RIGHT * i * cell_size,
                matrix_center + LEFT * matrix_size/2 + RIGHT * i * cell_size + UP * matrix_size,
                stroke_width=0.5,
                color=self.matrix_color
            )
            matrix_grid.add(line)
            
            # Horizontal lines
            line = Line(
                matrix_center + DOWN * matrix_size/2 + UP * i * cell_size,
                matrix_center + DOWN * matrix_size/2 + UP * i * cell_size + RIGHT * matrix_size,
                stroke_width=0.5,
                color=self.matrix_color
            )
            matrix_grid.add(line)
        
        # Highlight the contribution from the selected spring
        spring_nodes = spring_data[highlight_spring_idx]
        node1, node2 = spring_nodes
        
        # Create highlighted matrix entries for this spring's contribution
        highlighted_entries = VGroup()
        
        # The spring connects nodes node1 and node2, so it contributes to:
        # K[node1,node1], K[node1,node2], K[node2,node1], K[node2,node2]
        positions = [(node1, node1), (node1, node2), (node2, node1), (node2, node2)]
        
        for i, j in positions:
            # Calculate position in matrix
            entry_pos = (
                matrix_center 
                + LEFT * matrix_size/2 
                + RIGHT * (j + 0.5) * cell_size
                + UP * matrix_size/2
                - UP * (i + 0.5) * cell_size
            )
            
            entry = Rectangle(
                width=cell_size * 0.9,
                height=cell_size * 0.9,
                fill_color=self.highlight_color,
                fill_opacity=0.7,
                stroke_width=0
            ).move_to(entry_pos)
            highlighted_entries.add(entry)
        
        # Add labels
        mesh_label = MathTex(r"\text{Mass-Spring Mesh}", font_size=36, color=self.label_color)
        mesh_label.next_to(nodes, DOWN, buff=0.5)
        
        matrix_label = MathTex(r"\text{Global Stiffness Matrix } K", font_size=36, color=self.label_color)
        matrix_label.next_to(matrix_bg, DOWN, buff=0.5)
        
        # Add spring contribution formula
        formula = MathTex(
            r"K = \sum_{j} E_j^T K_j E_j",
            font_size=42,
            color=self.label_color
        ).to_edge(UP, buff=0.5)
        
        # Add highlighted spring label
        spring_label = MathTex(
            f"\\text{{Spring connecting nodes {node1} and {node2}}}",
            font_size=28,
            color=self.highlight_spring_color
        ).next_to(formula, DOWN, buff=0.3)
        
        # Add arrow pointing to highlighted region
        arrow = Arrow(
            mesh_center + RIGHT * 0.5,
            matrix_center + LEFT * 0.5,
            color=self.highlight_spring_color,
            stroke_width=3
        )
        
        # Group everything
        assembly_diagram = VGroup(
            nodes, springs, highlighted_spring,
            matrix_bg, matrix_grid, highlighted_entries,
            mesh_label, matrix_label, formula, spring_label, arrow
        )
        
        self.add(assembly_diagram)

class MatrixAssembly(MatrixAssemblyBase):
    """Light theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class MatrixAssemblyDark(MatrixAssemblyBase):
    """Dark theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)

class Spring3DBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"  # Dark background
            self.mass_color = "#e74c3c"    # Red masses
            self.spring_color = "#4a90e2"  # Blue spring
            self.force_color = "#f39c12"   # Orange force vectors
            self.axis_color = "#ecf0f1"    # Light gray axes
            self.label_color = WHITE
        else:  # light theme
            self.camera.background_color = WHITE  # Light background
            self.mass_color = "#c0392b"    # Darker red masses
            self.spring_color = "#2980b9"  # Darker blue spring
            self.force_color = "#d35400"   # Darker orange force vectors
            self.axis_color = "#2c3e50"    # Dark gray axes
            self.label_color = BLACK

    def construct(self):
        # Create two masses in 3D-perspective view (using 2D projections)
        pos_0 = np.array([-2.5, -0.8, 0])  # Bottom left 
        pos_1 = np.array([2.0, 1.5, 0])    # Top right (representing 3D displacement)
        
        # Create masses as circles with 3D shading effect
        mass_0 = Circle(radius=0.4, fill_color=self.mass_color, fill_opacity=0.8, stroke_color=self.mass_color, stroke_width=3)
        mass_0.move_to(pos_0)
        
        # Add gradient effect for 3D appearance
        mass_0_highlight = Circle(radius=0.25, fill_color=WHITE, fill_opacity=0.3, stroke_width=0)
        mass_0_highlight.move_to(pos_0 + UP * 0.1 + LEFT * 0.1)
        
        mass_1 = Circle(radius=0.4, fill_color=self.mass_color, fill_opacity=0.8, stroke_color=self.mass_color, stroke_width=3)
        mass_1.move_to(pos_1)
        
        mass_1_highlight = Circle(radius=0.25, fill_color=WHITE, fill_opacity=0.3, stroke_width=0)
        mass_1_highlight.move_to(pos_1 + UP * 0.1 + LEFT * 0.1)
        
        # Create spring as a zigzag pattern
        def spring_func(t):
            # Linear interpolation along the spring
            center_line = pos_0 + t * (pos_1 - pos_0)
            
            # Add zigzag pattern
            spring_direction = pos_1 - pos_0
            spring_length = np.linalg.norm(spring_direction)
            perpendicular = np.array([-spring_direction[1], spring_direction[0], 0])
            perpendicular = perpendicular / np.linalg.norm(perpendicular) if np.linalg.norm(perpendicular) > 0 else np.array([0, 1, 0])
            
            # Zigzag amplitude and frequency
            amplitude = 0.3
            frequency = 12
            
            zigzag_offset = amplitude * np.sin(2 * PI * frequency * t) * perpendicular
            return center_line + zigzag_offset
        
        spring = ParametricFunction(
            spring_func,
            t_range=[0.1, 0.9, 0.005],
            stroke_width=5,
            color=self.spring_color
        )
        
        # Add coordinate system in corner
        axes_origin = np.array([-5, -2.5, 0])
        axes_length = 1.2
        
        # X-axis (red)
        x_axis = Arrow(
            axes_origin,
            axes_origin + RIGHT * axes_length,
            color=RED,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        x_label = MathTex("x", font_size=32, color=RED).next_to(x_axis.get_end(), RIGHT, buff=0.1)
        
        # Y-axis (green)
        y_axis = Arrow(
            axes_origin,
            axes_origin + UP * axes_length,
            color=GREEN,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        y_label = MathTex("y", font_size=32, color=GREEN).next_to(y_axis.get_end(), UP, buff=0.1)
        
        # Z-axis (blue) - diagonal to suggest 3D
        z_axis = Arrow(
            axes_origin,
            axes_origin + UP * 0.6 * axes_length + LEFT * 0.8 * axes_length,
            color=BLUE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        z_label = MathTex("z", font_size=32, color=BLUE).next_to(z_axis.get_end(), UL, buff=0.1)
        
        # Position vectors and labels
        pos_0_label = MathTex(r"\mathbf{x}_0 = (x_0, y_0, z_0)", font_size=28, color=self.label_color)
        pos_0_label.next_to(mass_0, DOWN, buff=0.3)
        
        pos_1_label = MathTex(r"\mathbf{x}_1 = (x_1, y_1, z_1)", font_size=28, color=self.label_color)
        pos_1_label.next_to(mass_1, UP, buff=0.3)
        
        # Force vectors
        force_scale = 1.0
        spring_vector = pos_1 - pos_0
        spring_direction = spring_vector / np.linalg.norm(spring_vector)
        
        # Force on mass 0 (toward mass 1)
        force_0_end = pos_0 + force_scale * spring_direction
        force_0 = Arrow(
            pos_0,
            force_0_end,
            color=self.force_color,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        force_0_label = MathTex(r"\mathbf{f}_0", font_size=28, color=self.force_color)
        force_0_label.next_to(force_0.get_center(), DOWN + LEFT, buff=0.1)
        
        # Force on mass 1 (toward mass 0)  
        force_1_end = pos_1 - force_scale * spring_direction
        force_1 = Arrow(
            pos_1,
            force_1_end,
            color=self.force_color,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        force_1_label = MathTex(r"\mathbf{f}_1", font_size=28, color=self.force_color)
        force_1_label.next_to(force_1.get_center(), UP + RIGHT, buff=0.1)
        
        # Spring length vector
        length_vector = Arrow(
            pos_0 + DOWN * 0.8,
            pos_1 + DOWN * 0.8,
            color=self.axis_color,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        length_label = MathTex(r"\ell = ||\mathbf{x}_1 - \mathbf{x}_0||_2", font_size=28, color=self.label_color)
        length_label.next_to(length_vector.get_center(), DOWN, buff=0.2)
        
        # Add key equations
        equations = VGroup(
            MathTex(r"T = \frac{1}{2} m_0 ||\dot{\mathbf{x}}_0||^2 + \frac{1}{2} m_1 ||\dot{\mathbf{x}}_1||^2", font_size=32),
            MathTex(r"V = \frac{1}{2} k (\ell - \ell_0)^2", font_size=32),
            MathTex(r"\mathbf{f}_i = -k \frac{(\ell - \ell_0)}{\ell} (\mathbf{x}_i - \mathbf{x}_j)", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        equations.set_color(self.label_color)
        equations.to_corner(UR, buff=0.5)
        
        # Group everything
        spring_3d = VGroup(
            mass_0, mass_0_highlight, mass_1, mass_1_highlight, spring,
            x_axis, y_axis, z_axis, x_label, y_label, z_label,
            pos_0_label, pos_1_label,
            force_0, force_1, force_0_label, force_1_label,
            length_vector, length_label, equations
        )
        
        self.add(spring_3d)

class Spring3D(Spring3DBase):
    """Light theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class Spring3DDark(Spring3DBase):
    """Dark theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs)

class ConstraintsBase(Scene):
    def __init__(self, theme="light", **kwargs):
        super().__init__(**kwargs)
        self.theme = theme
        self.setup_theme_colors()
    
    def setup_theme_colors(self):
        if self.theme == "dark":
            self.camera.background_color = "#1a1a1a"  # Dark background
            self.free_node_color = "#4a90e2"    # Blue for free nodes
            self.pinned_node_color = "#e74c3c"  # Red for pinned nodes
            self.spring_color = "#ecf0f1"       # Light gray springs
            self.label_color = WHITE
            self.matrix_color = "#2c3e50"
        else:  # light theme
            self.camera.background_color = WHITE  # Light background
            self.free_node_color = "#2980b9"    # Darker blue for free nodes
            self.pinned_node_color = "#c0392b"  # Darker red for pinned nodes
            self.spring_color = "#95a5a6"       # Gray springs
            self.label_color = BLACK
            self.matrix_color = "#34495e"

    def construct(self):
        # Create a 4x3 mesh for better demonstration
        mesh_width = 4
        mesh_height = 3
        node_spacing = 1.0
        
        # Center the mesh
        mesh_center = LEFT * 2
        
        # Define which nodes are pinned (fixed) - top corners and middle top
        pinned_nodes = {0, 3, 6}  # Top-left, top-right, and one middle top node
        
        # Create nodes
        nodes = VGroup()
        node_positions = {}
        
        for j in range(mesh_height):
            for i in range(mesh_width):
                node_idx = j * mesh_width + i
                pos = (
                    mesh_center + 
                    RIGHT * (i * node_spacing - (mesh_width - 1) * node_spacing / 2) + 
                    UP * ((mesh_height - 1 - j) * node_spacing - (mesh_height - 1) * node_spacing / 2)
                )
                
                # Choose color based on whether node is pinned
                if node_idx in pinned_nodes:
                    node_color = self.pinned_node_color
                    node = Circle(
                        radius=0.15,
                        fill_color=node_color,
                        fill_opacity=0.9,
                        stroke_color=node_color,
                        stroke_width=4
                    )
                    # Add pin symbol
                    pin = Rectangle(width=0.1, height=0.3, fill_color=node_color, fill_opacity=1, stroke_width=0)
                    pin.move_to(pos)
                    node.move_to(pos)
                    node_group = VGroup(node, pin)
                else:
                    node_color = self.free_node_color
                    node = Circle(
                        radius=0.12,
                        fill_color=node_color,
                        fill_opacity=0.8,
                        stroke_color=node_color,
                        stroke_width=3
                    )
                    node.move_to(pos)
                    node_group = node
                
                # Add node index label
                label = MathTex(str(node_idx), font_size=18, color=self.label_color).move_to(pos)
                
                nodes.add(VGroup(node_group, label))
                node_positions[node_idx] = pos
        
        # Create springs (edges)
        springs = VGroup()
        
        # Horizontal springs
        for j in range(mesh_height):
            for i in range(mesh_width - 1):
                node1 = j * mesh_width + i
                node2 = j * mesh_width + (i + 1)
                
                spring = Line(
                    node_positions[node1],
                    node_positions[node2],
                    stroke_width=2,
                    color=self.spring_color
                )
                springs.add(spring)
        
        # Vertical springs
        for j in range(mesh_height - 1):
            for i in range(mesh_width):
                node1 = j * mesh_width + i
                node2 = (j + 1) * mesh_width + i
                
                spring = Line(
                    node_positions[node1],
                    node_positions[node2],
                    stroke_width=2,
                    color=self.spring_color
                )
                springs.add(spring)
        
        # Add legend
        legend_pinned = VGroup(
            Circle(radius=0.15, fill_color=self.pinned_node_color, fill_opacity=0.9, stroke_color=self.pinned_node_color, stroke_width=4),
            Rectangle(width=0.1, height=0.3, fill_color=self.pinned_node_color, fill_opacity=1, stroke_width=0),
            MathTex(r"\text{Pinned (fixed): } q_i = b_i", font_size=28, color=self.label_color)
        )
        legend_pinned[0].next_to(legend_pinned[2], LEFT, buff=0.3)
        legend_pinned[1].move_to(legend_pinned[0])
        
        legend_free = VGroup(
            Circle(radius=0.12, fill_color=self.free_node_color, fill_opacity=0.8, stroke_color=self.free_node_color, stroke_width=3),
            MathTex(r"\text{Free DOFs: } \hat{q}", font_size=28, color=self.label_color)
        )
        legend_free[0].next_to(legend_free[1], LEFT, buff=0.3)
        
        legend = VGroup(legend_pinned, legend_free).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend.to_corner(UR, buff=0.5)
        
        # Add constraint equations
        equations = VGroup(
            MathTex(r"q = P^T \hat{q} + b", font_size=36, color=self.label_color),
            MathTex(r"\text{where } P \text{ selects free DOFs}", font_size=28, color=self.label_color),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        equations.to_edge(DOWN, buff=0.8)
        
        # Add DOF reduction illustration
        total_nodes = mesh_width * mesh_height
        free_nodes = total_nodes - len(pinned_nodes)
        
        dof_info = VGroup(
            MathTex(f"\\text{{Total nodes: }}{total_nodes}", font_size=24, color=self.label_color),
            MathTex(f"\\text{{Pinned nodes: }}{len(pinned_nodes)}", font_size=24, color=self.pinned_node_color),
            MathTex(f"\\text{{Free DOFs: }}{free_nodes}", font_size=24, color=self.free_node_color),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        dof_info.to_corner(UL, buff=0.5)
        
        # Show some displacement vectors on free nodes to indicate motion
        displacement_vectors = VGroup()
        for node_idx in [4, 5, 7, 8, 9, 10, 11]:  # Some free nodes
            if node_idx not in pinned_nodes and node_idx < total_nodes:
                pos = node_positions[node_idx]
                # Add small displacement arrow
                disp_vector = Arrow(
                    pos,
                    pos + 0.3 * (RIGHT * np.cos(node_idx) + UP * np.sin(node_idx * 0.7)),
                    color=self.free_node_color,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.3,
                    stroke_opacity=0.6
                )
                displacement_vectors.add(disp_vector)
        
        # Group everything
        constraints_diagram = VGroup(
            springs, nodes, displacement_vectors,
            legend, equations, dof_info
        )
        
        self.add(constraints_diagram)

class Constraints(ConstraintsBase):
    """Light theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="light", **kwargs)

class ConstraintsDark(ConstraintsBase):
    """Dark theme version"""
    def __init__(self, **kwargs):
        super().__init__(theme="dark", **kwargs) 