def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#def move_up():


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#jump()
#jump()
#jump()
#jump()
#jump()
#jump()

# using loop
#for step in range(6):
  #  jump()
    
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

while not at_goal():
    jump()

