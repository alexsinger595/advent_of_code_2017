captcha = ''
total = 0

# Read in the captcha as a list of chars
with open('captcha.txt') as f:
    captcha = list(f.read().rstrip())

offset = int(len(captcha)  / 2) 

# For char in captcha
for idx, cur in enumerate(captcha):

    opposite_idx = idx + offset
    if opposite_idx >= len(captcha):
        opposite_idx = (opposite_idx - len(captcha))

    if cur == captcha[opposite_idx]:
        total = total + int(cur)

    print(cur, idx, captcha[opposite_idx], opposite_idx)

# Print the total
print(total)
