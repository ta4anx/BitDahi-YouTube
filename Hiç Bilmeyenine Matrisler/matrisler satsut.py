from manim import *

class MatrixHighlightScene(Scene):
    def construct(self):
        # Create the matrix as a Table
        matrix = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])
        self.play(Create(matrix))
        self.wait(3)

        # Highlight the rows
        row_rects = VGroup()
        for row in range(2):
            rect = SurroundingRectangle(matrix.get_rows()[row], color=YELLOW, buff=0.1)
            row_rects.add(rect)
        self.play(Create(row_rects))
        rows_text = Text("2 satır").next_to(matrix, DOWN)
        self.play(Write(rows_text))
        self.wait(1)

        # Unhighlight rows, highlight columns
        self.play(FadeOut(row_rects), FadeOut(rows_text))
        col_rects = VGroup()
        for col in range(3):
            rect = SurroundingRectangle(matrix.get_columns()[col], color=BLUE, buff=0.1)
            col_rects.add(rect)
        self.play(Create(col_rects))
        cols_text = Text("3 sütun").next_to(matrix, RIGHT)
        self.play(Write(cols_text))
        self.wait(1)
        # Unhighlight columns, highlight the entire matrix
        self.play(FadeOut(col_rects), FadeOut(cols_text))
        matrix_rect = SurroundingRectangle(matrix, color=GREEN, buff=0.1)
        self.play(Create(matrix_rect))
        matrix_text = Text("2x3 matris olarak adlandırılır.").next_to(matrix, DOWN)
        self.play(Write(matrix_text))
        self.wait(3)

        # Fade out everything
        self.play(FadeOut(matrix_rect),FadeOut(matrix_text) )
        self.wait(1)
        # Show "i" on the left and "j" on the right, then fade out
        i_text = Text("i", font_size=48).next_to(matrix, LEFT, buff=1)
        j_text = Text("j", font_size=48).next_to(matrix, RIGHT, buff=1)
        i_text.set_color([BLUE, PURPLE])
        j_text.set_color([BLUE, PURPLE])
        self.play(Write(i_text), Write(j_text))
        self.wait(1)
        self.play(FadeOut(i_text), FadeOut(j_text))
        # Highlight the i-hat (row indices) 1 and 2
        i_labels = VGroup(
            Text("i=1", font_size=28).next_to(matrix.get_rows()[0], LEFT, buff=0.6),
            Text("i=2", font_size=28).next_to(matrix.get_rows()[1], LEFT, buff=0.6)
        )
        i_rects = VGroup(
            SurroundingRectangle(matrix.get_rows()[0], color=ORANGE, buff=0.1),
            SurroundingRectangle(matrix.get_rows()[1], color=ORANGE, buff=0.1)
        )
        self.play(Create(i_rects), Write(i_labels))
        self.wait(1)
        self.play(FadeOut(i_rects), FadeOut(i_labels))

        # Highlight the j-hat (column indices) 1, 2, 3
        j_labels = VGroup(
            Text("j=1", font_size=28).next_to(matrix.get_columns()[0], UP, buff=0.3),
            Text("j=2", font_size=28).next_to(matrix.get_columns()[1], UP, buff=0.3),
            Text("j=3", font_size=28).next_to(matrix.get_columns()[2], UP, buff=0.3)
        )
        j_rects = VGroup(
            SurroundingRectangle(matrix.get_columns()[0], color=PURPLE, buff=0.1),
            SurroundingRectangle(matrix.get_columns()[1], color=PURPLE, buff=0.1),
            SurroundingRectangle(matrix.get_columns()[2], color=PURPLE, buff=0.1)
        )
        self.play(Create(j_rects), Write(j_labels))
        self.wait(1)
        self.play(FadeOut(j_rects), FadeOut(j_labels))

        # Highlight the (2,3) element by intersecting i-hat 2 and j-hat 3
        row2_rect = SurroundingRectangle(matrix.get_rows()[1], color=ORANGE, buff=0.1)
        col3_rect = SurroundingRectangle(matrix.get_columns()[2], color=PURPLE, buff=0.1)
        element_23 = matrix.get_entries()[5]  # (2,3) element in 2x3 matrix (row-major order)
        element_rect = SurroundingRectangle(element_23, color=RED, buff=0.15)
        self.play(Create(row2_rect), Create(col3_rect))
        self.wait(0.5)
        self.play(Create(element_rect))
        element_label = Text("i=2, j=3", font_size=32).next_to(element_23, DOWN, buff=0.3)
        self.play(Write(element_label))
        a23_text = Text("A'nın (2,3) elemanı = 6", font_size=32).next_to(element_label, DOWN, buff=0.6)
        self.play(Write(a23_text))
        self.wait(2)
        ij_text = Text("i = satır, j = sütun", font_size=32).to_edge(UP)
        self.play(Write(ij_text))
        self.wait(2)
        self.play(FadeOut(row2_rect), FadeOut(col3_rect), FadeOut(element_rect), FadeOut(element_label), FadeOut(a23_text), FadeOut(ij_text))
        