import turtle

t = turtle.Turtle()
my_win = turtle.Screen()

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

t.left(90)
t.up()
t.backward(200)
t.down()
t.color("black")
tree(110, t)
my_win.exitonclick()