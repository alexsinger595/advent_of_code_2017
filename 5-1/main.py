with open('input.txt') as input_file:
    jumps = [int(line.rstrip('\n')) for line in input_file]

step = 0
steps_taken = 0
while step < len(jumps):
    jumps[step] = jumps[step] + 1
    step = step + (jumps[step] - 1)
    steps_taken = steps_taken + 1

print(steps_taken)
