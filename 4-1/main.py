pass_phrases = []
valid_pass_phrases = 0
with open('input.txt') as input_file:
    pass_phrases = input_file.readlines()

for pass_phrase in pass_phrases:
    valid = True
    words = []
    for word_a in pass_phrase.rstrip().split(' '):
        for word_b in words:
            if word_a == word_b:
                valid = False
        else:
            words.append(word_a)
    if valid:
        valid_pass_phrases = valid_pass_phrases + 1
        print(words)


print(valid_pass_phrases)

