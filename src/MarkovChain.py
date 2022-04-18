''' Implementation of a Markov Chain with arbitrary state datatypes '''
import random

class MarkovChain(object):
    ''' A Markov Chain object for arbitrary state datatypes '''
    def __init__(self) -> None:
        self.markov_chain = dict() # dict of dicts 
    def fit(self, Seq: list) -> None:
        for i in range(0, len(Seq) - 1):
            a, b = Seq[i], Seq[i + 1]

            if a not in self.markov_chain: self.markov_chain[a] = dict()

            if b not in self.markov_chain[a]: self.markov_chain[a][b] = 0

            self.markov_chain[a][b] += 1
    def walk(self, iterations: int) -> list | bool:
        ''' Probabalistic walk about the model '''
        if not self.markov_chain: return False

        state = random.choice(list(self.markov_chain.keys()))
        y = [state]

        for i in range(iterations):
            elems, p = list(self.markov_chain[state].keys()), list(self.markov_chain[state].values())
            state = random.choices(elems, p, k = 1)[0]

            y.append(state)

        return y


if __name__ == "__main__":
    model = MarkovChain()

    model.fit("This is a sentence and a good sentence".split())
    print(model.markov_chain)

    print(model.walk(5))