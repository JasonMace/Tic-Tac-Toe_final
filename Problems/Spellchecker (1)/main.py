dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

sentence = input().split()
flag = True
for i in sentence:
    if i not in dictionary:
        print(i)
        flag = False

if flag:
    print("OK")
