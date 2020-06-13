from manimlib.imports import *
import os

class Car(SVGMobject):
    CONFIG = {
        "height": 1.5,
        "stroke_color": WHITE
        }


    def __init__(self, **kwargs):
        svg_file = os.path.join(os.getcwd(), "assets", "car.svg")
        SVGMobject.__init__(self, file_name = svg_file, **kwargs)

        self.set_colors()

    def set_colors(self, opacity = 1, stroke_color = "#ddddff", stroke_opacity = 0, override = None):
        
        if override != None:
            self.set_fill(override, opacity = opacity)
            self.set_stroke(BLACK, opacity = 0)
            return None
        
        def flatten_index(*keys):
            indexes = []
            for k in keys:
                indexes += [*Car.index_names[k]]
            return indexes
        
        self.set_color(WHITE)

        self.set_stroke(color = stroke_color, opacity = stroke_opacity)


 


        
