# 링크
# https://www.acmicpc.net/problem/5635

# 생일

# 문제
# 어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 반에 있는 학생의 수 n이 주어진다. (1 ≤ n ≤ 100)

# 다음 n개 줄에는 각 학생의 이름과 생일이 "이름 dd mm yyyy"와 같은 형식으로 주어진다. 이름은 그 학생의 이름이며, 최대 15글자로 이루어져 있다. dd mm yyyy는 생일 일, 월, 연도이다. (1990 ≤ yyyy ≤ 2010, 1 ≤ mm ≤ 12, 1 ≤ dd ≤ 31) 주어지는 생일은 올바른 날짜이며, 연, 월 일은 0으로 시작하지 않는다.

# 이름이 같거나, 생일이 같은 사람은 없다.

# 출력
# 첫째 줄에 가장 나이가 적은 사람의 이름, 둘째 줄에 가장 나이가 많은 사람 이름을 출력한다.

# 예제 입력
# 5
# Mickey 1 10 1991
# Alice 30 12 1990
# Tom 15 8 1993
# Jerry 18 9 1990
# Garfield 20 9 1990

# 예제 출력
# Tom
# Jerry

# 함수1 ----------------------------------------------------------
def solution1():
    n = int(input())
    nameList = []
    birthList = []
    studentList = []

    for _ in range(n):
        name, day, month, year = input().split()
        month = month if len(month) > 1 else '0'+month
        day = day if len(day) > 1 else '0' + day
        birthday = year + month + day

        birthList.append(int(birthday))
        studentList.append(name)

    nameList.append(studentList[birthList.index(max(birthList))])
    nameList.append(studentList[birthList.index(min(birthList))])
    return nameList


# 함수2 ----------------------------------------------------------
def solution2():
    n = int(input())
    nameList = []
    dic = {}

    for _ in range(n):
        name, day, month, year = input().split()
        month = month if len(month) > 1 else '0'+month
        day = day if len(day) > 1 else '0' + day
        birthday = year + month + day

        dic[int(birthday)] = name

    nameList.append(dic[max(dic.keys())])
    nameList.append(dic[min(dic.keys())])
    return nameList


# 실행 ------------------------------------------------------------
for i in solution1():
    print(i)

for i in solution2():
    print(i)
