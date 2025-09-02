from manim import *

class LennaToMatrix(Scene):
    def construct(self):
        # Load the grayscale image
        image = ImageMobject("lenna_gray.png")
        image.scale(1.5)  # Reduce scale to fit into the screen
        self.play(FadeIn(image))
        self.wait(1)

        # Define patch location and size (in image pixels)
        patch_size = 5
        px_size = 0.08  # Adjust pixel size to align visually with the smaller image

        # Extracted patch grayscale values (example data)
        values = [
            [143, 130, 115, 102, 88],
            [150, 137, 123, 110, 95],
            [160, 145, 130, 117, 103],
            [170, 155, 140, 125, 110],
            [180, 165, 150, 135, 120]
        ]

        # Create colored squares for each pixel
        squares = VGroup()
        for i, row in enumerate(values):
            for j, val in enumerate(row):
                gray_level = val / 255
                square = Square(side_length=px_size)
                square.set_fill(gray_level * WHITE, opacity=1)
                square.set_stroke(BLACK, width=0.5)
                square.move_to(
                    image.get_corner(UP + LEFT) +
                    RIGHT * px_size * (j + 1.2) +  # Adjust placement for smaller image
                    DOWN * px_size * (i + 1.2)
                )
                squares.add(square)

        # Add a rectangle around the patch
        patch_outline = SurroundingRectangle(squares, color=YELLOW)
        self.play(Create(patch_outline))
        self.wait(0.5)

        # Zoom into the patch (scale + move squares to center)
        self.play(
            image.animate.scale(0.5).shift(LEFT * 2),
            squares.animate.scale(6).move_to(ORIGIN),
            patch_outline.animate.scale(6).move_to(ORIGIN),
            run_time=2
        )
        self.wait(0.5)

        # Transform the squares into a matrix
        matrix = Matrix(values)
        matrix.scale(0.8)
        matrix.to_edge(RIGHT)

        self.play(
            FadeOut(image),
            FadeOut(patch_outline),
            squares.animate.shift(LEFT * 3.5),
            Write(matrix),
            run_time=2
        )
        self.wait(2)
