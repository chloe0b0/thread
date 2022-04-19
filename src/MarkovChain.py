''' Implementation of a Markov Chain with arbitrary state datatypes '''
import random
from typing import Any, Iterable

class MarkovChain(object):
    ''' A Markov Chain object for arbitrary state datatypes '''
    def __init__(self) -> None:
        self.markov_chain = dict() # dict of dicts
    def fit(self, Seq: Iterable, wrap: bool = False) -> None:
        ''' Given a list of states [s0, s1, ..., sn], where Sn 'leads to' Sn+1, fits the model. If wrap is true, the first element will be appended to the end '''
        if wrap: Seq.append(Seq[0])

        for i in range(0, len(Seq) - 1):
            a, b = Seq[i], Seq[i + 1]

            if a not in self.markov_chain: self.markov_chain[a] = dict()

            if b not in self.markov_chain[a]: self.markov_chain[a][b] = 0

            self.markov_chain[a][b] += 1
    def sample(self, state: Any) -> Any | bool:
        ''' Samples a state from the probability distribution of a given state. Returns False if there are no possible states '''
        elems, p = list(self.markov_chain[state].keys()), list(self.markov_chain[state].values())
        if not elems: return False

        return random.choices(elems, p, k = 1)[0]
    def walk(self, iterations: int) -> list | bool:
        ''' Probabalistic walk about the model for N iterations '''
        if not self.markov_chain: return False

        state = random.choice(list(self.markov_chain.keys()))
        y = [state]

        for i in range(iterations):
            state = self.sample(state)
            y.append(state)

        return y
    def distribution(self, state: Any) -> dict[Any, float]:
        ''' Given a state, returns the probability distribution of all possible subsequent states as a dictionary '''
        distr = self.markov_chain[state]
        sigma = sum(distr.values())

        return {k: v / sigma for k,v in distr.items()}