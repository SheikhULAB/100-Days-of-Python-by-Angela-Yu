def turn_right():
    turn_lef()
    turn_left()
    turn_left()

while not at_goal():
    if righ_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


