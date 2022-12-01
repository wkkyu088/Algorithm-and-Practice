# 2019112018 원규진
print('2019112018 원규진')
print('스트링 매칭 알고리즘\n')

import time


# def BruteForce(txt, ptn):
#     start = time.time()
#     n = len(txt)
#     m = len(ptn)
#     for i in range(n - m + 1):
#         j = 0
#         for j in range(m):
#             if ptn[j] != txt[i + j]:
#                 break
#             j += 1
#         if j == m:
#             print("BruteForce : 패턴이 %d번째부터 나타남" % i, end=", ")
#             end = time.time()
#             print(end - start)
#             return

def KMP(txt, ptn):
    start = time.time()
    n = len(txt)
    m = len(ptn)

    # making table
    F = [0] * m
    i, j = 1, 0

    while i < m:
        if ptn[i] == ptn[j]:
            j += 1
            F[i] = j
            i += 1
        elif j != 0:
            j = F[j - 1]
        else:
            F[j] = 0
            i += 1

    # kmp search
    i, j = 0, 0
    while i < n:
        if txt[i] == ptn[j]:
            if j == m - 1:
                print("KMP : 패턴이 %d번째부터 나타남" % (i - j), end=", ")
                end = time.time()
                print(end - start)
                return
            else:
                i += 1
                j += 1
        else:
            if j > 0:
                j = F[j - 1]
            else:
                i += 1

# def RabinKarp(txt, ptn):
#     start = time.time()
#     n = len(txt)
#     m = len(ptn)
    
#     hashT, hashP, b = 0, 0, 1
#     for i in range(n-m+1):
#         if i==0:
#             # get hash value
#             for j in range(m):
#                 hashT += ord(txt[m-1-j])*b
#                 hashP += ord(ptn[m-1-j])*b
#                 if j < m-1:
#                     b *= 2
#         else:
#             hashT = 2*(hashT - ord(txt[i-1])*b) + ord(txt[m-1+i])
#         # rabin-karp search
#         if hashT == hashP:
#             found = True
#             for j in range(m):
#                 if txt[i+j] != ptn[j]:
#                     found = False
#                     break
#             if found:
#                 print("RabinKarp : 패턴이 %d번째부터 나타남" % i, end=", ")
#                 end = time.time()
#                 print(end - start)
#                 return
    
    
text = "20191112018wongyuj12018wong2019112018wongyujygyujin20191won202019119112018w2019112018wongyujin"
pattern = "2019112018wongyujin"
# pattern = "2019"

print("text :", text)
print("pattern :", pattern)
print()

# BruteForce(text, pattern)
KMP(text, pattern)
# RabinKarp(text, pattern)
