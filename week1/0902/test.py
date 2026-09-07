# 변수를 이용해보자~

# title = "AI 서비스 백엔드 프로그래밍 실무"
# line = "=========="
# time = 8
# a = "파이썬 기본 문법"
# b = "클래스"
# c = "데코레이터"
# d = "예외 처리"
# e = "로깅"
# print(title)
# print(line)
# print(a, time, sep=", 시간:")
# print(b, time, sep=", 시간:")
# print(c, time, sep=", 시간:")
# print(d, time, sep=", 시간:")
# print(e, time, sep=", 시간:")

# 리스트를 이용해 보자~

# title='AI 서비스 백엔드 프로그래밍 실무'
# line='=========='
# time=8
# myList=['파이썬 기본 문법','클래스','데코레이터','예외 처리','로깅']
# print(title)
# print(line)
# print(myList[0],time,sep=', 시간:')
# print(myList[1],time,sep=', 시간:')
# print(myList[2],time,sep=', 시간:')
# print(myList[3],time,sep=', 시간:')
# print(myList[4],time,sep=', 시간:')

# for문을 이용해보자~

title='AI 서비스 백엔드 프로그래밍 실무'
line='=========='
time=8
myList=['파이썬 기본 문법','클래스','데코레이터','예외 처리','로깅']
print(title)
print(line)

for x in myList:
    print(x,time,sep=', 시간:')