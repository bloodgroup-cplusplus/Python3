from manim import *
class Updaters(Scene):

        def construct(self):

                num = MathTex("ln(2)")
                box = SurroundingRectangle(num,color = BLUE, fill_opacity = 0.4, fill_color = RED, buff = 2)


                name = Tex("Anime").next_to(box, DOWN, buff = 0.25) # we want it to be pretty close


                self.play(Create(VGroup(num, box, name)))
