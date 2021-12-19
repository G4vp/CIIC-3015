# You are building a battle snake to compete for honor and glory! But before you can do that, you need to take care of some fundamental details...

# Write a function called SnakeHead() which takes a battle snake game board dictionary as its argument and returns the x and y coordinates of your snake's head.

# Reference: https://docs.battlesnake.com/references/api/sample-move-request

def SnakeHead(data):
    x = data['board']['snakes'][0]['head']['x']
    y = data['board']['snakes'][0]['head']['y']
    
    return (x,y) 