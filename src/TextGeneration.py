from MarkovChain import MarkovChain

''' Ngram state Markov Chain for basic NLG '''

def NGrams(s: str, N: int) -> list[str]:
    array = s.split()
    return [' '.join(array[i: i + N]) for i in range(0, len(array), N)]

model = MarkovChain()
text = open(r'D:\thread\src\alice_in_wonderland.txt', 'r', encoding = 'utf-8').read()
Sequence = NGrams(text, 3)
model.fit(Sequence)

''' Generate 10 sequences of 15 states '''
for _ in range(10):
    print(' '.join(model.walk(15)))
    print(''.join(['-']*200))

