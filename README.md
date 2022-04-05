#### CS 110
# Chapter 5 - Lab - Selection

### [Assignment Description](https://docs.google.com/document/d/1QfPsRfo1kZoQw4p0DhjxZskNfE0eLAV6Z6SgPSleDM4/edit?usp=sharing)

***

_Replace anything surrounded by the `< >` symbols._

## SUMMARY:
The program simulates throwing darts at a dartboard
in order to approximate pi. Part A uses the drawSquare function, drawLine function, drawCircle function and setupDartboard function to setup the dartboard. throwDart function tests the code of throwing darts. Part B uses an accumulator and loop (playDarts function) to simulate a throwing dart game between two players. It also uses the throwDart function to change color depending on where the darts land on the board (green inside, red outside). Part C runs a Monte Carlo simulation (montePi function) to approximate pi with the provided formula. The isInCircle function returns a boolean value of the turtle is within the circle.   

## GRACE DAYS
Grace days used for this assignment: 0

Grace days remaining: 3/5

## KNOWN BUGS AND INCOMPLETE PARTS:
Part C prompt asking for user to input number of darts thrown in the simulation will sometimes not register number when the user types it. 

## REFERENCES:
https://www.w3schools.com/python/python_functions.asp
https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/Theforlooprevisited.html
https://www.educative.io/edpresso/multiline-comment-in-python
https://www.geeksforgeeks.org/draw-circle-in-python-using-turtle/

## MISCELLANEOUS COMMENTS:
Nothing of importance to note. 



#### CS 110
# Midterm - Python Programming

***

_Replace anything surrounded by the `< >` symbols._

## SUMMARY:
What did you clean up?: Cleaned up indentation errors and changed the original Lab 5 so that a 2x2 square is drawn for the setUpDartboard. Also removed space between functions to make code look more organized. Rearranged code so that the new feature is implemented as Part C and montePi is Part D. 

Summary of function(s) added: Added color_choice and target functions as Part C. color_choice function gives the selection of colors available to the user when prompted. target function draws four circles (in descending size order) which are filled in with the color asked from the program.  

Summary of Feature Added: Feature now shows a target with four rings (in descending size order). Each ring will be able to have their color filled from the color options of red, blue, green, yellow, or orange.  

## KNOWN BUGS AND INCOMPLETE PARTS:
Part C has issues filling in the desired color from the input for each circle. There were also issues with changing the target so it could fit within the window and it does not fully resemble a target.   

## REFERENCES:
https://docs.python.org/3/library/turtle.html#turtle.color
https://www.geeksforgeeks.org/turtle-fillcolor-function-in-python/

## MISCELLANEOUS COMMENTS:
Nothing of importance to note. 

