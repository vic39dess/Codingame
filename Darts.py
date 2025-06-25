import sys
import math
import operator

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

size = int(input())
n = int(input())

#Définition Dictionnaire nombre de point personnes
Point_list = {}
for i in range(n):
    name = input()
    Point_list[name] = 0
t = int(input())
for i in range(t):
    inputs = input().split()
    throw_name = inputs[0]
    throw_x = int(inputs[1])
    throw_y = int(inputs[2])

    #Définir carré, cercle, losange et points marqués
    if abs(throw_x)+abs(throw_y) <= size/2:
        Point_list[throw_name] += 15

    elif abs(throw_x)+abs(throw_y) > size/2 and (throw_x**2 + throw_y**2) <= (size*size)/4:
        Point_list[throw_name] += 10

    elif (throw_x**2 + throw_y**2) > (size*size)/4 and (abs(throw_x)<=size/2 and abs(throw_y)<=size/2):
        Point_list[throw_name] += 5

Point_list = dict(sorted(Point_list.items(), key=operator.itemgetter(1), reverse=True))


for name in Point_list:
    print(name,Point_list[name])

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
