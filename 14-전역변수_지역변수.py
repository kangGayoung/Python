def func1():
    a = 1   # 지역 변수 : 함수 안에서 만들어진 변수
            # 함수 안에서만 접근 가능

func1()
# print(a)

num = 10    # 전역 변수 : 함수 밖에서 만들어진 변수
            # 모든 지역에서 접근 가능 (read-only(파이썬에서만))
def func2():
    global num  # num 변수 값 수정 허락 맡기
    num += 1
    print(num)

func2()