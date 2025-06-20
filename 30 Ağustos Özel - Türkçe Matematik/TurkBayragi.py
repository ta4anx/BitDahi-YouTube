from manim import*
class TurkishFlag(Scene):
    def construct(self):
        # Define colors and proportions based on the Turkish Flag Law
        TURKISH_RED = "#E30A17"
        WHITE = "#FFFFFF"

        # Set the base unit L (height of the flag)
        L = 4.0
        G = 1.5 * L  # Width of the flag

        # Create the red background, centered at the origin
        background = Rectangle(
            width=G,
            height=L,
            color=TURKISH_RED,
            fill_opacity=1,
            stroke_width=0
        )

        # --- Crescent and Star Calculations ---
        # All positions are relative to the center of the flag (ORIGIN)
        # Hoist (left edge) x-coordinate
        hoist_x = -G / 2

        # Outer circle of the crescent
        outer_crescent_radius = (0.5 * L) / 2
        outer_crescent_center_x = hoist_x + (0.5 * L)
        outer_crescent = Circle(
            radius=outer_crescent_radius,
            color=WHITE,
            fill_opacity=1,
            stroke_width=0
        ).move_to([outer_crescent_center_x, 0, 0])

        # Inner circle (this "cuts out" the crescent shape)
        inner_crescent_radius = (0.4 * L) / 2
        inner_crescent_center_x = outer_crescent_center_x + (1 / 16.0) * L
        inner_crescent = Circle(
            radius=inner_crescent_radius,
            color=TURKISH_RED,
            fill_opacity=1,
            stroke_width=0
        ).move_to([inner_crescent_center_x, 0, 0])

        # Star
        star_radius = (0.25 * L) / 2
        # The center of the star is at a distance of 1/3 * L from the center of the crescent's outer circle.
        star_center_x = outer_crescent_center_x + (1 / 3.0) * L
        star = Star(
            n=5,
            outer_radius=star_radius,
            color=WHITE,
            fill_opacity=1,
            stroke_width=0,
            # Rotate the star so one point faces the hoist (left)
            start_angle=PI 
        ).move_to([star_center_x, 0, 0])

        # --- Animation Sequence ---
        self.play(DrawBorderThenFill(background))
        self.wait(0.5)
        self.play(GrowFromCenter(outer_crescent))
        self.wait(0.2)
        # The inner circle appears on top of the white one, creating the crescent
        # Animate the inner crescent moving from right to left into position
        inner_crescent_start = inner_crescent.copy().move_to([inner_crescent_center_x + L-2, 0, 0])
        self.add(inner_crescent_start)
        self.play(
            inner_crescent_start.animate.move_to([inner_crescent_center_x, 0, 0])
        )
        # Replace with the actual inner_crescent for further animations if needed
        self.remove(inner_crescent_start)
        self.add(inner_crescent)
        self.wait(0.5)
        self.play(DrawBorderThenFill(star))
        self.wait(1)

