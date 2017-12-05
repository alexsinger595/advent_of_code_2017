with open('input.txt') as input_file:
    jumps = [int(line.rstrip('\n')) for line in input_file]

step = 0
steps_taken = 0
while step < len(jumps):
    past_step = step
    step = step + jumps[step] 

    if jumps[past_step] >= 3:
        jumps[past_step] = jumps[past_step] - 1
    else:
        jumps[past_step] = jumps[past_step] + 1

    steps_taken = steps_taken + 1

print(steps_taken)
