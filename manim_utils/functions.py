from manimlib.mobject.functions import ParametricFunction
import numpy as np

def interpolate(start, end, alpha):
    return start*(1 - alpha) + end*alpha

def make_path(
    func,
    x_min=0,
    x_max=1,
    y_max = None,
    y_infinity = 10,
    color = "#ffffff",
    **kwargs
    ):

    

    def parametric(alpha = 1, override_x = None):
        
        if override_x == None:
          x = interpolate(x_min, x_max, alpha)
        else:
          x = override_x

        y = func(x)
    
        if not np.isfinite(y) or (y_max and y >= y_max):
            y = y_infinity

        return (x, y, 0)

    path = ParametricFunction(parametric, color = color, **kwargs)
    path.underlying_function = func

    path.para_func = parametric
    path.x_min = x_min
    path.x_max = x_max


    return path
