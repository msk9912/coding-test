def solution(i, j, k):
    answer = 0

    for l in range(i, j + 1):
        while l > 0:
            if l % 10 == k:
                answer += 1
            l //= 10

    return answer
