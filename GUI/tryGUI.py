from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

def func(x):
    return x

w = widgets.IntSlider()
display(w)