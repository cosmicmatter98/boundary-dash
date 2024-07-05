# Boundary-Dash
# a game where you have to move a square, the protagonist - you, around
# a green 'field' without hitting the red boundary walls.
# if you hit the wall, it's GAME OVER


from graphics import *

def main():
	'''creating the game window'''
	win = GraphWin("Game", 400, 400)
	
	'''setting the background to green'''
	win.setBackground("green")
	
	'''coordinate transformation'''
	win.setCoords(0, 0, 100, 100)
	
	'''creating boundary wall'''
	wall = Polygon(Point(0, 0), Point(1, 0), Point(1, 99), Point(99, 99), Point(99, 0), Point(100, 0), Point(100, 100), Point(0, 100))
	wall.draw(win)
	wall.setOutline("red")
	wall.setFill("red")
	
	'''bottom boundary'''
	bottom_bound = Rectangle(Point(1, 0), Point(99, 1))
	bottom_bound.draw(win)
	bottom_bound.setOutline("red")
	bottom_bound.setFill("red")
	
	'''creating the player object which is a rectangle'''
	character = Rectangle(Point(49, 74), Point(51, 76))
	character.draw(win)
	character.setOutline("yellow")
	character.setFill("yellow")
	
	'''taking a mouse input'''
	msg = Text(Point(50, 20), "Click to start")
	msg.setFace("helvetica")
	msg.setSize(20)
	msg.setStyle("bold")
	msg.draw(win)
	msg.setTextColor("white")
	win.getMouse()
	msg.setText("")
	
	'''score'''
	score = 0
	
	'''asking player for input'''
	msg.setText("Press arrow key to move")
	trigger = 1
	while trigger == 1:
		key = win.getKey()
		msg.setText("")
		
		'''moving player based on input'''
		if key == "Up":
			character.move(0, 1)
			score += 1
		elif key == "Down":
			character.move(0, -1)
			score += 1
		elif key == "Left":
			character.move(-1, 0)
			score += 1
		elif key == "Right":
			character.move(1, 0)
			score += 1
		elif key == "Escape":
			break
		
		pos = character.getCenter()
		trigger = check(msg, pos)
	
	'''exit message'''
	if trigger == 0:
		score -= 1
		msg.setText("COLLISION!\nGAME OVER\nClick to Exit")
		
		# displaying the score
		msg_score = Text(Point(50, 50), f"Score is {score}")
		msg_score.setFace("helvetica")
		msg_score.setSize(20)
		msg_score.setStyle("bold")
		msg_score.draw(win)
		msg_score.setTextColor("white")
		win.getMouse()
		msg.undraw()
		msg_score.undraw()
		win.close()
	else:
		msg.setText("CHICKEN!\nClick to exit")
		win.getMouse()
		win.close()

def check(msg, pos):	
	'''bifurcating the position data into x and y components'''
	pos_x = pos.getX()
	pos_y = pos.getY()
	
	'''decision bloc'''
	if 0 <= pos_x <= 1 or 0 <= pos_y <= 1:
		return 0
	elif 99 <= pos_x <= 100 or 99 <= pos_y <= 100:
		return 0
	else:
		return 1

main()
