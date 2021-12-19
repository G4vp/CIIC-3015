# You are building a battle snake to compete for honor and glory! But before you can do that, you need to take care of some fundamental details...

# Write a function called SnakeSafe() which takes a battle snake game board dictionary, an x-coordinate, and a y-coordinate as its arguments and returns True or False depending on whether it is safe for a snake to move into that location. (Empty spaces and food are safe. Snake body parts and hazards are not safe.)

# Reference: https://docs.battlesnake.com/references/api/sample-move-request
def SnakeSafe(data,x,y):
    hazards = data['board']['hazards']
    body = data['you']['body']
    for i in hazards:
        if x == i['x'] or y == i['y']: return False
    for i in body:
        if x == i['x'] or y == i['y']: return False
    return True