from manim import *


class GradientDescentScene(ThreeDScene):
    def construct(self):
        # Define the axes.
        axes = ThreeDAxes()

        # Define the function that you are using. For example, z = f(x, y).
        def function(x, y):
            return np.sin(x) * np.cos(y)

        # Create a surface.
        surface = Surface(
            lambda u, v: axes.c2p(u, v, function(u, v)),
            u_range=[-PI, PI],
            v_range=[-PI, PI],
            resolution=(30, 30),
        ).set_fill_by_checkerboard(ORANGE, opacity=0.5)

        # Define the ball at a particular point (x_k, y_k).
        ball = Sphere(radius=0.2, color=RED).move_to(axes.c2p(1, 1, function(1, 1)))

        # Define the gradient vector at the same point as the ball.
        gradient_vector = Arrow(
            start=axes.c2p(1, 1, function(1, 1)),
            end=axes.c2p(1.5, 1.5, function(1, 1)),
            buff=0,
            color=BLUE,
        )
        gradient_label = MathTex("-\\nabla f(x_k)").next_to(
            gradient_vector.get_end(), UP
        )

        # Define the momentum vector at the same point as the ball.
        momentum_vector = Arrow(
            start=axes.c2p(1, 1, function(1, 1)),
            end=axes.c2p(0.5, 0.5, function(1, 1)),
            buff=0,
            color=GREEN,
        )
        momentum_label = MathTex("\\mu k_{-1}").next_to(momentum_vector.get_end(), DOWN)

        # Add everything to the scene at once, without animations.
        self.add(
            axes,
            surface,
            ball,
            gradient_vector,
            gradient_label,
            momentum_vector,
            momentum_label,
        )
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
