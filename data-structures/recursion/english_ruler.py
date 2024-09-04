

def draw_line(length = 1, marking = ''):
    print("|"+"-"*length + f"  {marking}")


def draw_interval(length, mark, num):
    if length > 0: 
        draw_interval(length - 1, mark/2, num)
        draw_line(length, str(num + mark/2))
        draw_interval(length - 1, mark/2, num)


def draw_ruler(length, resolution = 2): 
    draw_line(resolution + 1, marking = str(0))
    for i in range(length):
        draw_interval(resolution, 1, i)  
        draw_line(resolution + 1, marking = str(i + 1))

# TEST: 
# draw_line(4)  
# draw_line(3)  
# draw_interval(3, 1)  
draw_ruler(3, 3)