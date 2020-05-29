from manimlib.imports import *
import math as mt


class Light(VGroup):
    CONFIG = {
        "stroke_width": 0,
        "stroke_opacity": 0,
        "color": WHITE
    }

    def __init__(self, radius = 1, n = 100, y_func = lambda x: 2*(x**(4)), color = WHITE, **kwargs):
        VGroup.__init__(self, **kwargs)
        
        self.color = color
        self.radius = radius
        self.n = n
        self.y = y_func

        for i in range(0,n):
            x = i/n
            self.add(Circle(stroke_opacity = 0, radius = i/(n/radius), fill_color = self.color, fill_opacity = 2*mt.ceil(100*(self.y(x)*(1/n)))/100))
        
