import itertools as it
import string

from manimlib.animation.animation import Animation
from manimlib.animation.rotation import Rotating
from manimlib.constants import *
from manimlib.mobject.geometry import AnnularSector
from manimlib.mobject.geometry import Arc
from manimlib.mobject.geometry import Circle
from manimlib.mobject.geometry import Line
from manimlib.mobject.geometry import Polygon
from manimlib.mobject.geometry import Rectangle
from manimlib.mobject.geometry import Square
from manimlib.mobject.mobject import Mobject
from manimlib.mobject.svg.svg_mobject import SVGMobject
from manimlib.mobject.svg.tex_mobject import TexMobject
from manimlib.mobject.svg.tex_mobject import TextMobject
from manimlib.mobject.three_dimensions import Cube
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.types.vectorized_mobject import VMobject
from manimlib.mobject.types.vectorized_mobject import VectorizedPoint
from manimlib.utils.bezier import interpolate
from manimlib.utils.config_ops import digest_config
from manimlib.utils.rate_functions import linear
from manimlib.utils.space_ops import angle_of_vector
from manimlib.utils.space_ops import complex_to_R3
from manimlib.utils.space_ops import rotate_vector


class Bubble(SVGMobject):
    CONFIG = {
        "direction": LEFT,
        "center_point": ORIGIN,
        "content_scale_factor": 0.75,
        "height": 5,
        "width": 8,
        "bubble_center_adjustment_factor": 1. / 8,
        "file_name": None,
        "fill_color": BLACK,
        "fill_opacity": 0.8,
        "stroke_color": WHITE,
        "stroke_width": 3,
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs, locals())
        if self.file_name is None:
            raise Exception("Must invoke Bubble subclass")
        
        self.file_name = os.path.join("assets", self.file_name)
        SVGMobject.__init__(self, **kwargs)

        self.center()
        self.stretch_to_fit_height(self.height)
        self.stretch_to_fit_width(self.width)
        if self.direction[0] > 0:
            self.flip()
        self.direction_was_specified = ("direction" in kwargs)
        self.content = Mobject()

    def get_tip(self):
        # TODO, find a better way
        return self.get_corner(DOWN + self.direction) - 0.6 * self.direction

    def get_bubble_center(self):
        factor = self.bubble_center_adjustment_factor
        return self.get_center() + factor * self.get_height() * UP

    def move_tip_to(self, point):
        mover = VGroup(self)
        if self.content is not None:
            mover.add(self.content)
        mover.shift(point - self.get_tip())
        return self

    def flip(self, axis=UP):
        Mobject.flip(self, axis=axis)
        if abs(axis[1]) > 0:
            self.direction = -np.array(self.direction)
        return self

    def pin_to(self, mobject):
        mob_center = mobject.get_center()
        want_to_flip = np.sign(mob_center[0]) != np.sign(self.direction[0])
        can_flip = not self.direction_was_specified
        if want_to_flip and can_flip:
            self.flip()
        boundary_point = mobject.get_critical_point(UP - self.direction)
        vector_from_center = 1.0 * (boundary_point - mob_center)
        self.move_tip_to(mob_center + vector_from_center)
        return self

    def position_mobject_inside(self, mobject):
        scaled_width = self.content_scale_factor * self.get_width()
        if mobject.get_width() > scaled_width:
            mobject.set_width(scaled_width)
        mobject.shift(
            self.get_bubble_center() - mobject.get_center()
        )
        return mobject

    def add_content(self, mobject):
        self.position_mobject_inside(mobject)
        self.content = mobject
        return self.content

    def write(self, *text):
        self.add_content(TextMobject(*text))
        return self

    def resize_to_content(self):
        target_width = self.content.get_width()
        target_width += max(MED_LARGE_BUFF, 2)
        target_height = self.content.get_height()
        target_height += 2.5 * LARGE_BUFF
        tip_point = self.get_tip()
        self.stretch_to_fit_width(target_width)
        self.stretch_to_fit_height(target_height)
        self.move_tip_to(tip_point)
        self.position_mobject_inside(self.content)

    def clear(self):
        self.add_content(VMobject())
        return self


class SpeechBubble(Bubble):
    CONFIG = {
        "file_name": "Bubbles_speech.svg",
        "height": 4
    }


class DoubleSpeechBubble(Bubble):
    CONFIG = {
        "file_name": "Bubbles_double_speech.svg",
        "height": 4
    }


class ThoughtBubble(Bubble):
    CONFIG = {
        "file_name": "Bubbles_thought.svg",
    }

    def __init__(self, **kwargs):
        Bubble.__init__(self, **kwargs)
        self.submobjects.sort(
            key=lambda m: m.get_bottom()[1]
        )

    def make_green_screen(self):
        self.submobjects[-1].set_fill(GREEN_SCREEN, opacity=1)
        return self




