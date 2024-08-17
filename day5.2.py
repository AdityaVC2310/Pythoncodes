import math

def trig_values():
    for angle in range(0, 345 + 1, 15):
        radian = math.radians(angle)
        sine = round(math.sin(radian), 3)
        cosine = round(math.cos(radian), 3)
        print(angle, sine, cosine)

# Example usage
trig_values()
