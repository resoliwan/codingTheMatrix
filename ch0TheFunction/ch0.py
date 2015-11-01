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

#python set's elements must not be mutable
#there is a frozen set be used as element but we will not use
#{{1,2},3}

#List
[1, 1+1, 3, 2, 3]
L = [[1,1 + 1, 4 -1], {2*2,3}, "yo"]
len(L)
L1 = [1,2,3]
sum(L1)
sum(L1, -9)

#Task 0.5.10
sum(L1)/len(L1)

[1,2] + [3,4]
mylist = [4,8,12]
mylist + [1,2]
mylist

#we can sum() on a collcetions of list, obtaining the concanation of all the lists by providing [] as the second argument
#sum([[1,2],[2,3],[3,4]])
sum([[1,2],[2,3],[3,4]],[])

#the order of list might not corrspond to the order of elements in  a set since the latter order is not significant
[2 * x for x in {1,2,3}]

[2 * x for x in [1,2,3]]
[x * y for x in [1,2,3] for y in [2,3,4]]

#Task 0.5.11
[[x,y] for x in ['A','B',"C"] for y in [1,2,3]]

#Task 0.5.12
Lofl = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
sum(sum(Lofl,[]))

mylist = [0,1,2]
mylist[0]
['in', 'the','CIT'][1]
#i:j and j as one past the index of the last element
mylist[1:3]
#if first index of the pair is 0 it can be omitted
mylist[:2]
#if the second element j of the pair is the lenght of the list, it can be omitted
mylist[0:]
#a:b:c a, start , b:end c: c'th element if we get odd-index element
a = [0,1,2,3,4,5]
a[::2]
a[1::2]

#unpacking
y = [1,2,3]
[a,b,c] = y
a

[a,b,c] = [1,2,3,4]
listOfList = [[1,2],[3,4],[5,6]]
[y for [x, y] in listOfList]

mylist = [1,2,3]
mylist[1] = 0
mylist

#tupple is an ordered sequence of elements however, tuple are immutable
(1,1+3,4)
(1,'A')
{(1,2),(1, 3+4)}

mytuple = (1,'A',(1,2))
mytuple[2]

(a,b) =(1,2)
a
a,b = 1,2
a,b = 1, 5-3
[y for (x,y) in [(1,'A'),(2,'B'),(3,'C')]]

#Task 0.5.14
[(x,y,z) for x in {-4, -2,1,2,5,0} for y in {-4, -2,1,2,5,0} for z in {-4, -2,1,2,5,0} if sum([x,y,z]) == 0]

#Task 0.5.15
[(x,y,z) for x in {-4, -2,1,2,5,0} for y in {-4, -2,1,2,5,0} for z in {-4, -2,1,2,5,0} if sum([x,y,z]) == 0 and not (x == 0 and y == 0 and z == 0)]

#Task 0.5.16
[(x,y,z) for x in {-4, -2,1,2,5,0} for y in {-4, -2,1,2,5,0} for z in {-4, -2,1,2,5,0} if sum([x,y,z]) == 0  and x != y and x != z and y != z]


set([1,2,3])
list({1,2,3})
set((1,2,3))
list((1,2,3))
tuple([1,2,3])
tuple({1,2,3})

#Task 0.5.17
len([1,1,1])
len(list(set([1,1,1])))

#range make sequenc 0 to num - 1
range(10)

#range is not a set or list
list(range(10))
list(range(1, 3))

#Task 0.5.18
set(range(1,100,2))


#zip  each elements of the zip is a tuple consisting of one element from each other of the input collections
list(zip([1,2,3],['A','B','C']))

characters = ['N','B','C']
actors = ['1','2','3']
[c + ' is ' + a for (c, a) in zip(characters, actors)]

#Task 0.5.19
list(zip(list(range(5)), ['A','B','C','D','E']))

#Task 0.5.20
[sum([x,y]) for (x,y) in zip([10, 20, 40],[1,25,20])]
[ sum(x) for x in zip([10, 20, 40], [1,25,20])]

#reverse dose not change self
[x*x for x in reversed([1,2,3])]
a = [1,2,3]
list(reversed(a))
a

alphabet ={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,
'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
{1+2:1,2:2}
{0:1,0:2}
alphabet['A']
{1:1,4:4}[1]

mydict = {'Neo':'Keanu', 'Morpheus':'Laurence', 'Trinity':'Carrie-Anne'}
mydict['Neo']
mydict['Oracle']

'Oracle' in mydict
'Neo' in mydict

mydict['Oracle'] if 'Oracle' in mydict else 'NOT PRESENT'
mydict['Neo'] if 'Neo' in mydict else 'NOT PRESENT'
#Task 0.5.12
[mydict[key] for key in mydict]

#Task 0.5.22 ??
#comprehension?
dlist = [{'Bilbo':'Ian', 'Frodo':'Elijah'},{'Bilbo':'Ian', 'Torin':'Elijah'}]
[dic['Bilbo'] if 'Bilbo' in dic else 'NOT PRESENT' for dic in dlist]
[dic['Frodo'] if 'Frodo' in dic else 'NOT PRESENT' for dic in dlist]

l = {'A':1}
l['A'] = 2
l

{k:v for (k,v) in [(1,2),(3,4)]}
{(x,y):x * y for x in [1,2,3] for y in [4,5,6] }

#Task 0.5.23
{ x:x**2 for x in list(range(0,100))}

#Task 0.5.24
D = {'red','white','blue'}
{x:x for x in D}

#Task 0.5.25 ?

base = 10
digits = set(range(base))
digits
{x:(x//(base*base),x%(base*base)//base,x%base) for x in range(1000)}

#{x:(x//(base*base),x//base,x%base) for x in range(999)}

base = 2
digits = set(range(base))
digits
{x:(x//(base*base),x%(base*base)//base,x%base) for x in range(8)}

[2*x for x in {1:'A',2:'B'}.keys()]
[x for x in {1:'A',2:'B'}.values()]

[k for k in {'a':1,'b':2}.keys()|{'b':3,'c':4}.keys()]
[k for k in {'a':1,'b':2}.keys()&{'b':3,'c':4}.keys()]
[myitem for myitem in {1:'a',2:'b'}.items()]
[k + v for (k, v) in {'a':'a','b':'b'}.items()]

#Task 0.5.26
id2salary = {0:100, 3:300,1:1000}
names = ["Larry","Curly","","Moe"]
{names[k] : v for (k,v) in id2salary.items()}

#Task 0.5.27
def twice(z): return 2*z
twice(1)
twice('A')
twice(['A'])
#z

#Task 0.5.28
def nextInts(l):return [x + 1 for x in l]
nextInts([1,2,5])
#Task 0.5.29
def cubes(l): return [x**3 for x in l]
cubes([1,2,3])
#Task 0.5.30
def dict2list(dic, keylist): return [dic[x] for x in keylist]
dict2list({'a':'A','b':'B','c':'C'},['b','c','a'])
#Task 0.5.31
def list2dict(L,keylist): return { keylist[i]:L[i] for i in range(len(L))}
def list2dict(L,keylist): return { k:v for (k,v) in zip(keylist,L)}
list2dict(['A','B','C'], ['a','b','c'])

#Task 0.5.32
def all_3_digit_numbers(base, digits): return {sum((x*base*base,y*base,z)) for x in digits for y in digits for z in digits}
all_3_digit_numbers(2, {0,1})
all_3_digit_numbers(3, {0,1,2})

#0.6
#Task 0.6.1
import math
help(math)
math.sqrt(3)
#Task 0.6.2
from random import randint
randint(1,10)
def movie_review(name): return ["See it","A gem!","Ideologcial claptrap!"][randint(0,2)]
movie_review('hello')

#Task 0.6.3
import dictutil
dictutil.dict2list({'a':'A','b':'B','c':'C'},['b','c','a'])
dictutil.list2dict(['A','B','C'], ['a','b','c'])

from importlib import reload
reload(dictutil)
#Task 0.6.4
dictutil.listrange2dict(['A','B','C'])

for x in {1,2,3}:
    print(x)

v = [1,2,0]
i = 0
while v[i] == 0:
    print(v[i])
    i = i + 1
if True : print('True')

for x in [1,2,3]:
    y = x * x
    print(y)
x
y

S = "There is no spoon"
for i in range(len(S)):
    if S[i] == 'n':
        break

f = open('./ch0TheFunction/stories_big.txt')

for line in f:
    print(f)

f = open('./ch0TheFunction/stories_small.txt')
stories = list(f)
len(stories)
list(enumerate(['A','B','C']))
[i*s for (i,s) in enumerate(['A','B','C'])]


a = {1,2}
a.add(3)
a
def makeInverseIndex(strlist):
    result = {}
    for i, str in enumerate(strlist):
        words = str.split()
        for word in words:
            if word in result:
                result[word].add(i)
            else:
                result[word] = {i}

    return result





makeInverseIndex(['hello world','hello','hello cat','hellolot of cats']) == {'hello': {0, 1, 2}, 'cat': {2}, 'of': {3}, 'world': {0}, 'cats': {3}, 'hellolot': {3}}

mystr = 'hello world'
mystr.split()

idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
idx

a = {1,2}
b = {2,3}
a.union(b)

def orSearch(inverseIndex, query):
    result = set()
    for q in query:
        result = result | inverseIndex[q]

    return result

orSearch(idx, ['Bach','the'])

def andSearch(inverseIndex, query):
    result = None
    for q in query:
        if result ==  None:
            result = inverseIndex[q]
        else:
            result = result & inverseIndex[q]

    return result

andSearch(idx, ['Johann', 'the'])