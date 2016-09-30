from graphics import *

w1 = GraphWin("My first window!", 200, 200)

w1.getWidth()
w1.getHeight()

w2 = GraphWin("My second  window!", 300, 100)

w1.getWidth()
w2.getWidth()

w2.close()

w1.getMouse()

p = Point(10, 50) # Create a new Point object.
p.getX()          # Extract the X-value. 
p.getY()          # Extract the Y-value.

p = w1.getMouse()
p.getX()
p.getY()

w3 = GraphWin("Change my background", 300, 100)

w3.setBackground("blue")
w3.getMouse()
w3.setBackground("yellow")
w3.getMouse()
w3.setBackground("#FFC0CB")

w4 = GraphWin("Shapes", 300, 100)

cp = Point(100, 50)
c = Circle(cp, 25)
c.setFill("red")
c.draw(w4)

w4.getMouse()

c.setFill("blue")
c.setWidth(10)
c.move(100,0)

w4.getMouse()

r = Rectangle(Point(25, 25), Point(75, 75))
r.setFill("red")
r.setWidth(10)
r.draw(w4)

w4.getMouse()

r.move(10, 10)

w4.getMouse()

l = Line(r.getCenter(), c.getCenter())
l.setWidth(5)
l.draw(w4)

w4.getMouse()


l.setArrow("last")

w4.getMouse()



w5 = GraphWin("Input text", 300, 100)
e = Entry(Point(150, 50), 20) # An input field, width 20 characters.
e.draw(w5)

w5.getMouse()
print "Text: " + e.getText()

print "Press any key ..."

print "Key pressed: %s" %  w5.getKey()


