correct = input()
wrong = input()
for w in wrong:
    correct.replace(w, '')
correct = set(correct)
pop1 = correct.pop()
if pop1 in wrong:
    print(correct)
