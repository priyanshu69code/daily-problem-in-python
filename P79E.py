import math

def design_web_page(target_area):
    # calculate the initial value of L
    L = math.ceil(math.sqrt(target_area))
    
    # calculate the corresponding value of W
    W = target_area // L
    
    # swap L and W if necessary
    if W >= L:
        L, W = W, L
    
    return [L, W]

>>> design_web_page(120)
[12, 10]