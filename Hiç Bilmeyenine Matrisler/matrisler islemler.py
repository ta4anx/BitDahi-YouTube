from manim import *
class MatrislerleIslemler(Scene):
    def construct(self):
        # Matrisler text checklist text
        # ✅ Denklem sistemlerini çözebileceğiz
        #✅ Dönüşümleri ifade edebileceğiz
        # ✅ Ve verilerle çalışırken çözüm yolları inşa edebileceğiz
        title = Text("Matrislerle İşlemler", font_size=48)
        title.set_color_by_gradient(BLUE, PURPLE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        checklist = VGroup(
            Text("Bu işlemler sayesinde:", font_size=36).to_edge(UP),
            Text("· Denklem sistemlerini çözebileceğiz", font_size=36),
            Text("· Dönüşümleri ifade edebileceğiz", font_size=36),
            Text("· Verilerle çalışırken çözüm yolları inşa edebileceğiz", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT, buff=1.5)
        self.play(LaggedStartMap(Write, checklist, lag_ratio=0.5))
        self.wait(2)
        self.play(FadeOut(checklist))
        self.wait(1)

        #Determinant
        determinant_text = Text("Determinant", font_size=36)
        determinant_text.to_edge(UP)
        self.play(Write(determinant_text))
        # Separate notation, matrix, and formula, and arrange vertically
        det_notation = MathTex(r"\text{det}(A) =").set_color(BLUE)
        det_matrix = MathTex(r"\begin{vmatrix} a & b \\ c & d \end{vmatrix}").set_color(YELLOW)
        # Arrange notation and matrix horizontally, then formula below
        det_top_row = VGroup(det_notation, det_matrix).arrange(RIGHT, buff=0.2)
        det_formula = MathTex(r"= ad - bc").set_color(GREEN)
        det_group = VGroup(det_notation, det_matrix, det_formula).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        det_matrix.next_to(determinant_text, DOWN)
        self.play(Write(det_group))
        #draw two lines across the matrix
        self.wait(1)
        line = line_to_point = Line(
            det_matrix.get_left() + UP * 0.5,
            det_matrix.get_right() + DOWN * 0.5
        )
        line2 = Line(
            det_matrix.get_left() + DOWN * 0.5,
            det_matrix.get_right() + UP * 0.5
        )
        self.play(Create(line), Create(line2))
        self.wait(2)
        self.play(FadeOut(determinant_text), FadeOut(det_group), FadeOut(line), FadeOut(line2))

        ##############
        # determinant özellikleri
        #1.	🔁 Satır veya sütun yer değiştirirse, determinantın işareti değişir.
        #2.	🔄 Satır/sütunlardan biri diğerinin katıysa → determinant = 0  BURAYI DETAYLANDIR
        #3.	↔ Aynı satır/sütun iki kez varsa → determinant = 0
        #4.	🧊 Üçgensel ya da köşegen matrislerde → determinant = köşegenin çarpımı SIFIRLARDAN DOLAYI OLDUĞUNU DETAYLANDIR
        #5.	💥 Satır veya sütunlardan birine sabit sayı eklemek → determinantı değiştirmez.
        #6.	📐 det(AB) = det(A) * det(B)
        #7.	📎 det(Aᵗ) = det(A)