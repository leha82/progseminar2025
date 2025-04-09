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

if __name__ == "__main__":
    print(solution("aukks", "wbqd", 5))