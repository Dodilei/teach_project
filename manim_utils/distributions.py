from manimlib.imports import *
import os


def random(model, n, h, w, dist_set = [1,1], width_ratio=1, is3d = False):
    
    nums_init = np.random.rand(n, 3)
    nums_init -= 0.5
    if not is3d:
        nums_init[:, -1] = 0

    items = VGroup(unpack_groups = False)
    
    items_to_sort = []
    for x in nums_init:
        item = model.copy()
        item.move_to(x[1:]*np.array((w,h,1)))
        
        items_to_sort.append(item)
        
        
    items_to_sort.sort(reverse = True, key= lambda x: x.get_center()[1])
        
    items.add(*items_to_sort)
        
    for item1 in items:
        for item2 in items:
            if item1==item2: continue
                
            center_dif = np.abs(item1.get_center() - item2.get_center())
            
            height_dist = (item1.height + item2.height)/(2*dist_set[0])
            width_dist = (item1.height + item2.height)/((1/width_ratio)*2*dist_set[1])
            
            min_dist = np.abs(np.array([height_dist, width_dist, 0]))
                              
            if (center_dif <= min_dist).all():
                items.remove(rock1)
    
    return items




        
