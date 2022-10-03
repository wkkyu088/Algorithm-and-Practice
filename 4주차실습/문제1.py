# 2019112018 원규진
print('2019112018 원규진')
print('문제1-2 순환 방식 회문\n')

# 파일을 리스트로 변환
def fileToList(f):
    ls = []
    while True:
        line = f.readline().rstrip()
        if not line: break
        ls.append(line)
        
    return ls

# 비순환 방식 회문 알고리즘
def palindrome(str):
    result = True

    while len(str) > 1:
        x = str[0]
        y = str[-1]
        if x!=y: 
            result = False
            break
        str = str[1:-1]
    return result

# 순환 방식 회문 알고리즘
def recursivePalindrome(str):
    result = True
    if len(str) <= 1:
        return result
    
    x = str[0]
    y = str[-1]
    if x!=y: 
        result = False
        return result

    result = recursivePalindrome(str[1:-1])
    return result


f = open("4주차실습/src.txt", 'r')
ls = fileToList(f)
f.close()

# 비순환 방식
# for l in ls:
#     str = ''.join(l.lower().split())
#     print(l, ':', '회문' if palindrome(str) else 'X')

# 순환 방식
for l in ls:
    str = ''.join(l.lower().split())
    print(l, ':', '회문' if recursivePalindrome(str) else 'X')