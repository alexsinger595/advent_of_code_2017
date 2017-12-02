captcha = ''
total = 0

# Read in the captcha as a list of chars
with open('captcha.txt') as f:
    captcha = list(f.read())

# For char in captcha
for prev, cur, nxt in zip([captcha[-2]]+captcha[:-2], captcha, captcha[1:]):

    # If char equals the char before it, add their sum to the total
    if cur == prev:
        total = total + int(cur)

# Print the total

print(total)
