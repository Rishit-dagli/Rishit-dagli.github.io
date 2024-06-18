from manim import *


class FlatSharpMinimaScene(Scene):
    def construct(self):
        # Setup axes for the graphs with smaller margins
        axes = Axes(
            x_range=[-3, 3, 0.5],
            y_range=[0, 2, 0.5],
            x_length=5,  # increased length for tighter layout
            y_length=4,  # increased length for tighter layout
            axis_config={"color": WHITE},
        )

        # Define the functions for flat and sharp minima
        flat_curve = axes.plot(lambda x: 1 - np.exp(-1 * x**2) + 0.7, color=GREEN)
        sharp_curve = axes.plot(lambda x: 1 - np.exp(-4 * x**2) + 0.7, color=RED)

        # The actual minima of the functions is at (0, 0.7), adjusting the dot placement
        flat_minima_dot = Dot(axes.c2p(0, 0.7), color=BLUE)
        sharp_minima_dot = Dot(axes.c2p(0, 0.7), color=BLUE)

        # Labels for the minima, placed exactly above the end of the graph
        flat_minima_label = MathTex("m_1", color=WHITE).next_to(
            flat_minima_dot, RIGHT, buff=0.2
        )
        sharp_minima_label = MathTex("m_2", color=WHITE).next_to(
            sharp_minima_dot, RIGHT, buff=0.2
        )

        # Labels for the types of minima, positioned relative to their respective graphs
        flat_label = (
            Text("Flat Minima", color=GREEN)
            .scale(0.7)
            .next_to(flat_curve, UP, buff=1.3)
            .shift(2.75 * LEFT)
        )
        sharp_label = (
            Text("Sharp Minima", color=RED)
            .scale(0.7)
            .next_to(sharp_curve, UP, buff=1.3)
            .shift(RIGHT)
            .shift(RIGHT)
            .shift(RIGHT)
        )

        # Group the components of each graph
        flat_graph = VGroup(axes, flat_curve, flat_minima_dot, flat_minima_label)
        sharp_graph = VGroup(
            axes.copy(), sharp_curve, sharp_minima_dot, sharp_minima_label
        )

        # Position the graphs closer to each other
        graphs = VGroup(flat_graph, sharp_graph).arrange(
            RIGHT, buff=1
        )  # reduced buff for tighter layout

        # Add the graphs and labels to the scene
        self.add(graphs)
        self.add(flat_label)
        self.add(sharp_label)
