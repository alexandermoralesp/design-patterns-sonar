from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data : List):
        pass

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using the strateg (not sure hot it'll do it")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))



class ConcreteAStrategy(Strategy):
    def do_algorithm(self, data: List):
        return sorted(data)
    
class ConcreteBStrategy(Strategy):
    def do_algorithm(self, data : List):
        return reversed(sorted(data))

if __name__ == "__main__":
    context = Context(ConcreteAStrategy())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteBStrategy()
    context.do_some_business_logic()