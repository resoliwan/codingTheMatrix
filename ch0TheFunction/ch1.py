__author__ = 'younlee'
#Task 1.5.1
7 * 24 * 60
#Task 1.5.2
234018/47 - 234018//47
#Task 1.5.3
(673 + 909)%3 == 0
#Task 1.5.4
x = -9
y = 1/2
2**(y+1/2) if x+10<0 else 2**(y-1/2)
#Task 1.5.5
{x**2 for x in {1,2,3,4,5}}
#Task 1.5.6
{2**x for x in {0,1,2,3,4}}
#Task 1.5.7
{x*y for x in {1,2,3} for y in {4,5,7}}
#Task 1.5.8
{x*y for x in {0,1,4} for y in {2,8,32}}
#Task 1.5.9
{x for x in {1,2,3,4} for y in {3,4,5,6} if x == y}
#Task 1.5.10
sum([20,10,15,75])/len([20,10,15,75])
#Task 1.5.11
[[x,y] for x in ['A','B','C'] for y in [1,2,3]]
#Task 1.5.12
loft = [[.25,.75,.1],[-1,0],[4,4,4,4]]
sum(sum(loft,[]))
#Task 1.5.13
[x,y] = [1,2,3]
#Task 1.5.14
S = {-4,-2,1,2,5,0}
[(i,j,k) for i in S for j in S for k in S if i + j + k == 0]
#Task 1.5.15
[(i,j,k) for i in S for j in S for k in S if i + j + k == 0 if not (i == 0 and j ==0 and k ==0)]
#Task 1.5.16
[[(i,j,k) for i in S for j in S for k in S if i + j + k == 0 if not (i == 0 and j ==0 and k ==0)][0]]
#Task 1.5.17
L = [0,0,1]
len(L)
len(list(set(L)))
#Task 1.5.18
list(range(1,100,2))
#Task 1.5.19
L = ['A','B','C','D','E']
list(zip(range(len(L)), L))
#Task 1.5.20
[x+y for [x,y] in list(zip([10,25,40],[1,15,20]))]
#Task 1.5.21
dlist = [{'James':'Sean','director':'Terence'},{'James':'Roger'}]
key = 'James'
[dic[key] for dic in dlist]
#Task 1.5.22
key2 = 'director'
[x[key2] if key2 in x else 'NOT PRESENT' for x in dlist]


