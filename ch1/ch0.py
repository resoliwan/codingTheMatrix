__author__ = 'yeonghuni'
44 + 11 * 4 -6 /11
#Task0.5.1
60 * 24 * 7
#Task0.5.2
2304811/47 - 2304811//47

1e16 + 1
"This is sentance is false"
"So's this one"
5 == 4
4 == 4
True and False
True and not (4 == 5)
#Task0.5.3
673%3 == 909%3
909%3
673%3

mynum = 4 + 1
mynum = "Brown"

# <expression> if <condition> else <expression>
x = -9
y = 1/2
2**(y+1/2) if x+10<0 else 2**(y-1/2)

#Set
{1+2, 3, "a"}
{2, 1, 3}
len({'a', 'b', 'c', 'a', 'a'})

sum({1,2,3})
sum({1,2,3},10)
S={1,2,3}
2 in S
4 in S
4 not in S

#union
{1,2,3}|{2,3,4}
{1,2,3}&{2,3,4}

S = {1,2,3}
S.add(4)
S
S.remove(2)
S

S.update({2,3,4,5})
K = {1,2,3}
K.intersection_update({1,2})
K
A = {1,2}
B = A
B.remove(1)
A

C = {1,2}
D = C.copy()
C.remove(2)
D

{2*x for x in {1,2,3}}
#Task 0.5.5
{x**2 for x in {1,2,3,4,5}}
#Task 0.5.6
{2**x for x in {1,2,3,4}}

{x*x for x in S | {6}}
{x for x in {1,2,3} if x > 2}
{x * y for x in {1,2,3} for y in {2,3,4}}
#Task 0.5.7
{x * y for x in {1,2,3} for y in {4,5,7}}

{x * y for x in {1,2,3} for y in {2,3} if x == y}

#Task 0.5.8 ?
{x * y for x in {4,8,1} for y in {2,16,12} if x != y}

#Task 0.5.9
S = {1,2,3,4}
T =  {3,4,5,6}
{x for x in S for y in T if x in T}
S & T