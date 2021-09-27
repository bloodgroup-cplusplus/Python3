from manim import *
import math 
import numpy as np

class Arc(MovingCameraScene):
  def construct(self):
    arc = Arc(color = RED, stroke_width = 30, radius = 3, angle = math.radians(180),start_angle = math.radians(90),arc_center= [2,0,0])
    self.play(Create(arc))
    
