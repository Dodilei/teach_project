from manimlib.imports import *
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
        
		

