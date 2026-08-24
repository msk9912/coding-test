def solution(lines):
    answer = 0

    left = min(line[0] for line in lines)
    right = max(line[1] for line in lines)

    result = {key: 0 for key in range(left, right)}

    for line in lines:
        temp = line[0]

        while temp < line[1]:
            result[temp] += 1
            temp += 1

    for val in result.values():
        if val >= 2:
            answer += 1

    return answer
