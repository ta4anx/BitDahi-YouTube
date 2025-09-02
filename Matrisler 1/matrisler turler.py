from manim import *
import random

class ExpandZeroMatrix(Scene):
    def construct(self):

        # Initial 2x3 zero matrix
        matrix_2x3 = Matrix([[0, 0, 0],
                             [0, 0, 0]])
        matrix_2x3.move_to(ORIGIN)

        # Target 3x4 zero matrix
        matrix_3x4 = Matrix([[0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]])
        matrix_3x4.move_to(ORIGIN)

        # Show the 2x3 matrix
        title = Title("Sıfır Matris").next_to(matrix_2x3, UP, buff=1)
        self.play(Write(title))
        self.wait(1)
        self.play(Write(matrix_2x3))
        self.wait(1)

        # Animate the expansion to 3x4
        self.play(Transform(matrix_2x3, matrix_3x4))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(matrix_2x3))

        # Show a 3x3 square matrix with random numbers
        random_matrix_3x3 = Matrix([
            [random.randint(1, 9) for _ in range(3)] for _ in range(3)
        ])
        random_matrix_3x3.move_to(ORIGIN)
        title_square = Title("Kare Matris")
        self.play(Write(title_square))
        self.wait(1)
        #write the description
        description = Text("Satır ve sütun sayısı eşit olan matristir.", font_size=36)
        description.next_to(title_square, DOWN, buff=0.5)
        self.play(Write(description))
        self.wait(1)

        self.play(Write(random_matrix_3x3))
        self.wait(1)


        self.play(FadeOut(random_matrix_3x3))

        # Show a 4x4 square matrix with random numbers
        random_matrix_4x4 = Matrix([
            [random.randint(1, 9) for _ in range(4)] for _ in range(4)
        ])
        random_matrix_4x4.move_to(ORIGIN)
        self.play(Write(random_matrix_4x4))
        self.wait(1)

        self.play(FadeOut(random_matrix_4x4))

        # Show a 1x1 square matrix
        random_matrix_1x1 = Matrix([[random.randint(1, 9)]])
        random_matrix_1x1.move_to(ORIGIN)
        self.wait(1)
        self.play(Write(random_matrix_1x1))
        self.wait(1)

        # Highlight the only entry (i == j == 0)
        rect_1x1 = SurroundingRectangle(random_matrix_1x1.get_entries()[0], color=YELLOW, buff=0.15)
        self.play(Create(rect_1x1))
        self.wait(1)
        self.play(FadeOut(rect_1x1),FadeOut(random_matrix_1x1), FadeOut(title_square), FadeOut(description))

        # Create 3x3 identity matrix
        identity_3x3 = Matrix([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        identity_3x3.move_to(ORIGIN)

        # Show the 3x3 identity matrix
        title_id = Title("Birim Matris")
        self.play(Write(title_id))
        self.wait(1)
        # Write the description
        description_id = Text("Ana köşegenindeki elemeanlar 1, \n diğer elemanları 0 olan matristir.", font_size=36)
        description_id.next_to(title_id, DOWN, buff=0.5)
        self.play(Write(description_id))
        self.play(Write(identity_3x3))
        self.wait(1)
        #I veya In ile gösterilir.
        description_In = Text("I veya I", font_size=36)
        subscript_n = Text("n", font_size=28).next_to(description_In, RIGHT, buff=0.07).align_to(description_In, DOWN)
        description_In = VGroup(description_In, subscript_n, Text(" ile gösterilir.", font_size=36).next_to(subscript_n, RIGHT, buff=0.05))
        description_In.to_edge(DOWN, buff=0.5)
        self.play(Write(description_In))
        self.wait(1)

        # Highlight the diagonal ones
        diagonal_indices = [(0, 0), (1, 1), (2, 2)]
        highlight_rects = VGroup()
        for i, j in diagonal_indices:
            rect = SurroundingRectangle(identity_3x3.get_entries()[i*3 + j], color=YELLOW, buff=0.15)
            highlight_rects.add(rect)
        self.play(Create(highlight_rects))
        self.wait(0.1)
        # Draw a diagonal line passing through all diagonal entries
        diagonal_entries = [identity_3x3.get_entries()[i*3 + i] for i in range(3)]
        diagonal_line = VMobject(color=RED, stroke_width=6)
        diagonal_line.set_points_as_corners([entry.get_center() for entry in diagonal_entries])
        self.play(Create(diagonal_line))
        self.wait(1)
        self.play(FadeOut(diagonal_line))
        #highlight the zero entries
        zero_indices = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        highlight_zero_rects = VGroup()
        for i, j in zero_indices:
            rect = SurroundingRectangle(identity_3x3.get_entries()[i*3 + j], color=BLUE, buff=0.15)
            highlight_zero_rects.add(rect)
        self.play(Create(highlight_zero_rects), run_time=0.30)
        self.wait(0.75)
        self.play(FadeOut(highlight_zero_rects))
        self.wait(0.25)
        # Prepare 5x5 identity matrix
        identity_5x5 = Matrix([
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]
        ])
        identity_5x5.move_to(ORIGIN)

        # Animate expansion to 5x5 identity matrix
        self.play(Transform(identity_3x3, identity_5x5), FadeOut(highlight_rects),FadeOut(description_id), FadeOut(description_In))
        self.wait(1)
        #highlight the diagonal ones in 5x5
        diagonal_indices_5x5 = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        highlight_rects_5x5 = VGroup()
        for i, j in diagonal_indices_5x5:
            rect = SurroundingRectangle(identity_5x5.get_entries()[i*5 + j], color=YELLOW, buff=0.15)
            highlight_rects_5x5.add(rect)
        self.play(Create(highlight_rects_5x5))
        self.wait(0.1)
        # Draw a diagonal line passing through all diagonal entries in 5x5
        diagonal_entries_5x5 = [identity_5x5.get_entries()[i*5 + i] for i in range(5)]
        diagonal_line_5x5 = VMobject(color=RED, stroke_width=6)
        diagonal_line_5x5.set_points_as_corners([entry.get_center() for entry in diagonal_entries_5x5])
        self.play(Create(diagonal_line_5x5))
        self.wait(1)
        self.play(FadeOut(diagonal_line_5x5))
        self.wait(0.25)
        self.play(FadeOut(title_id), FadeOut(identity_3x3), FadeOut(highlight_rects_5x5), FadeOut(identity_5x5))


        # Create a diagonal matrix
        diagonal_matrix = Matrix([
            [1, 0, 0],
            [0, 2, 0],
            [0, 0, 3]
        ])
        diagonal_matrix.move_to(ORIGIN)

        # Show the diagonal matrix
        title_diag = Title("Köşegen Matris")
        self.play(Write(title_diag))
        self.wait(1)
        self.play(Write(diagonal_matrix))
        self.wait(1)

        # Highlight the diagonal entries
        diagonal_indices = [(0, 0), (1, 1), (2, 2)]
        highlight_rects = VGroup()
        for i, j in diagonal_indices:
            rect = SurroundingRectangle(diagonal_matrix.get_entries()[i*3 + j], color=YELLOW, buff=0.15)
            highlight_rects.add(rect)
        self.play(Create(highlight_rects))
        self.wait(1)
        # draw a diagonal line
        # Draw a diagonal line passing through all diagonal entries
        diagonal_entries = [diagonal_matrix.get_entries()[i*3 + i] for i in range(3)]
        diagonal_line = VMobject(color=RED, stroke_width=6)
        diagonal_line.set_points_as_corners([entry.get_center() for entry in diagonal_entries])
        self.play(Create(diagonal_line))
        self.wait(1)
        self.play(FadeOut(diagonal_line))
        #highlight the zero entries
        zero_indices = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        highlight_zero_rects = VGroup()
        for i, j in zero_indices:
            rect = SurroundingRectangle(diagonal_matrix.get_entries()[i*3 + j], color=BLUE, buff=0.15)
            highlight_zero_rects.add(rect)
        self.play(Create(highlight_zero_rects), run_time=0.40)
        self.wait(0.25)
        self.play(FadeOut(highlight_zero_rects))
        self.wait(0.25)
        self.play(FadeOut(title_diag), FadeOut(diagonal_matrix), FadeOut(highlight_rects))

        # upper triangular matrix
        upper_triangular_matrix = Matrix([
            [1, 2, 3],
            [0, 4, 5],
            [0, 0, 6]
        ])
        upper_triangular_matrix.move_to(ORIGIN)
        # Show the upper triangular matrix
        title_upper = Title("Üst Üçgen Matris")
        self.play(Write(title_upper))
        self.wait(1)
        self.play(Write(upper_triangular_matrix))
        self.wait(1)
        # Highlight the upper triangular entries
        upper_indices = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
        highlight_upper_rects = VGroup()
        for i, j in upper_indices:
            rect = SurroundingRectangle(upper_triangular_matrix.get_entries()[i*3 + j], color=YELLOW, buff=0.15)
            highlight_upper_rects.add(rect)
        self.play(Create(highlight_upper_rects))
        self.wait(1)
        # Draw a right angle triangle at the right of the matrix
        # Calculate the positions of the non-zero (upper triangular) entries
        upper_entries = [upper_triangular_matrix.get_entries()[i*3 + j] for i, j in upper_indices]
        # Get their centers
        points = [entry.get_center() for entry in upper_entries]
        # Create a polygon that covers the upper triangle area
        triangle = Polygon(
            points[0],  # (0,0)
            points[1],  # (0,1)
            points[2],  # (0,2)
            points[4],  # (1,2)
            points[5],  # (2,2)
            points[3],  # (1,1)
            points[0],  # back to (0,0)
            color=TEAL, fill_opacity=0.3
        )
        triangle.move_to(upper_triangular_matrix.get_center())
        self.play(Create(triangle))
        self.wait(1)
        self.play(FadeOut(triangle))
        self.play(FadeOut(highlight_upper_rects), FadeOut(title_upper), FadeOut(upper_triangular_matrix))
        self.wait(0.25)

        
        # lower triangular matrix
        lower_triangular_matrix = Matrix([
            [1, 0, 0],
            [2, 3, 0],
            [4, 5, 6]
        ])
        lower_triangular_matrix.move_to(ORIGIN)
        # Show the lower triangular matrix
        title_lower = Title("Alt Üçgen Matris")
        self.play(Write(title_lower))
        self.wait(1)
        self.play(Write(lower_triangular_matrix))
        self.wait(1)
        # Highlight the lower triangular entries
        lower_indices = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2)]
        highlight_lower_rects = VGroup()
        for i, j in lower_indices:
            rect = SurroundingRectangle(lower_triangular_matrix.get_entries()[i*3 + j], color=YELLOW, buff=0.15)
            highlight_lower_rects.add(rect)
        self.play(Create(highlight_lower_rects))
        self.wait(1)
        # Draw a right angle triangle at the left of the matrix
        # Calculate the positions of the non-zero (lower triangular) entries
        lower_entries = [lower_triangular_matrix.get_entries()[i*3 + j] for i, j in lower_indices]
        # Get their centers
        points_lower = [entry.get_center() for entry in lower_entries]
        # Create a polygon that covers the lower triangle area
        triangle_lower = Polygon(
            points_lower[0],  # (0,0)
            points_lower[1],  # (1,0)
            points_lower[3],  # (2,0)
            points_lower[4],  # (2,1)
            points_lower[5],  # (2,2)
            points_lower[2],  # (1,1)
            points_lower[0],  # back to (0,0)
            color=TEAL, fill_opacity=0.3
        )
        triangle_lower.move_to(lower_triangular_matrix.get_center())
        self.play(Create(triangle_lower))
        self.wait(1)
        self.play(FadeOut(triangle_lower))
        self.play(FadeOut(highlight_lower_rects), FadeOut(title_lower), FadeOut(lower_triangular_matrix))