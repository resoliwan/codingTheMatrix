# Copyright 2013 Philip N. Klein
#dict2list({'a':'A','b':'B','c':'C'},['b','c','a']) => ['B', 'C', 'A']
def dict2list(dct, keylist): return [dct[x] for x in keylist]

#list2dict(['A','B','C'], ['a','b','c']) =>{'a': 'A', 'b': 'B', 'c': 'C'}
def list2dict(L, keylist): return { k:v for (k,v) in zip(keylist,L)}

#listrange2dict(['A','B','C']) =>  {0: 'A', 1: 'B', 2: 'C'}
def listrange2dict(L): return list2dict(L,range(len(L)))