name = 'Subhi'
num = 102
score = 12.5

# %s str; %d int;  %f float

print('name: [', name, '] num: [', num, '] score: [', score, ']', sep='')

print('name: [%s] num: [%s] score: [%s]' % (name, num, score) )

print('name: [%s] num: [%d] score: [%f]' % (name, num, score) )
# print('name: [%d] num: [%d] score: [%f]' % (name, num, score) ) # ERROR

print('name: [%12s] num: [%12d] score: [%12f]' % (name, num, score) )
print('name: [%12s] num: [%12d] score: [%12.3f]' % (name, num, score) )
print('name: [%-12s] num: [%-12d] score: [%-12.3f]' % (name, num, score) )

sentance = 'name: [%12s] num: [%12d] score: [%12f]' % (name, num, score)
print(sentance)
