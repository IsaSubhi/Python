scores = {
    'david': 90,
    'moshe': 85,
    'lea': 66
}

print('david score is:', scores['david'])

# add 5 points to lea

# scores['lea'] = scores['lea'] + 5
scores['lea'] += 5
print("lea's score is:", scores['lea'])

name = input("enter name:")
print(scores[name])
print(f"{name} score is: {scores[name]}")

# copy moshe's score to david
scores['david'] = scores['moshe']

# remove moshe from scores dictionary:
del scores['moshe']

# add "avi" with score or 94
scores['avi'] = 94

print('shlomo' in scores) # False
print('avi' in scores)    # True
print('david' in scores)  # True
print('moshe' in scores)  # False

print(94 in scores.values())
print(scores.values())
