from manimlib.imports import *
from assets.drawings import ThoughtBubble
import os

class Sheperd(SVGMobject):
    CONFIG = {
        "height": 3,
        "stroke_color": WHITE
        }

    def __init__(self, mode = None, **kwargs):
        if mode == None:
            default_file = "sheperd"
        else:
            default_file = "sheperd_" + mode
        svg_file = os.path.join(os.getcwd(), "assets", default_file + ".svg")
        SVGMobject.__init__(self, file_name = svg_file, **kwargs)
        
        self.set_color_()

    def think(self):
        rect = Rectangle(width = self.height*0.3, height = self.height, fill_color = BLACK, fill_opacity=1, stroke_opacity=0)
        rect.move_to(self.get_center())
        thinking = Sheperd(mode = "thinking", height=self.height)
        thinking.set_style(**self.get_style())
        thinking.set_color_()
        thinking.move_to(self.get_center())
        thinking.remove(thinking[-1])
        last = self
        self = thinking

        bubble = ThoughtBubble(height = 1.2, width = 1.2, stroke_color = GRAY, FILE_DIR = "/home/mauricio/anaconda3/envs/manim/lib/python3.7/site-packages/manimlib/files/")
        #bubble.set_color(WHITE)
        bubble.move_to(self.get_center() + UP*1.8 + RIGHT*1)
        text = TextMobject("?", color = WHITE)
        bubble.add_content(text)
        
        rotate_center = last[-1].get_center()+(RIGHT*0.6+UP*0.2)*last.height*0.3
        angle = -np.pi/4
    
        return (bubble, FadeOut(last), FadeIn(rect), FadeIn(self), Rotate(last[-1], angle, about_point=rotate_center), Rotate(last[-2], angle, about_point=rotate_center), FadeIn(bubble), FadeIn(text))

    def set_color_(self, override = False):
    
        if override:
            self.set_fill(override)
            self.set_stroke(color = override, width = self.stroke_width+1)
            return None
    
        self[0].set_fill("#d57454").set_stroke(width = 1)
        self[5].set_fill("#d57454").set_stroke(width = 1)
        self[3].set_fill("#d57454").set_stroke(width = 1)
        
        self[1].set_fill("#ad4d2f")
        self[1].set_stroke("#cd6d4f")
        
        self[2].set_fill("#3c1515")
        self[4].set_fill("#3c1515")
        self[6].set_fill("#3c1515")
        self[2].set_stroke("#ac8585")
        self[4].set_stroke("#ac8585")
        self[6].set_stroke("#ac8585")



class Old_sheperd(SVGMobject):
    CONFIG = {
        "height": 3,
        "stroke_color": WHITE
        }

    index_names = {
        "hand": (0, 3, 14),
        "arm_back": (1,),
        "staff": (2,),
        "leg": (4, 5),
        "foot": (6, 7),
        "body": (8,),
        "head": (9, 10),
        "eye": (11,),
        "eyelid": (12,),
        "hat": (13,),
        "arm_front_stroke": (15,),
        "arm_front": (16, ),
        "beard": (17,),
        "mouth": (18,),
    }

    def __init__(self, mode = None, **kwargs):
        if mode == None:
            default_file = "sheperd_old"
        else:
            default_file = "sheperd_old_" + mode
        svg_file = os.path.join(os.getcwd(), "assets", default_file + ".svg")
        SVGMobject.__init__(self, file_name = svg_file, **kwargs)
        
        self.set_colors()
        self.set_strokes()

    def think(self):
        
        thinking = Old_sheperd(mode = "thinking", height=self.height)
        thinking.move_to(self.get_center())
        last = self
        self = thinking

        bubble = ThoughtBubble(height = 1.2, width = 1.2, stroke_color = GRAY)
        #bubble.set_color(WHITE)
        bubble.move_to(self.get_center() + UP*1.8 + RIGHT*1)
        text = TextMobject("?", color = WHITE)
        bubble.add_content(text)

        return (bubble, ReplacementTransform(last, self), FadeIn(bubble), FadeIn(text))

    def set_colors(self, opacity = 1, stroke_color = BLACK, stroke_opacity = 0, override = None):
        
        if override != None:
            self.set_fill(override, opacity = opacity)
            self.set_stroke(BLACK, opacity = 0)
            return None
        
        def flatten_index(*keys):
            indexes = []
            for k in keys:
                indexes += [*Old_sheperd.index_names[k]]
            return indexes

        for i in flatten_index("hand", "head", "leg", "eyelid"):
            self.submobjects[i].set_fill("#e9d2aa", opacity = opacity)

        for i in flatten_index("arm_back", "body", "arm_front"):
            self.submobjects[i].set_fill("#d3c27c", opacity = opacity)

        for i in flatten_index("arm_front_stroke"):
            self.submobjects[i].set_fill(BLACK, opacity = 0)

        for i in flatten_index("staff"):
            self.submobjects[i].set_fill("#91703b", opacity = opacity)

        for i in flatten_index("foot"):
            self.submobjects[i].set_fill("#45392e", opacity = opacity)

        for i in flatten_index("eye", "mouth"):
            self.submobjects[i].set_fill(BLACK, opacity = opacity)

        for i in flatten_index("hat"):
            self.submobjects[i].set_fill("#612c3a", opacity = opacity)

        for i in flatten_index("beard"):
            self.submobjects[i].set_fill(WHITE, opacity = opacity)

        self.set_stroke(color = stroke_color, opacity = stroke_opacity)

        return self


    def set_strokes(self, color = BLACK, opacity = 1, width = 2.5, override = None):
        
        if override != None:
            self.set_stroke(override, opacity = opacity)
            return None
        
        def flatten_index(*keys):
            indexes = []
            for k in keys:
                indexes += [*Old_sheperd.index_names[k]]
            return indexes

        for i in flatten_index("hand", "head", "leg", "eyelid"):
            self.submobjects[i].set_stroke(color = color, opacity = opacity, width = width)

        for i in flatten_index("arm_back", "body", "arm_front_stroke"):
            self.submobjects[i].set_stroke(color = color, opacity = opacity, width = width)

        for i in flatten_index("arm_front"):
            self.submobjects[i].set_stroke(color = color, opacity = 0, width = width)

        for i in flatten_index("staff", "hat"):
            self.submobjects[i].set_stroke(color = color, opacity = opacity, width = width)

        for i in flatten_index("foot"):
            self.submobjects[i].set_stroke(color = color, opacity = opacity, width = width)

        for i in flatten_index("eye", "mouth"):
            self.submobjects[i].set_stroke(color = color, opacity = 0, width = width)

        for i in flatten_index("beard"):
            self.submobjects[i].set_stroke(color = color, opacity = opacity, width = width)


        return self
		
        
		

