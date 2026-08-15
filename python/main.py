#initializing this program to only run on 4x4 boards that compute the game of life
from function import encode, decode, extract_neighbour, neighbour_adder, rule_circuit, display_board, clear_screen
import time
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
display_board(decoded) #display the board in a readable format
input("Press Enter to start the game of life simulation...") #wait for user input to start the game
#game logic
cycle = 0
while True:
    print("Cycle: ", cycle)

    conway = encode(decoded)
    new = 0
    for index in range(16):
        [b0,b1,b2,b3,b4,b5,b6,b7] = extract_neighbour(conway, index)
        count = neighbour_adder(b0,b1,b2,b3,b4,b5,b6,b7)
        #update state
        state = (conway >> (15 - index)) &1
        new = new << 1 | rule_circuit(state,count)

    #after loop ends new will be the new board
    decoded = decode(new)
    display_board(decoded) #display the board in a readable format
    time.sleep(0.5) #wait for 0.5 seconds before displaying the next board
    clear_screen() #clears the screen to display the next board

    cycle += 1
    if cycle == 30:
        break #stops the cycle after 30 iterations to avoid infinite loop




