import numpy as np

pop = 5
n = 6

def GenerateP_0(pop, n):
    '''Generuje P_0'''
    P_0 = []
    for i in range(pop):
        P_0.append(np.random.choice(n, size=n, replace=False) + 1)
    return np.array(P_0)

def evaluate(P):
    # res = []
    # for el in P:
    #     res.append(beats_counter(el))
    return beats_counter(P)

def beats_counter(pos):
    '''Liczy bicia'''
    cnt = 0
    #Iterujemy po każdym elemencie
    for iter in range(len(pos) - 1):
        #Kolumny to indeksy, a wiersze to zawartość listy pos
        for col, row in enumerate(pos[iter:]):
            #Sprawdzamy czy kolumna nie jest ustawiona na ostatnią, i przechodzimy po liście w celu poszukiwania bić
            if(col == (len(pos[iter:]) - 1)):
                break
            else:
                if Attack(row, col + 1, pos[col + 1], col + 2) == True:
                    cnt += 1
    return cnt

def Attack(q_row, q_col, o_row, o_col):
    '''Sprawdza czy jest bicie między 2 hetmanami q - actual_queen, o - opponent'''
    if q_row == o_row:
        return True
    elif q_col == o_col:
        return True
    elif (np.abs(q_row - o_row) == np.abs(q_col - o_col)):
        return True
    else:
        return False

def selection(P):
    '''Dokonuje selekcji turniejowej, zwraca P_n z powtórkami'''
    i = 0
    P_n = []
    while i < pop:
        i_1 = np.random.randint(pop)
        i_2 = np.random.randint(pop)
        if i_1 != i_2:
            if i_1 != i_2:
                if evaluate(P[i_1]) <= evaluate(P[i_2]):
                    P_n.append(P[i_1])
                else:
                    P_n.append(P[i_2])
                i += 1
    # return np.unique(P_n, axis=0)           ##Zwraca unikalne wartości ale trzeba pozniej changeować pop -> dziwne, teraz są powtórki ?
    return np.array(P_n)

def crossover(P):
    '''Swapuje miejscami kilka losowych wartości'''
    i = 0
    p_c = 0.7
    while i < pop - 2:
        if np.random.rand() <= p_c:
            P[[i + 1, i]] = P[[i, i + 1]]
            i += 2
    return P

def mutation(P):
    '''Usuwa i dodaje nową wartość do populacji'''
    i = 0
    p_m = 0.5
    while i < pop:
        if np.random.rand() <= p_m:
            P[i] = np.random.choice(n, size=n, replace=False) + 1
        i += 1
    return P

P_0 = GenerateP_0(pop, n)
P_n = selection(P_0)
P_n = crossover(P_n)
print(P_n)
print(mutation(P_n))
# best = np.where(evaluate(P_0) == np.amin(evaluate(P_0)))[0][0]      ###indeks najlepszego rozwiązania
# print(best)