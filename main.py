#initializing this program to only run on 4x4 boards that compute the game of life
from function import encode, decode, extract_neighbour, neighbour_adder, rule_circuit
#initialize a board with blinker as python list
board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,1,1,1],
    [0,0,0,0]
]

#encode function takes this board and converts it into a single 16bit integer

conway = encode(board)
new = 0
for index in range(16):
    [b0,b1,b2,b3,b4,b5,b6,b7] = extract_neighbour(conway, index)
    count = neighbour_adder(b0,b1,b2,b3,b4,b5,b6,b7)
    #update state
    state = (conway >> (15 - index)) &1
    new = new << 1 | rule_circuit(state,count)

#after loop ends new will be the new board
decoded = decode(new)
print(decoded)


#game logic




