from manim import *


class Library(Scene):

        def construct(self):

                # manim library 
                # is created by the engineers

                # they can figure the axes 

                # they can create all the stuffs and it is up on the screen


                # it is a good idea to be able to read it and be aware


                # stuff that we see

                # couple of main ones


                # 3d axis requires a 3d scene


                # class of a number lane



                # whenever we call this it can have an illusion



                # we can call whole bunch of stuffs



                # we could get a graph label


                #reimann rectangles is the area under the curve


                # it is there to be able to read 


                # there is a width color and opacity


                # it is super important to read the documentation


                # what are getters in manim


                rect = Rectangle(color = WHITE, height = 3, width = 2.5).to_edge(UL)

                circ = Circle().to_edge(DOWN) # to the bottom of the screen

                # put arrow from the rectangle to the circle

                arrow = Line(start = rect.get_bottom(),end = circ.get_top(),buff = 0.2).add_tip()


                self.play(Create(VGroup(rect,circ,arrow)))


                self.wait()


                self.play(rect.animate.to_edge(UR))
