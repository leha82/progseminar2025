def solution(s,skip,index):
    a='abcdefghijklmnopqrstuvwxyz'
    S=set(skip)
    r=''
    for c in s:
        i=0
        while i<index:
            c=a[(a.index(c)+1)%26]
            i+=c not in S
        r+=c
    return r

def sol(s, skip, index):
    allowed = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in skip]
    return ''.join(allowed[(allowed.index(c) + index) % len(allowed)] for c in s)

if __name__ == "__main__":
    print(solution("aukks", "wbqd", 5))
    print(sol("aukks", "wbqd", 5))
