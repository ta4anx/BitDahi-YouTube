from manim import *

class MatrixTitleIntro(Scene):
    def construct(self):
        # Step 1: Create a 9x9 matrix with "MATRİSLER" on the diagonal, numbers elsewhere
        title = "MATRİSLER"
        size = 9
        matrix_data = []
        for i in range(size):
            row = []
            for j in range(size):
                if i == j:
                    row.append(title[i])
                else:
                    # Fill with numbers, e.g., row*size + col + 1
                    row.append(str(i * size + j + 1))
            matrix_data.append(row)

        # Manually define the matrix for full control
        def cell_mobject(cell):
            # Use Text for non-ASCII, MathTex for numbers
            if cell.isnumeric():
                return MathTex(cell)
            else:
                return Text(cell, font_size=36)
        matrix_mob = MobjectTable(
            [[cell_mobject(cell) for cell in row] for row in matrix_data],
            include_outer_lines=True
        ).scale(0.7)
        self.play(FadeIn(matrix_mob))
        self.wait(1)

        # Step 2: Animate the diagonal letters to move and form the word "MATRİSLER"
        diagonal_letters = [
            matrix_mob.get_entries()[i * size + i] for i in range(size)
        ]
        # Group the diagonal letter mobjects (these are part of the matrix)
        # Save the original positions for smooth animation
        diagonal_letters_group = VGroup(*diagonal_letters)
        matrisler_group = VGroup(
            *[Text(title[i], font_size=36) for i in range(size)]
        ).arrange(RIGHT, buff=0.3).move_to(matrix_mob)

        # Animate diagonal letters to their new positions, fade out only the non-diagonal elements and lines
        non_diagonal_entries = [
            entry for i, entry in enumerate(matrix_mob.get_entries())
            if (i // size) != (i % size)
        ]

        # Animate each diagonal letter to its new position using Transform, keeping the original objects
        self.play(
            *[
                Transform(diagonal_letters[i], matrisler_group[i], run_time=1.2)
                for i in range(size)
            ],
            FadeOut(VGroup(*non_diagonal_entries), shift=DOWN, lag_ratio=0.1, run_time=1.5),
            FadeOut(matrix_mob.get_horizontal_lines(), run_time=1.5),
            FadeOut(matrix_mob.get_vertical_lines(), run_time=1.5),
        )
        self.wait(0.5)
        # Step 3: Animate "NEDİR?" appearing below "MATRİSLER" and center both together
        nedir_text = Text("NEDİR?", font_size=72)
        # Re-create the "MATRİSLER" group with the same style as "NEDİR?"
        matrisler_final = VGroup(
            *[Text(title[i], font_size=72) for i in range(size)]
        ).arrange(RIGHT, buff=0.3)
        # Position the new "MATRİSLER" group at the location of the transformed diagonal letters
        matrisler_final.move_to(VGroup(*diagonal_letters).get_center())
        # Animate the diagonal letters (now forming "MATRİSLER") to zoom in and match the size and position of matrisler_final
        self.play(
            Transform(VGroup(*diagonal_letters), matrisler_final, run_time=1.2)
        )
        # Replace the transformed diagonal letters with the styled "MATRİSLER"
        # Just add "NEDİR?" below the existing diagonal letters (now forming "MATRİSLER")
        nedir_text = Text("NEDİR?", font_size=72)
        nedir_text.next_to(VGroup(*diagonal_letters), DOWN, buff=0.5)
        self.play(
            FadeIn(nedir_text, shift=DOWN)
        )
        self.wait(2)
