n = int(input())
divide = 0

for i in range(1, n+1):  # 1부터 n까지의 숫자로 나누어야 하므로 range를 수정합니다.
    divide += 1  # 나눗셈을 진행할 때마다 divide를 1씩 증가시킵니다.
    n //= i  # 나눗셈 연산을 진행한 몫을 n에 다시 저장합니다.
    if n <= 1:  # n이 1 이하가 되었을 때 반복문을 종료합니다.
        print(divide)
        break