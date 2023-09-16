#1-1. 로또 당첨 번호를 리스트에 저장하기

# 아래에 코딩하세요
# 1. for문 or while문 반드시 사용하기
# 2. random.randint() 활용하기

# 랜덤 로또 번호 출력
import random
lotto = []

for i in range(6):
    num = random.randint(1,45)
    if num not in lotto:
        lotto.append(num)

print(lotto)

#1-2. 로또 당첨 여부 출력하기 (당첨될 때까지 반복)
my_lotto = [13,23,33,43,44,45]

# 각자 좋아하는 숫자로 바꿔도 됩니다.
# 아래에 코딩하세요
# 1. set 자료형 활용하기
# 2. while문 활용하기

# 결과 예시
# 1개 : 낙첨
# 3개 : 당첨
import random

# 당첨 번호
winner_number = set([1, 3, 5, 7, 9, 11])

# 내 로또 번호
my_lotto = [2, 4, 6, 8, 10, 12]

def check_lotto_numbers(my_lotto, winner_number):
    matching_numbers = set(my_lotto).intersection(winner_number)
    return len(matching_numbers)

attempts = 0
while True:
    lotto = [] #당첨 번호를 랜덤으로 바꾸는....것

    for i in range(6):
        num = random.randint(1,45)
        if num not in lotto:
            lotto.append(num)
    attempts += 1
    matching_count = check_lotto_numbers(my_lotto, lotto)
    
    if matching_count >= 3:
        print(f"{attempts}번째 시도: {matching_count}개 일치")
        break
    else:
        print(f"{attempts}번째 시도: {matching_count}개 일치{' (낙첨)' if matching_count < 3 else ''}")

'''
#답안과 비교해보기
my_lotto=[13,23,33,43,44,45]

while True:
    lotto =[]

    while len(lotto) < 6:
        num = random.randint(1,45)
        if num not in lotto: #중복 안되게
            lotto.append(num)
    if len(set(lotto).intersection(my_lotto)) >=3:
        print(f"{len(set(lotto). intersection(my_lotto))}개 : 당첨")
         break
    else:
        print(f"{len(set(lotto).intersection(my_lotto))}개 : 낙첨")
'''
