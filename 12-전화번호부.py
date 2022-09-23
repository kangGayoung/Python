phoneList = []
numOfData = 0

#1.전화번호 추가
def inputData():
    name = input("이름 입력 : ")
    number = input("번호 입력 : ")
    phoneList.append({"name": name, "number": number})
    global numOfData
    numOfData += 1

# # 2.전화번호 검색
# def serch(name):
#     for i in range(0, len(phoneList)):
#         if name in phoneList[i][0]:
#             #

#4.전화번호 전체출력
def showAllData():
    for data in phoneList:
        print("------------------------")
        print("이름 : ", data["name"])
        print("번호 : ", data["number"])
        print("------------------------")

while True:
    print("===============================")
    print("현재 데이터 개수 :  {}개".format(numOfData))
    print("1.전화번호 추가")
    print("2.전화번호 검색")
    print("3.전화번호 삭제")
    print("4.전화번호 전체출력")
    print("5.종료")
    print("===============================")
    menu = int(input("선택 >> "))
    if menu == 1:
        # name = input("이름 입력 : ")
        # number = input("번호 입력 : ")
        # phoneList.append({"name":name, "number":number})
        # numOfData += 1

        inputData()

    elif menu == 2:
        pass
    elif menu == 3:
        pass
    elif menu == 4:
        # for data in phoneList:
        #     print("------------------------")
        #     print("이름 : ", data["name"])
        #     print("번호 : ", data["number"])
        #     print("------------------------")
        showAllData()

    elif menu == 5:
        print("종료 되었습니다.")
        break
    else:
        print("올바른 선택이 아닙니다.")