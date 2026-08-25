def solution(a, b):
    answer = 1
    div = 2

    while div <= min(a, b):
        if a % div == 0 and b % div == 0:
            a //= div
            b //= div
        else:
            div += 1

    while b != 1:
        if b % 2 == 0:
            b //= 2
        elif b % 5 == 0:
            b //= 5
        else:
            answer = 2
            break

    return answer
