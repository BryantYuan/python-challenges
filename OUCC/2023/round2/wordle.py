word = input()
guess = input()
feedback = 'nnnnn'

for i in range(len(guess)):
    letter = guess[i]
    if letter == word[i]:
        feedback = feedback[:i] + 'y' + feedback[i+1:]
        word = word[:i] + ' ' + word[i+1:]
        guess = guess[:i] + '_' + guess[i+1:]

for i in range(len(guess)):
    letter = guess[i]
    if letter not in word:
        continue
    elif letter in word:
        feedback = feedback[:i] + 'p' + feedback[i + 1:]
        letter.replace(letter, ' ', 1)

print(feedback)
