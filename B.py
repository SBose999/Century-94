import sys
_ord, inp, num, neg, _Index = lambda x: x, [], 0, False, 0
i, s = 0, sys.stdin.buffer.read()
try:
    while True:
        if s[i] >= b"0"[0]:num = 10 * num + _ord(s[i]) - 48
        elif s[i] == b"-"[0]:neg = True
        elif s[i] != b"\r"[0]:
            inp.append(-num if neg else num)
            num, neg = 0, False
        i += 1
except IndexError: pass
if s and s[-1] >= b"0"[0]: inp.append(-num if neg else num)
_T_=inp[_Index];_Index+=1
for _t_ in range(_T_):
    p,f=inp[_Index:_Index+2];_Index+=2
    cs,cw=inp[_Index:_Index+2];_Index+=2
    s,w=inp[_Index:_Index+2];_Index+=2
    if w<s:
        s,w=w,s
        cs,cw=cw,cs 
    ans=0
    for i in range(0,cs+1):
        ptakes=min(p//s,i)
        ptakew=min(cw,(p-(ptakes*s))//w)
        ftakes=min(cs-ptakes,f//s)
        ftakew=min(cw-ptakew,(f-(ftakes*s))//w)
        ans=max(ans,ptakes+ptakew+ftakes+ftakew)
    print(ans)
