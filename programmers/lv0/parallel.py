def solution(dots):
    answer = 0

    def inc(a, b):
        return (dots[a][1] - dots[b][1]) / (dots[a][0] - dots[b][0])

    if inc(0, 1) == inc(2, 3):
        answer = 1
    elif inc(0, 2) == inc(1, 3):
        answer = 1
    elif inc(0, 3) == inc(1, 2):
        answer = 1

    return answer
