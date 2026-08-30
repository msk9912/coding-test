def solution(bin1, bin2):
    answer = ""
    num1 = 0
    num2 = 0

    bin1 = int(bin1)
    bin2 = int(bin2)

    b = 0
    while bin1 > 0:
        num1 += 2**b * (bin1 % 10)
        bin1 //= 10
        b += 1

    b = 0
    while bin2 > 0:
        num2 += 2**b * (bin2 % 10)
        bin2 //= 10
        b += 1

    total = num1 + num2
    while total > 0:
        answer = str(total % 2) + answer
        total //= 2

    if answer == "":
        answer = "0"
    return answer
