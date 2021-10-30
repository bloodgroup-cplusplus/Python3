rom manim import *

class Graphing(Scene):
        def construct(self):
                # add a plane or an axis

                plane = NumberPlane(x_range = [-4, 4, 2], x_length = 7, y_range = [0,16,4], y_length = 8 ).to_edge(DOWN).add_coordinates()


 # start point,end point and step


                #parab = # name of the plane.get graph

                parab = plane.get_graph( lambda x : x**2, x_range = [-4, 4] , color = GREEN)


                self.play(DrawBorderThenFill(plane))
                self.play(Create(parab))

                self.wait()
