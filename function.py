#this file implements all the math functions required for the bitwise operations

def full_adder(a,b,c):
    #this functions takes in two one bit numbers a and b and adds them with carry c
    s = a ^ b
    c1 = a & b
    total = s ^ c
    carry = (s & c) | c1
    return total, carry

def bus(tup):
    #tup carries total and carry from full adder. this function combines them.
    num = tup[1] << 1 | tup[0]
    return num

def bit2_adder(a,b):
    #function takes in two 2bit numbers a and b and adds them together for a 3 bit output with carry
    (b0,c0) = full_adder(a & 1, b & 1, 0)
    (b1,c1) = full_adder(a >> 1 &1, b>>1 &1,c0)
    total = c1 << 2 | b1 << 1 | b0
    return total #3bit number

def bit3_adder(a,b):
    #function takes in two 3bit numbers and gives a 4bit output for addition
    (b0,c0) = full_adder(a & 1, b & 1, 0)
    (b1,c1) = full_adder(a >> 1 &1, b >> 1 &1, c0)
    (b2,c2) = full_adder(a >> 2 &1, b >> 2 &1, c1)
    total = c2 << 3 | b2 << 2 | b1 << 1 | b0
    return total #4bit number

def neighbour_adder(b0,b1,b2,b3,b4,b5,b6,b7):
    #function takes the cell values of 8 precise bits and returns the total number of cells that are alive
    #first parallel adder gives us a two bit output.
    first1 = bus(full_adder(b0,b1,0)) 
    first2 = bus(full_adder(b2,b3,0))
    first3 = bus(full_adder(b4,b5,0))
    first4 = bus(full_adder(b6,b7,0))

    second1 = bit2_adder(first1, first2)
    second2 = bit2_adder(first3, first4)

    third = bit3_adder(second1, second2)
    return third

def encode(board):
    #read every element in the board and create a number out of it
    num = 0
    for row in board:
        for cell in row:
            num = num << 1 | cell
    return num

def decode(num:int):
    #have to read number backwards and reconstruct the board. num is a 16bit integer
    board = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
    #take the binary number and get the last digit of it and perform and operation with 1.
    for i in range(4):
        for j in range(4):
            board[3-i][3-j] = num & 1
            num = num >> 1
    return board

def rule_circuit(state, count):
    #this function takes in state of the cell and it's neighbour count to compute the next state
    s = state #this codes the s bit as a state bit
    b,c,d = count>>2 &1, count>>1 &1, count>>0 &1 #count is 4bit encoded in a b c d separate
    #logic circuit f = b'c(s+d)
    not_b = b ^ 1
    out = (not_b & c) & (s | d)
    return out

def extract_neighbour(num, index):
    #the input is the board in the bit representation num, and the index at which we are picking the neighbour.
    values = [0,0,0,0,0,0,0,0] #stores the cell values
    i=0
    for n in neighbours[index]:
        values[i] = num >> (15 - n) & 1
        i+=1
    #order of neighbours is irrelevant, only total count necessary. thus how many 1s in values only matter
    #feed neighbour adder the elements of the list returned by this function
    return values

def neighbour_link(index):
    #given index returns a list of neighbouring indices
    neighbour = []
    row = index >> 2
    col = index & 3
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == 0 and j == 0:
                continue
            r = row + i
            c = col + j
            if 0 <= r < 4 and 0 <= c < 4:
                neighbour.append(r*4+c)

    return neighbour

neighbours = [neighbour_link(i) for i in range(16)]