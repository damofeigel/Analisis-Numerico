from tkinter import X
import numpy as np
import math as m

import math
from ej1 import intenumcomp 

def senint(x):
    N = m.ceil(x / 0.1) + 1
    return intenumcomp(m.cos, 0, x, N, "punto medio")

