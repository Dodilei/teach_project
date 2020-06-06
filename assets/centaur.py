from manimlib.imports import *
import os

class Centaur(SVGMobject):
    CONFIG = {
        "height": 3,
        "stroke_color": WHITE
        }

    index_names = {
        "ears": (0,1),
        "tail_light": (2),
        "tail_shadow": (3),
        "leg_back_lower": (4),
        "foot_back_shadow": (5),
        "body_horse": (6),
        "leg_front_shadow": (7,9),
        "leg_back_upper": (8),
        "midleg_shadow": (10),
        "body_top_shadow": (11),
        "body_man": (12),
        "nipple": (13, 14),
        "face_shadow": (15),
        "body_shadow": (16),
        "head": (17),
        "beard": (18),
        "eyes": (19, 20),
        "foot_front": (21, 22),
        "foot_back_upper": (23)
    }

    def __init__(self, **kwargs):
        svg_file = os.path.join(os.getcwd(), "assets", "centaur.svg")
        SVGMobject.__init__(self, file_name = svg_file, **kwargs)

        self.set_colors()

    def set_colors(self, opacity = 1, stroke_color = "#52232b", stroke_opacity = 0, override = None):
        
        if override != None:
            self.set_fill(override, opacity = opacity)
            self.set_stroke(BLACK, opacity = 0)
            return None
        
        def flatten_index(*keys):
            indexes = []
            for k in keys:
                indexes += [*Centaur.index_names[k]]
            return indexes

        for i in flatten_index("ears"):
            self.submobjects[i].set_fill("#df897c", opacity = opacity)

        for i in flatten_index("tail_light"):
            self.submobjects[i].set_fill("#f4c8b3", opacity = opacity)

        for i in flatten_index("tail_shadow"):
            self.submobjects[i].set_fill("#c8957e", opacity = opacity)

        for i in flatten_index("leg_back_lower"):
            self.submobjects[i].set_fill("#52232b", opacity = opacity)

        for i in flatten_index("foot_back_shadow", "eyes"):
            self.submobjects[i].set_fill("#333344", opacity = opacity)

        for i in flatten_index("body_horse"):
            self.submobjects[i].set_fill("#8a5455", opacity = opacity)

        for i in flatten_index("leg_front_shadow", "leg_back_upper", "midleg_shadow", "body_top_shadow"):
            self.submobjects[i].set_fill("#723e41", opacity = opacity)

        for i in flatten_index("beard"):
            self.submobjects[i].set_fill("#8a5455", opacity = opacity)

        for i in flatten_index("body_man", "head"):
            self.submobjects[i].set_fill("#efac9c", opacity = opacity)

        for i in flatten_index("nipple", "body_shadow", "face_shadow"):
            self.submobjects[i].set_fill("#df897c", opacity = opacity)

        for i in flatten_index("foot_front", "foot_back_upper"):
            self.submobjects[i].set_fill("#4d4d5e", opacity = opacity)


        self.set_stroke(color = stroke_color, opacity = stroke_opacity)


 


        
