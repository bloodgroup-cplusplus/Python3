from manim import *

class Testing(Scene):
        def construct(self):
                # create a whole bunch of stuff and move it around the scene


                name = Tex("Chad").to_edge(UL, buff = 0.5)

                sq = Square(side_length = 0.5,fill_color = GREEN, fill_opacity = 0.75).shift(LEFT*3)

                #create a triangle

                tri = Triangle().scale(0.6).scale(0.6).to_edge(DR) # scale it to 0.6 the size of itself

                # we haven't moved them it will move on the middle of the string



                # to move up left 

                #name = Tex("Name").to_edge(UL, buff =0.5)


                self.play(Write(name))
                self.play(DrawBorderThenFill(sq), run_time= 2)
                self.play(Create(tri))
                self.wait()


