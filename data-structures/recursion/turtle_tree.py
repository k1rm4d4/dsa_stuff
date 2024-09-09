import turtle
import random 

# def draw_leaf(size, t): 
#     # t.down()
#     orignal = t.xcor()
#     print(orignal, type(orignal))
#     print(int(orignal), type(orignal))
    
#     t.right(45)
#     t.forward(size/5)
#     print("Orignal: ",(t.xcor(), t.ycor()) )
#     print((t.xcor(), t.ycor()))
    
#     # while int(t.xcor()) != int(orignal):
#     #     t.forward(size/2)
#     #     t.left(10)
#     #     print(t.xcor(), t.ycor())
#     #     print(int(t.xcor()), int(t.ycor()))   
#     for _ in range(5):
#         t.forward(size)
#         t.left(20)

#     t.left(90)
#     for _ in range(5):
#         t.forward(size)
#         t.left(20)
#     # done
#     # t.up()


def tree(branch_len, t):
    if branch_len > 75 and branch_len < 50: 
        t.pencolor("#087000")
    elif branch_len > 50 and branch_len < 75: 
        t.pencolor("#6e4300")
    elif branch_len > 25 and branch_len < 50: 
        t.pencolor("#994f00")
    elif branch_len > 5 and branch_len < 25: 
        t.pencolor("#ca9a6f")

    len_subtr = random.randrange(start=5, stop=20, step=2)
    # len_subtr = 15
    angle = random.randrange(start=10, stop=50, step=5)
    # angle = 20
    if branch_len > 5:
        t.width((branch_len/50 * 5))
        t.forward(branch_len)
        
        # angle = random.randrange(start=10, stop=40, step=5)
        t.right(angle)
        tree(branch_len - len_subtr, t)

        # angle = random.randrange(start=40, stop=90, step=5)
        t.left(2*angle)
        tree(branch_len - len_subtr, t)
        
        # angle = random.randrange(start=10, stop=40, step=5)
        t.right(angle)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.speed(9)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.width(5)

    tree(100, t)
    my_win.exitonclick()

main()