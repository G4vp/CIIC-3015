# You are building a battle snake to compete for honor and glory! But before you can do that, you need to take care of some fundamental details...

# Write a function called SnakeNeck() which takes a battle snake game board dictionary as its argument and returns a string describing the relative position of your snake's neck to its head, either "left" or "right" or "up" or "down" where the x-coordinate increases going to the right and the y-coordinate increases going up. The neck is defined to be the first body segment immediately following the head.

# Reference: https://docs.battlesnake.com/references/api/sample-move-request
def SnakeNeck(data):
    headx = data['board']['snakes'][0]['head']['x']
    heady = data['board']['snakes'][0]['head']['y']
    neckX = data['board']['snakes'][0]['body'][1]['x']
    necky = data['board']['snakes'][0]['body'][1]['y']
    
    if(headx == neckX):
        if(heady < necky):
            return 'up'
        else:
            return 'down'
    else:
        if(headx < neckX):
            return 'right'
        else:
            return 'left'
    