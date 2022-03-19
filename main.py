'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################
def drawSquare(darty=None, width=0, top_left_x=0, top_left_y=0):
  darty.up()
  darty.goto(top_left_x, top_left_y)
  for i in range(4):
    darty.down()
    darty.forward(width)
    darty.right(90) 
  
def drawLine(darty=None, x_start=0, y_start=0, x_end=0, y_end=0):
  darty.up()
  darty.goto(x_start,y_start)
  darty.down()
  darty.goto(x_end,y_end)
  
def drawCircle(darty=None, radius=0):
   darty.up()
   darty.goto(0, -1)
   darty.down()
   darty.circle(radius)
  
def setUpDartboard(myscreen=None, darty=None):
  myscreen.setworldcoordinates(-1.5,-1.5,1.5,1.5)
  drawSquare(darty,2,-1,1)
  drawLine(darty,0,-1,0,1)
  drawLine(darty,-1,0,1,0)
  drawCircle(darty,1)
  return setUpDartboard
  
def isInCircle(darty=None, circle_center_x=0, circle_center_y=0, radius=0):
  return darty.distance(0,0)<=1
  return isInCircle
  
def throwDart(darty=None):
  darty.up()
  x=random.uniform(-1,1)
  y=random.uniform(-1,1)
  darty.goto(x,y)
  darty.dot()
  if isInCircle(darty):
    darty.dot("green")
    return True
  else:
    darty.dot("red")
    return False
  return throwDart
  
def playDarts(darty=None):
  player1=0
  player2=0
  for i in range(10):
    throwDart(darty)
    if isInCircle(darty):
      player1 += 1 
  for i in range(10):
    throwDart(darty)
    if isInCircle(darty):
      player2 += 1
  if player1>player2:
    print("Player 1 has won the game!")
  elif player2>player1:
    print("Player 2 has won the game!")
  else:
    print("Tie Game")
  return playDarts
  
def montePi(darty=None, number_darts=0):
  inside_count=0
  for i in range(number_darts):
    throwDart(darty)
    if isInCircle(darty):
          inside_count +=1
  pi=(inside_count/number_darts)*4
  return pi
  return montePi


#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main provided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
