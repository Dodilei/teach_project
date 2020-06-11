from manimlib.mobject.functions import ParametricFunction
import numpy as np

def interpolate(start, end, alpha):
    return start*(1 - alpha) + end*alpha

def make_path(
    func,
    color=WHITE,
    x_min=0,
    x_max=1,
    y_infinity = 10,
    **kwargs
    ):

    def parametric(alpha):
        
        x = interpolate(x_min, x_max, alpha)

        y = func(x)

        if not np.isfinite(y):
            y = y_infinity

        return (x, y)

    path = ParametricFunction(parametric, color = color, **kwargs)
    path.underlying_function = func

    return path
