#Dana jest tablica wypeªniona liczbami naturalnymi int t[N][N] reprezentuj¡ca szachownic¦. Prosz¦ napisa¢
#funkcj¦, która sprawdza, czy jest mo»liwe ustawienie dwóch wzajemnie szachuj¡cych si¦ skoczków tak, aby
#suma warto±ci pól, na których stoj¡ skoczki, byªa liczb¡ pierwsz¡. Do funkcji nale»y przekaza¢ tablic¦ t,
#funkcja powinna zwróci¢ warto±¢ typu bool.
def is_prime(a):
    if a < 2:
        return False
    if a == 2 or a == 3 or a == 5:
        return True
    if a%2 == 0 or a%3 == 0:
        return False
    for i in range(6,a//2,6):
        if a % (i-1) == 0 or a % (i+1) == 0:
            if a != i:
                return False
    return True

def is_safe(tab,w,k,i):
    moves = [(1,2),(2,1),(-1,-2),(-2,-1),(-1,2),(2,-1),(-2,1),(1,-2)]
    n = len(tab)
    nw = w + moves[i][0]
    nk = k + moves[i][1]
    if nw >= 0 and nw < n and nk >= 0 and nk < n:
        if is_prime(tab[w][k] + tab[nw][nk]):
            return True
    return False


def funkcja(tab):
    n = len(tab)
    f = False
    for w in range(n):
        for k in range(n):
            for i in range(8):
                if is_safe(tab,w,k,i):
                    f = True
    if f:
        return True
    else:
        return False

tab = [[2,3,4],[4,5,3],[2,4,8]]
print(is_safe(tab,0,0,0))
print(funkcja(tab))