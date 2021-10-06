from manim import *
class Vectors(VectorScene):


        def construct(self):
                code = (

                        Code(
                                "create_arc.py",
                                style = Code.styles_list[12],
                                background = "window",
                                language = "python",
                                insert_line_no = True,
                                tab_width = 2,
                                line_spacing = 0.3,
                                font = "Monospace",

                        )
                        .set_width(10)
                        .set_height(2)

                )
                self.play(Write(code),run_time=6)
                self.wait()
