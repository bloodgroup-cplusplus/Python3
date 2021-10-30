from manim import *

class ValueTrackers(Scene):
        def construct(self):
                k = ValueTracker(3.5)   # argument can be changed to any number)

                # we are going to be animating a number 


                num = always_redraw(lambda:DecimalNumber().set_value(k.get_value())) # this is going to display a number 

                self.play(FadeIn(num))


                self.wait()

        #       self.play(k.animate.set_value(0), run_time =3 ) # atm the moment number is fixed without any updaters 

                # we need to add updaters to decimcal using always_redraw ( lambda: argument)
                # 

                # this pops up the decimal number 


                # go from 5 to zero in a linear fashion


                self.play(k.animate.set_value(0),run_time = 5, rate_func = linear)


                # this is going to follow a linear progression at a fixed rate

                # smooth will start of slower zoom through the end and end up slow
