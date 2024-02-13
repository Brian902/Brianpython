import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")

love = turtle.Turtle()
love.shape("turtle")
love.color("red")
love.speed(2)

# Draw the heart shape
love.begin_fill()
love.fillcolor("red")
love.left(50)
love.forward(133)
love.circle(50, 200)
love.right(140)
love.circle(50, 200)
love.forward(133)
love.end_fill()

# Hide the turtle
love.hideturtle()

# Keep the window open
turtle.mainloop()
