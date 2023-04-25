# sliding window 알고리즘 문제를 해결하면서 queue 자료구조로 일반화 하기 좋아보여서 만들어 보았다.

from collections import deque

class SlidingWindow:
    def __init__(self, iterable, size):
        if len(iterable) < size: raise IndexError("too big window for me.. :(")
        self.iterable = iterable
        self.size = size
        self.windows = list(self._get_windows()) # all windows
        
    def _get_windows(self):
        window = deque(self.iterable[:self.size])
        yield tuple(window)
        for elem in self.iterable[self.size:]:
            window.popleft()
            window.append(elem)
            yield tuple(window)
    
    def __iter__(self):
        return iter(self.windows)

    def __len__(self):
        return len(self.windows)

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            return [self.windows[i] for i in range(start, stop, step)]
        elif index < 0:
            index += len(self)
        if not 0 <= index < len(self):
            raise IndexError("index out of range! :(")
        return self.windows[index]
    
    def count(self, subsequence):
        return self.windows.count(subsequence)
    
    def index(self, subsequence):
        return self.windows.index(subsequence)
    
def main():
    window = SlidingWindow([1, 2, 3, 4, 5], 3)

    print(len(window))  

    print(window[1])  
    print(window[:2])  

    print(window.count((2, 3, 4)))
    print(window.count((1, 2, 3)))
    print(window.count((1, 2, 5))) 

    print(window.index((2, 3, 4))) 
    print(window.index((1, 2, 3))) 

if __name__ == '__main__':
    main()


