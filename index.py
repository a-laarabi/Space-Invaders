#! /usr/bin/env python2.7
#codeing : UTF_8

import turtle
import os
import math
import random


#set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("img/Sans_titre-1.gif")

#Register the shapes
turtle.register_shape("img/dead.gif")
turtle.register_shape("img/enemy.gif")
turtle.register_shape("img/weapon.gif")
turtle.register_shape("img/player.gif")


#border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(4)
for i in range(4):
	border.fd(600)
	border.left(90)
border.hideturtle()

############################ player ############################
player = turtle.Turtle()
player.penup()
player.setposition(0,-250)
player.shape("img/player.gif")
player.color("red")
player.setheading(90)
player.speed(0)

playerSpeed = 15


############################ weapon ############################
weapon = turtle.Turtle()
weapon.color("white")
weapon.shape("img/weapon.gif")
weapon.speed(0)
weapon.penup()
weapon.shapesize(0.5,0.5)
weapon.setheading(90)
weapon.hideturtle()

weaponSpeed = 20
weaponState = "ready"


############################ enemy ############################
global enemyNumber
#enemyNumber = 7

#enemies = []

#for i in range(enemyNumber):
#enemies.append(turtle.Turtle())

#for enemy in enemies:
enemy =turtle.Turtle()
enemy.penup()
enemy.shape("img/enemy.gif")
#x = random.randint(-250,-230)
#y = random.randint(-280, 280)
enemy.setposition(-250,250)
enemy.speed(0)
enemy.color("yellow")

enemySpeed = 2


###move PLAYER right and left
def move_left():
	x = player.xcor()
	x -= playerSpeed
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerSpeed
	if x > 280:
		x = 280
	player.setx(x)

def show_weapon():
	global weaponState
	if weaponState == "ready":
		weaponState = "notReady"
		x = player.xcor()
		y = player.ycor()+10
		weapon.setposition(x , y)
		weapon.showturtle()

def move_weapon():
	y = weapon.ycor()
	y += weaponSpeed
	weapon.sety(y)
	

###move ENEMY right and left
def move_enemy():
	global enemySpeed
	y = enemy.ycor()
	x = enemy.xcor()
	x += enemySpeed
	if x == 280:
		enemySpeed *= -1
		y -= 40
		enemy.sety(y)
	if x == -280:
		enemySpeed *= -1
		y -= 40
		enemy.sety(y)
	enemy.setx(x)


def isCollision(t1,t2):
	global distance
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False


#keybord bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(show_weapon, "space")



while True:
	move_enemy()
	move_weapon()
	if weapon.ycor() > 250:
		weapon.hideturtle()
		weaponState = "ready"

	#if (weapon.xcor() == enemy.xcor()) and (weapon.ycor() == enemy.ycor()):
	#	enemy.hideturtle()
	#	weapon.hideturtle()
	#print("({},{}) ||| ({},{})").format(weapon.xcor(),weapon.ycor(),enemy.xcor(),enemy.ycor())

	if isCollision(weapon,enemy):
		#Reset weapon
		weapon.hideturtle()
		weaponState = "ready"
		weapon.setposition(0,-400)
		#Reset the enemy
		enemy.shape("img/dead.gif")
		enemy.setposition(-250,250)
		enemy.shape("img/enemy.gif")
		
		#<>enemyNumber += 1

	if isCollision(player,enemy):
		player.hideturtle()
		enemy.hideturtle()
		print("Game Over")
		break

	###move weapon 


























