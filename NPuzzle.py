def dimension(initial_state):
    return len(initial_state)

def inversion(initial_state):
    i_state = []
    for i in initial_state:
        for j in i:
            i_state.append(j)

    total_sum = 0
    for i in range(len(i_state)-1):
        if(i_state[i]!=10000):
            for j in range(i+1,len(i_state)):
                if(i_state[i] > i_state[j]):
                    total_sum += 1
    return total_sum

def blank_tile(initial_state):
    idx = 0
    for i in initial_state:
        idx += 1
        if 10000 in i:
            return dimen - idx + 1

def solvability(dim, inverse, blank):
    if(dimen%2==1 and inverse%2==0):
        return True
    elif(dimen%2==0 and blank%2==1 and inverse%2==0):
        return True
    elif(dimen%2==0 and blank%2==0 and inverse%2==1):
        return True
    else:
        return False

initial_state = [
    [6,1,10,2],
    [7,11,4,14],
    [5,10000,9,15],
    [8,12,13,3]
]

dimen = dimension(initial_state)
inverse = inversion(initial_state)
blank = blank_tile(initial_state)

print("Puzzel dimension: ",dimen)
print("Inversion: ", inverse)
print("Blacktile position: ", blank)

if(solvability(dimen,inverse,blank)==True):
    print("The puzzle is solvable")
else:
    print("The puzzle is not solvable")