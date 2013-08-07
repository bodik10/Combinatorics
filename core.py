"модуль із класом Core що включає в собі деякі методи комбінаторики, які використовуються в програмі"

import itertools
from math import factorial as fact

class Core:
    perm = itertools.permutations                           # перестановки
    comb = itertools.combinations                           # комбінації без повторень (порядок не враховується)
    comb_w_repl = itertools.combinations_with_replacement   # комбінації із повторенями (порядок не враховується)
    
    @staticmethod
    def place_w_repl(seq, depth, prev=""):      # розміщення із повторенями (порядок ВРАХОВУЄТЬСЯ)
        for char in seq:
            res = prev + char
            if len(res) == depth:
                yield res
            else:
                for res in Core.place_w_repl(seq, depth, prev=res):
                    yield res
                    
    @staticmethod
    def place(seq, N, prev=""):             # розміщеня із seq по N (порядок ВРАХОВУЄТЬСЯ)
        for char in seq:
            res = prev + char
            if len(res) == N:
                yield res
            else:
                new_s = list(seq)
                new_s.remove(char)
                for res in Core.place(new_s, N, prev=res):
                    yield res
                    
# тестування
if __name__ == '__main__':
    for i in Core.place_w_repl("abcd", 3):
        print(i, end=" ")  
    print(len(list(Core.place_w_repl("abcd", 3))))
    
    for i in Core.place("abcdef", 3):
        print(i, end=" ")  
    print(len(list(Core.place("abcdef", 3))))
    
    
