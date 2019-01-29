
def primary_color(color1 , color2):
    if color1 == "red" and color2 == "blue":
        return "purple"
    elif color1 == "blue" and color2 == "red":
        return "purple"
    elif color1 == "red" and color2 == "yellow":
        return "orange"
    elif color1 == "yellow" and color2 == "red":
        return "orange"
    elif color1 == "yellow" and color2 == "blue":
        return "green"
    elif color1 == "blue" and color2 == "yellow":
        return "green"
    elif color1 == color2:
        return "Your chosen colors must be different"
    else:
        return "Your chosen colors must be primary colors (red,blue,yellow)"

def color_mixer():
    first_color = input("input your first color: ").strip()
    second_color = input("input your second color: ").strip()
    return primary_color(first_color.lower(),second_color.lower())

print(color_mixer())


