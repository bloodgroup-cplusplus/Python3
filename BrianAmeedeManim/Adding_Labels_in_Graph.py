from manim import *

class Graphing(Scene):
        def construct(self):
                plane = (

                        NumberPlane(x_range = [-4,4,2], x_length = 7, y_range = [0,16,4], y_length = 5)

                        .to_edge(DOWN).add_coordinates()

                )


                labels = plane.get_axis_labels(x_label = "x", y_label =  "f(x)")



                parab = plane.get_graph ( lambda x: x**2, x_range=[-4,4], color = GREEN)


                func_lable = MathTex("f(x) = {x} ^ {2} ").scale(0.6).next_to(parab, RIGHT, buff = 0.5)


                self.play(DrawBorderThenFill(plane))


                self.play(Create(VGroup(labels, parab)))


                self.wait()
