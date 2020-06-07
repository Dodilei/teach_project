from manimlib.imports import *
import os


def c_adder(color1, color2, return_as_string=True):
	
    if type(color1) == str:
        color1 = int("0x"+color1[1:], 16)

    if type(color2) == str:
        color2 = int("0x"+color2[1:], 16)

    added = hex(int(color1) + int(color2))
	
    if return_as_string: 
        return ("#" + str(added)[2:])
    else:
        return added

class Llama(SVGMobject):
    CONFIG = {
        "height": 3,
        "stroke_color": WHITE
        }

    index_names = {
        "foot_back": (1, 4),
        "foot_front": (7, 10),
        "legs_front_upper": (8, 11),
        "legs_back_upper": (2, 5),
        "legs_front_lower": (6, 9),
        "legs_back_lower": (0,3),
        "body": 12,
        "head": 14,
        "nose": 13,
        "eye": 15,
        "ear": 16,
    }

    @staticmethod
    def create_llama_herd(n, h, w, s, pos_set = [1,1], size_set=1, width_ratio=7/9):
        
        nums_init = np.random.rand(n, 4)
        nums_init[:, 1:4] += -0.5
        nums_init[:, -1] = 0
        nums_init[:, 0] = np.abs(nums_init[:, 0])
        nums_init[:, 0] += size_set
        nums_init[:, 0] = nums_init[:, 0]/((size_set+1)/s)
        
        llamas = VGroup(unpack_groups = False)
        
        llamas_to_sort = []
        for x in nums_init:
            llama_body = Llama(height=x[0], stroke_width = 2.7)
            llama_body.move_to(x[1:]*np.array((w,h,1)))
            
            shadow = llama_body.copy()
            shadow.set_height(shadow.height * 1.1)
            shadow.set_colors(override = BLACK, opacity = 0.2)
            shadow.shift(UP*0.03 + LEFT*0.1)
            
            llama = VGroup(shadow, llama_body)
            llamas_to_sort.append(llama)
            
            
        llamas_to_sort.sort(reverse = True, key= lambda x: x.get_center()[1])
        
        for _, llama in llamas_to_sort:
            llama.set_colors(main = c_adder(llama.main_color, -0x101010*(3/h)*(llama.get_center()[1].astype(np.int64))),
                        stroke_color = BLACK)
            
            
        llamas.add(*llamas_to_sort)
            
        for group in llamas:
            _, llama1 = group
            for group2 in llamas:
                _, llama2 = group
                if llama1==llama2: continue
                    
                center_dif = np.abs(llama.get_center() - llama2.get_center())
                
                height_dist = (llama.height + llama2.height)/(2*pos_set[0])
                width_dist = (llama.height + llama2.height)/((1/width_ratio)*2*pos_set[1])
                
                min_dist = np.abs(np.array([height_dist, width_dist, 0]))
                                  
                if (center_dif <= min_dist).all():
                    llamas.remove(sub1)
        
        return llamas

    def __init__(self, **kwargs):
        svg_file = os.path.join(os.getcwd(), "assets", "llama.svg")
        SVGMobject.__init__(self, file_name = svg_file, **kwargs)

        self.main_color = "#dbdbdb"
        self.set_colors()

    def set_colors(self, opacity = 1, main = "main_color", add_shadow = -0x161616, to_dark = -0x6e645a, to_light = 0x101010, stroke_color = "default", override = None):
        
        if override != None:
            self.set_fill(override, opacity = opacity)
            self.set_stroke(BLACK, opacity = 0)
            return None

        if main == "main_color":
            main = self.main_color

        if stroke_color == "default":
            stroke_color = main

        darker = c_adder(main, to_dark)
        lighter = c_adder(main, to_light)
        
        for i in Llama.index_names["foot_back"]:
            self.submobjects[i].set_fill(c_adder(darker, add_shadow*3), opacity = opacity)

        for i in Llama.index_names["foot_front"]:
            self.submobjects[i].set_fill(c_adder(darker, add_shadow*2), opacity = opacity)

        for i in Llama.index_names["legs_front_lower"]:
            self.submobjects[i].set_fill(darker, opacity = opacity)

        for i in Llama.index_names["legs_back_lower"]:
            self.submobjects[i].set_fill(c_adder(darker, add_shadow), opacity = opacity)

        for i in Llama.index_names["legs_front_upper"]:
            self.submobjects[i].set_fill(main, opacity = opacity)

        for i in Llama.index_names["legs_back_upper"]:
            self.submobjects[i].set_fill(c_adder(main, add_shadow), opacity = opacity)

        self.submobjects[Llama.index_names["body"]].set_fill(main, opacity = opacity)
        self.submobjects[Llama.index_names["ear"]].set_fill(main, opacity = opacity)
        self.submobjects[Llama.index_names["head"]].set_fill(darker, opacity = opacity)
        self.submobjects[Llama.index_names["nose"]].set_fill(c_adder(darker, add_shadow*3), opacity = opacity)
        self.submobjects[Llama.index_names["eye"]].set_fill(c_adder(darker, add_shadow*4), opacity = opacity)
        self.set_stroke(color = stroke_color, opacity = opacity)


 


        
