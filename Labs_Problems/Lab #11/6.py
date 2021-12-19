# You are building a battle snake to compete for honor and glory! But before you can do that, you need to take care of some fundamental details...

# Write a function called SnakeTargets() which takes a battle snake game board dictionary as its argument and returns a list containing the names of all snakes which are shorter than your snake, in the same order that they appear in the board data.

# Reference: https://docs.battlesnake.com/references/api/sample-move-request
data = {
  "game": {
    "id": "game-00fe20da-94ad-11ea-bb37",
    "ruleset": {
      "name": "standard",
      "version": "v.1.2.3"
    },
    "timeout": 500
  },
  "turn": 14,
  "board": {
    "height": 11,
    "width": 11,
    "food": [
      {"x": 5, "y": 5}, 
      {"x": 9, "y": 0}, 
      {"x": 2, "y": 6}
    ],
    "hazards": [
      {"x": 3, "y": 2}
    ],
    "snakes": [
      {
        "id": "snake-508e96ac-94ad-11ea-bb37",
        "name": "My Snake",
        "health": 54,
        "body": [
          {"x": 0, "y": 0}, 
          {"x": 1, "y": 0}, 
          {"x": 2, "y": 0}
        ],
        "latency": "111",
        "head": {"x": 0, "y": 0},
        "length": 3,
        "shout": "why are we shouting??",
        "squad": ""
      }, 
      {
        "id": "snake-b67f4906-94ae-11ea-bb37",
        "name": "Another Snake",
        "health": 16,
        "body": [
          {"x": 5, "y": 4}, 
          {"x": 5, "y": 3}, 
          {"x": 6, "y": 3},
          {"x": 6, "y": 2}
        ],
        "latency": "222",
        "head": {"x": 5, "y": 4},
        "length": 4,
        "shout": "I'm not really sure...",
        "squad": ""
      }
    ]
  },
  "you": {
    "id": "snake-508e96ac-94ad-11ea-bb37",
    "name": "My Snake",
    "health": 54,
    "body": [
      {"x": 0, "y": 0}, 
      {"x": 1, "y": 0}, 
      {"x": 2, "y": 0}
    ],
    "latency": "111",
    "head": {"x": 0, "y": 0},
    "length": 3,
    "shout": "why are we shouting??",
    "squad": ""
  }
}
def SnakeTargets(data):
    myLength = data['board']['snakes'][0]['length']
    asd = [x['name'] for x in data['board']['snakes'] if x['length'] < myLength]
    return asd

print(SnakeTargets(data))