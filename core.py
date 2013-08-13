"модуль із класом Core що включає в собі деякі методи комбінаторики, які використовуються в програмі"

import itertools
from math import factorial as fact

class Core:
    # Методи-генератори комбінацій/перестановок
    
    #perm = itertools.permutations                           # перестановки
    comb = itertools.combinations                           # комбінації без повторень (порядок не враховується)
    comb_w_repl = itertools.combinations_with_replacement   # комбінації із повторенями (порядок не враховується)

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

    @staticmethod
    def place_w_repl(seq, depth, prev=""):  # розміщення із повторенями (порядок ВРАХОВУЄТЬСЯ)
        for char in seq:
            res = prev + char
            if len(res) == depth:
                yield res
            else:
                for res in Core.place_w_repl(seq, depth, prev=res):
                    yield res
                              
    @staticmethod
    def perm(seq, uselessK):                # перестановки
        for res in itertools.permutations(seq):
            yield res

    # 
    # Методи для обчислення кількості комбінацій/перестановок
    
    @staticmethod
    def comb_number(seq, k):
        N = len(seq)
        return int(fact(N)/(fact(k) * fact(N-k)))

    @staticmethod
    def comb_w_repl_number(seq, k):
        N = len(seq)
        return int(fact(N+k-1)/(fact(k) * fact(N-1)))
    
    @staticmethod
    def place_number(seq, k):
        N = len(seq)
        return int(fact(N)/fact(N-k))
    
    @staticmethod
    def place_w_repl_number(seq, k):
        N = len(seq)
        return N**k

    @staticmethod
    def perm_number(seq, uselessK=None):
        N = len(seq)
        return fact(N)

    
# тестування
if __name__ == '__main__':
    for i in Core.place_w_repl("abcd", 3):
        print(i, end=" ")  
    print(Core.place_w_repl_number("abcd", 3))
    
    for i in Core.place("abcdef", 3):
        print(i, end=" ")  
    print(Core.place_number("abcdef", 3))
    
    print(len(list(Core.perm(range(10)))), Core.perm_number(range(10)))
