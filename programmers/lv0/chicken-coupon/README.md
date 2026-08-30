# 치킨 쿠폰

- 플랫폼: 프로그래머스
- 난이도: Lv.0
- 풀이일: 2026-08-30
- 상태: 해결
- Notion: https://app.notion.com/p/3cc258d7cd3b8197b403e9a4e22aab9c?pvs=204

## 내 풀이

```python
def solution(chicken):
    answer = 0

    while chicken >= 10:
        answer += chicken // 10
        chicken = chicken // 10 + chicken % 10

    return answer
```

## 풀이 아이디어

- `chicken // 10`: 현재 쿠폰으로 새로 받을 수 있는 서비스 치킨 수
- `chicken % 10`: 교환 후 남는 쿠폰 수
- 다음 반복에서 사용할 쿠폰 수는 `chicken // 10 + chicken % 10`
- 쿠폰이 10장 이상일 때만 서비스 치킨을 받을 수 있으므로 `while chicken >= 10`으로 반복한다.

## 처음 막힌 부분

처음에는 최종 코드와 같은 계산식을 작성했지만 오류가 나자 계산식에 문제가 있다고 생각해 코드를 풀어썼다.

```python
def solution(chicken):
    answer = 0

    while chicken > 0:
        chick = 0
        answer += chicken // 10
        chick = chicken % 10
        chicken = chicken // 10
        chicken += chick

    return answer
```

실제 문제는 계산식이 아니라 반복문의 종료 조건이었다.

`chicken`이 1~9가 되면 `chicken // 10`은 0이고 `chicken % 10`은 자기 자신이므로 값이 더 이상 줄지 않는다. 예를 들어 5라면 `5 → 5 → 5 ...`가 되어 `while chicken > 0`이 끝나지 않고 시간 초과가 발생한다.

## 배운 점

- 시간 초과가 발생하면 무한 루프 가능성도 확인한다.
- `while`문에서는 반복 변수가 실제로 종료 조건을 향해 변하고 있는지 확인한다.
- 오류가 났다고 처음 작성한 로직 전체를 바꾸기보다 어느 부분에서 값이 예상과 달라지는지 먼저 확인한다.
- 몫과 나머지를 이용하면 `새로 받은 치킨 수 + 남은 쿠폰 수`를 간결하게 표현할 수 있다.
