import random

def randomColor():
    """Returns a random color string."""
    color = "#"
    colorString ="0123456789ABCDEF"
    for anyColor in range(6):
     randColor = random.randrange(0,len(colorString))
     color+=f"{colorString[randColor]}"
    print(f"RandomColor: {color}")
    return color 