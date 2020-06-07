from manimlib.imports import *
import os

class Italian_coffe(SVGMobject):
    CONFIG = {
        "height": 1.5,
        "stroke_color": WHITE
        }

    index_names = {
        "button": (0,),
        "button_shadow": (1,),
        "top": (2,),
        "top_shadow": (3,),
        "handle": (4,),
        "pourer": (5,),
        "middle": (6,),
        "middle_shadow": (7,),
        "body": (8, 9),
        "body_shadow": (10, 11),
        "detail": (12, 13, 14),
        "detail_shadow": (15, 16, 17),
        
    }

    def __init__(self, **kwargs):
        svg_file = os.path.join(os.getcwd(), "assets", "italian_coffe.svg")
        SVGMobject.__init__(self, file_name = svg_file, **kwargs)

        self.set_colors()

    def set_colors(self, opacity = 1, stroke_color = "#b99b7d", stroke_opacity = 0, override = None):
        
        if override != None:
            self.set_fill(override, opacity = opacity)
            self.set_stroke(BLACK, opacity = 0)
            return None
        
        def flatten_index(*keys):
            indexes = []
            for k in keys:
                indexes += [*Italian_coffe.index_names[k]]
            return indexes

        for i in flatten_index("button_shadow", "handle", "detail_shadow", "middle_shadow"):
            self.submobjects[i].set_fill("#634b34", opacity = opacity)

        for i in flatten_index("button", "detail", "middle", "pourer"):
            self.submobjects[i].set_fill("#866748", opacity = opacity)

        for i in flatten_index("top"):
            self.submobjects[i].set_fill("#b99b7d", opacity = opacity)

        for i in flatten_index("top_shadow"):
            self.submobjects[i].set_fill("#af8a67", opacity = opacity)

        for i in flatten_index("body"):
            self.submobjects[i].set_fill("#f69a1f", opacity = opacity)

        for i in flatten_index("body_shadow"):
            self.submobjects[i].set_fill("#f5891b", opacity = opacity)


        self.set_stroke(color = stroke_color, opacity = stroke_opacity)


 


        
