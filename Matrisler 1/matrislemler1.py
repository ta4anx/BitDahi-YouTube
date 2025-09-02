from manim import *
class MatrisIslemleri(Scene):
    def construct(self):
        # Matrislerle topama - çıkarma işlemleri
        # First, show thew plus and minus signs
        plus = Tex("+")
        minus = Tex("-")
        plus.scale(4)
        minus.scale(4)
        plus.set_color(BLUE)
        minus.set_color(TEAL)
        plus.move_to(LEFT * 3)
        minus.move_to(RIGHT * 3)
        self.play(Write(plus),running_time=0.2)
        self.play(Write(minus),running_time=0.2)
        self.wait(1)
        self.play(Indicate(plus),run_time=0.7)
        self.wait(0.5)
        self.play(Indicate(minus),run_time=0.7)
        self.wait(1)
        self.play(FadeOut(plus), FadeOut(minus))
        # Now show the two matrices of only dots and the addition and subtraction signs
        dot = r"\cdot"
        matrix1 = Matrix([[dot, dot], [dot, dot]], element_to_mobject_config={"color": BLUE})
        matrix2 = Matrix([[dot, dot], [dot, dot]], element_to_mobject_config={"color": TEAL})

        matrix1.move_to(LEFT * 2)
        matrix2.move_to(RIGHT * 2)
        plus = Tex("+")
        minus = Tex("-")
        plus.scale(2.5)
        minus.scale(2.5)
        plus.set_color(BLUE)
        minus.set_color(TEAL)
        self.play(Write(matrix1), run_time=0.5)
        self.play(Write(matrix2), run_time=0.5)
        self.play(Write(plus), run_time=0.5)
        self.wait(1)
        self.play(Transform(plus, minus), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(matrix1), FadeOut(matrix2), FadeOut(plus), FadeOut(minus))
        # Now the academical definition of addition and subtraction
        #Akademik Tanım: Boyutları aynı olan iki matris A=[aij] ve B=[bij] olsun. Bu durumda, matris toplamı A+B ve matris farkı A−B aşağıdaki şekilde tanımlanır:
        #•	A+B=[aij+bij]
        #•	A−B=[aij−bij]
        definition = Title("Akademik Tanım:", font_size=36)
        definition.set_color(YELLOW)
        definition.to_edge(UP)
        self.play(Write(definition))
        self.wait(1)
        deftext = Tex(
            r"Boyutları aynı olan iki matris $A=[a_{ij}]$ ve $B=[b_{ij}]$ olsun. Bu durumda, matris toplamı $A+B$ ve matris farkı $A-B$ aşağıdaki şekilde tanımlanır:",
            font_size=36
        )
        deftext.set_color(WHITE)
        deftext.next_to(definition, DOWN, buff=0.5)
        self.play(Write(deftext), run_time=2)
        self.wait(1)
        
        #A+B=[aij+bij]
        addition = MathTex(r"A + B = [a_{ij} + b_{ij}]")
        addition.set_color(BLUE)
        addition.next_to(deftext, DOWN, buff=0.5)
        self.play(Write(addition), run_time=2)
        self.wait(1)
        #A−B=[aij−bij]
        subtraction = MathTex(r"A - B = [a_{ij} - b_{ij}]")
        subtraction.set_color(TEAL)
        subtraction.next_to(addition, DOWN, buff=0.5)
        self.play(Write(subtraction), run_time=2)
        self.wait(1)
        # Fade out all the text
        self.play(
            FadeOut(definition),
            FadeOut(deftext),
            FadeOut(addition),
            FadeOut(subtraction)
        )


        
