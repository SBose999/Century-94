import sys
input=sys.stdin.readline
inin=lambda: int(input())
inar=lambda: list(map(int,input().split()))
inst=lambda: input().rstrip('\n\r')
#INF=float('inf'); from math import gcd 
#from collections import deque as que, defaultdict as vector, Counter
#from bisect import bisect
#from heapq import heapify, heappush as hpush, heappop as hpop
'''from types import GeneratorType
def recursive(f, stack=[]):
  def wrappedfunc(*args, **kwargs):
    if stack: return f(*args, **kwargs)
    else: 
      to = f(*args, **kwargs)
      while True:
        if type(to) is GeneratorType:
          stack.append(to); to = next(to)
        else:
          stack.pop()
          if not stack: break
          to = stack[-1].send(to)
      return to
  return wrappedfunc'''

_T_=inin()
for _t_ in range(_T_):
    s=inst()
    x=inin()
    n=len(s)
    ns=['1' for i in range(len(s))]
    w=['1' for i in range(len(s))]
    for i in range(len(s)):
        if s[i]=='0':
            if i-x>=0:
                w[i-x]='0'
            if i+x<n:
                w[i+x]='0'
    for i in range(len(s)):
        if i-x>=0 and w[i-x]=='1':
            ns[i]='1'
        elif i+x<n and w[i+x]=='1':
            ns[i]='1'
        else:
            ns[i]='0'
    if ''.join(ns)==s:
        print(''.join(w))
    else:
        print(-1)
