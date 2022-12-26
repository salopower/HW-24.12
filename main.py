from typing import TypeVar, List

T = TypeVar('T')


class ReverseIterator:
    def __init__(self, lst: List[T]) -> None:
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self) -> 'ReverseIterator':
        return self

    def __next__(self) -> T:
        if self.index < 0:
            raise StopIteration
        else:
            result = self.lst[self.index]
            self.index -= 1
            return result


lst = [1, 2, 3, 4]

rev_iter = ReverseIterator(lst)
for item in rev_iter:
    print(item)
