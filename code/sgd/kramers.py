from manim import *
import numpy as np


class MeanEscapeTime(ThreeDScene):
    def construct(self):
        # Set the axes
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        # Define the surfaces based on the provided sketch
        # 'a1' and 'a2' are the minima, 'b' is the saddle point
        def combined_valley(u, v):
            steep_minima = -np.exp(-0.5 * ((u + 1) ** 2 + (v + 1) ** 2))
            flat_minima = -np.exp(-0.1 * ((u - 1) ** 2 + (v - 1) ** 2))
            saddle_point_height = 0.1  # Height of the saddle point, adjust as needed
            saddle = saddle_point_height * (u**2 - v**2)
            return np.array([u, v, steep_minima + flat_minima + saddle])

        # Create the surface
        combined_surface = Surface(
            lambda u, v: combined_valley(u, v),
            u_range=[-2, 2],
            v_range=[-2, 2],
            fill_opacity=0.8,
            checkerboard_colors=[BLUE, BLUE],
        )

        # Create the ball and its start position at 'a1' which is a steep minima
        ball = Sphere(radius=0.1, color=RED)
        ball_start_pos = np.array(
            [-1, -1, combined_valley(-1, -1)[2]]
        )  # Position at 'a1'
        ball.move_to(ball_start_pos)

        # Define the path from 'a1' to 'a2' via 'b'
        # We calculate the z-coordinate from the combined_valley function for accuracy
        path_to_flat = VMobject()
        path_points = [
            ball_start_pos,
            np.array([0, 0, combined_valley(0, 0)[2]]),  # Saddle point 'b'
            np.array([1, 1, combined_valley(1, 1)[2]]),  # Flat minima 'a2'
        ]
        path_to_flat.set_points_smoothly(path_points)

        # Animations
        self.add(axes, combined_surface, ball)
        self.play(MoveAlongPath(ball, path_to_flat), run_time=6)
        self.wait()

        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
