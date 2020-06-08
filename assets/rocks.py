from manimlib.imports import *
import os


def create_rock_field(n, h, w, s, pos_set = [1,1], size_set=1, width_ratio=1):
    
    nums_init = np.random.rand(n, 4)
    nums_init[:, 1:4] += -0.5
    nums_init[:, -1] = 0
    nums_init[:, 0] = np.abs(nums_init[:, 0])
    nums_init[:, 0] += size_set
    nums_init[:, 0] = nums_init[:, 0]/((size_set+1)/s)
    
    rocks = VGroup(unpack_groups = False)
    
    rocks_to_sort = []
    for x in nums_init:
        rock_type = int(np.ceil(np.random.rand()*5))
        rock = ImageMobject("assets/rock{}.png".format(rock_type), height=x[0])
        rock.move_to(x[1:]*np.array((w,h,1)))
        
        rocks_to_sort.append(rock)
        
        
    rocks_to_sort.sort(reverse = True, key= lambda x: x.get_center()[1])
        
    rocks.add(*rocks_to_sort)
        
    for rock1 in rocks:
        for rock2 in rocks:
            if rock1==rock2: continue
                
            center_dif = np.abs(rock1.get_center() - rock2.get_center())
            
            height_dist = (rock1.height + rock2.height)/(2*pos_set[0])
            width_dist = (rock1.height + rock2.height)/((1/width_ratio)*2*pos_set[1])
            
            min_dist = np.abs(np.array([height_dist, width_dist, 0]))
                              
            if (center_dif <= min_dist).all():
                rocks.remove(rock1)
    
    return rocks




        
