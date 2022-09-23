import random

ans = random.randint(1, 100)  # 1~100사이의 랜덤한 숫자를 뽑아 줌
# print(ans)

print("----- 업 다운 게임을 시작합니다 -----")
cnt = 0 # 몇 회만에 정답을 맞췄는지 횟수 변수
while True:
    num = int(input("숫자 입력 >> "))
    cnt += 1
    if num == ans:
        print("{}회 만에 정답을 맞추셨습니다!".format(cnt))
        break
    elif num > ans:
        print("DOWN!")
    elif num < ans:
        print("UP!")