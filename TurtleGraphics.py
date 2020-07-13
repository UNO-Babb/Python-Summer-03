#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle

def drawSquare(myTurtle, size):
    count = 0
    while count < 4:
        myTurtle.forward(size)
        myTurtle.right(90)
        count = count + 1


def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
input("Hit enter to quit") #this keeps the turtle window from disapearing too soon.
