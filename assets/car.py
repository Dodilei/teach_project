from manimlib.imports import *
import os

class Car(SVGMobject):
    CONFIG = {
        "height": 1.5,
        "stroke_color": WHITE
        }

    index_names = {
        "rear": (0,),
        "front": (1,),
        "bump": (2,),
        "tire_light": (3, 7),
        "tire_shadow": (4, 8),
        "wheel_light": (5, 9),
        "wheel_shadow": (6, 10),
        "windows": (11, 12),
        "light1": (13,),
        "light2": (14,)
        
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

        for i in flatten_index("rear", "bump"):
            self.submobjects[i].set_fill("#78b9eb", opacity = opacity)

        for i in flatten_index("front"):
            self.submobjects[i].set_fill("#5a8bb0", opacity = opacity)

        for i in flatten_index("tire_light"):
            self.submobjects[i].set_fill("#616064", opacity = opacity)

        for i in flatten_index("tire_shadow"):
            self.submobjects[i].set_fill("#565659", opacity = opacity)

        for i in flatten_index("wheel_light"):
            self.submobjects[i].set_fill("#cdcdd0", opacity = opacity)

        for i in flatten_index("wheel_shadow"):
            self.submobjects[i].set_fill("#acabb1", opacity = opacity)

        for i in flatten_index("windows"):
            self.submobjects[i].set_fill("#ffffff", opacity = opacity)

        for i in flatten_index("light1"):
            self.submobjects[i].set_fill("#ff5023", opacity = opacity)

        for i in flatten_index("light2"):
            self.submobjects[i].set_fill("#ff9811", opacity = opacity)



        self.set_stroke(color = stroke_color, opacity = stroke_opacity)


 


        
