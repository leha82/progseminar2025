"""
    2023.04.09
    코드 작성자: 김태희
    문제: https://school.programmers.co.kr/learn/courses/30/lessons/142086
"""
def solution(s, skip, index):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # 알파벳 소문자
    skip_set = set(skip) # skip에 있는 문자를 set으로 저장
    filtered_alphabet = [ch for ch in alphabet if ch not in skip_set] # skip에 없는 문자만 남김

    # s를 순회하면서 각 문자를 filtered_alphabet에서 찾아서 index만큼 이동
    for i in range(len(s)):
        if s[i] in filtered_alphabet: # s[i]가 filtered_alphabet에 있는 경우에만 이동
            idx = filtered_alphabet.index(s[i]) # s[i]의 인덱스 찾기
            new_idx = (idx + index) % len(filtered_alphabet) # index만큼 이동, len(filtered_alphabet)로 나눈 나머지로 wrap-around 처리
            s = s[:i] + filtered_alphabet[new_idx] + s[i+1:] # s[i]를 새로운 문자로 변경
        else:
            pass # s[i]가 filtered_alphabet에 없는 경우는 pass
    return s

s="aukks"
skip="wbqd"
index=5
print(solution(s, skip, index)) # "happy"