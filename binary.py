from itertools import combinations
n=int(input())
teams = [list(map(int,list(input()))) for i in range(n)]
print(teams)
comb=combinations(teams,2)
#print("this is the list of combinations",list(comb))
for i in comb:
    print(*i)
    print("asterisk3",list(zip(*i)))
    print("only i",i)
    print("no asterisk", list(zip(i)))
    print("\n\n")