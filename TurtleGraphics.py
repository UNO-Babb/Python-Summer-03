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
    leo = turtle.Turtle()
    drawSquare(leo, 200)
    # drawPolygon(leo, 5) #draws a pentagon
    # drawPolygon(leo, 8) #draws an octogon

    # fillCorner(leo, 2) #draws a square with top right corner filled in.
    # fillCorner(leo, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(leo, 5) #draws 5 concentric squares
    # squaresInSquares(leo, 3) #draws 3 concentric squares


main()
