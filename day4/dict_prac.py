"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

# 1번 풀이
total = 0
count = 0

for value in score.values():
    total += value
    count += 1

print('전체 평균은', total/len(score), '입니다.')
print('전체 평균은', total/count, '입니다.') # 동일

# 2번 풀이
total2 = sum(score.values())
print(total2)
count = len(score)
print(total2/count)


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

count2 = 0
total_score = 0
for person_scores in scores.values():
    for score in person_scores.values():
        total_score += score
        count2 += 1
print('반 평균은', total_score/count2, '입니다.')


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""

for name, temp in city.items():
    avg = sum(temp)/len(temp)
    print(f'{name} : {avg:.2f}')
    print('{} : {:.2f}'.format(name, avg))
    print(name, ':', avg)
    

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

min_temp = 0
max_temp = 0
min_city = ''
max_city = ''
# 모든 지역의 온도를 확인하면서,
for name, temp in city.items():
    # 초기화/첫번째 반복때는 모두 다 저장해!
    if count == 0:
        min_city = name
        max_city = name
        min_temp = min(temp)
        max_temp = max(temp)
        count += 1
# 가장 추우면, 해당 도시와 기온을 기록
    if min(temp) < min_temp:
        min_city = name
        min_temp = min(temp)
# 더울 때도, 해당 도시와 기온을 기록
    if max(temp) > max_temp:
        max_city = name
        max_temp = max(temp)
print(f'추운 곳은 {min_city}, 더운 곳은 {max_city}')


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
# for문에서 in : 그 안에
# if문에서 in : 그 값이 있니?
# 0 in range(5) -> false
if 2 in city['서울']:
    print('네')
else:
    print('아뇨')