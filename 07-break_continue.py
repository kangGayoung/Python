num = 0
while True: # 무한 루프
    num += 1
    if num % 2 == 1: # 만약 num이 홀수라면?
        continue    # 반복문의 조건부 문장으로 돌려보냄
    print(num)
    if num == 20:   # == : 양쪽 값이 같냐?
        break   # 반복문을 강제 탈출시킴