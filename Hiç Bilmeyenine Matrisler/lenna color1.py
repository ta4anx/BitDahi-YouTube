from manim import *

class RGBMatrixScene(Scene):
    def construct(self):
        # Load and show the full color image
        img = ImageMobject("lenna_color.png").scale(2)
        self.play(FadeIn(img))
        self.wait(1)

        # Define the 5x5 RGB matrices
        R = [
            [177, 165, 152, 141, 130],
            [185, 172, 160, 148, 135],
            [195, 183, 170, 158, 145],
            [205, 192, 180, 167, 155],
            [215, 202, 190, 178, 165]
        ]
        G = [
            [130, 118, 105, 95, 85],
            [138, 126, 113, 103, 93],
            [148, 136, 123, 111, 100],
            [158, 146, 133, 121, 110],
            [168, 156, 143, 131, 120]
        ]
        B = [
            [98, 86, 72, 60, 52],
            [106, 94, 80, 68, 60],
            [116, 104, 90, 78, 70],
            [126, 114, 100, 88, 80],
            [136, 124, 110, 98, 90]
        ]

        # Create a patch outline on the image
        patch_size = 0.1
        squares = VGroup()
        for i in range(5):
            for j in range(5):
                color = rgb_to_color([R[i][j], G[i][j], B[i][j]])
                square = Square(side_length=patch_size)
                square.set_fill(color, opacity=1)
                square.set_stroke(BLACK, width=0.5)
                square.move_to(
                    img.get_corner(UP + LEFT) +
                    RIGHT * patch_size * (j + 1.5) +
                    DOWN * patch_size * (i + 1.5)
                )
                squares.add(square)

        patch_outline = SurroundingRectangle(squares, color=YELLOW)
        self.play(Create(patch_outline))
        self.wait(0.5)

        # Zoom into patch
        self.play(
            img.animate.scale(0.4).shift(LEFT * 2.5),
            squares.animate.scale(5).move_to(ORIGIN),
            patch_outline.animate.scale(5).move_to(ORIGIN),
            run_time=2
        )
        self.wait(0.5)

        # Create R, G, B matrices
        r_matrix = Matrix(R).scale(0.4).to_edge(UP).set_color(RED)
        g_matrix = Matrix(G).scale(0.4).to_edge(RIGHT).set_color(GREEN)
        b_matrix = Matrix(B).scale(0.4).to_edge(DOWN).set_color(BLUE)

        # Titles
        r_label = Text("Kırmızı (Red) Kanalı", color=RED).scale(0.5).next_to(r_matrix, UP)
        g_label = Text("Yeşil(Green) Kanalı", color=GREEN).scale(0.5).next_to(g_matrix, UP)
        b_label = Text("Mavi (Blue) Kanalı", color=BLUE).scale(0.5).next_to(b_matrix, UP)

        # Animate appearance
        self.play(
            FadeOut(img),
            FadeOut(patch_outline),
            squares.animate.shift(LEFT * 2.5),
        )
        self.play(Write(r_matrix), Write(r_label))
        self.play(Write(g_matrix), Write(g_label))
        self.play(Write(b_matrix), Write(b_label))
        self.wait(2)

        # Step 1: Move RGB matrices to center to "overlay"
        target_pos = ORIGIN

        self.play(
            FadeOut(squares),
            r_matrix.animate.move_to(target_pos + UP * 0.4),
            g_matrix.animate.move_to(target_pos),
            b_matrix.animate.move_to(target_pos + DOWN * 0.4),
            FadeOut(r_label),
            FadeOut(g_label),
            FadeOut(b_label),
            run_time=2
        )
        self.wait(0.5)

        # Step 2: Fade them out and show the combined RGB color matrix
        color_matrix_group = VGroup()
        square_size = 0.6

        for i in range(5):
            for j in range(5):
                color = rgb_to_color([R[i][j], G[i][j], B[i][j]])
                square = Square(side_length=square_size)
                square.set_fill(color, opacity=1)
                square.set_stroke(BLACK, width=0.5)
                square.move_to(ORIGIN + RIGHT * j * square_size + DOWN * i * square_size)
                color_matrix_group.add(square)

        color_matrix_group.move_to(ORIGIN)


        self.play(
            FadeOut(r_matrix),
            FadeOut(g_matrix),
            FadeOut(b_matrix),

            FadeIn(color_matrix_group),

            run_time=2
        )
        self.wait(2)
