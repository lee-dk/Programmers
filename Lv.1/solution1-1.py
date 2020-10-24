# 두 개 뽑아서 더하기
""" 문제
    정수 배열 numbers가 주어집니다. 
    numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 
    더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 
    return 하도록 solution 함수를 완성해주세요.
"""
''' 제한사항
    numbers의 길이는 2 이상 100 이하입니다.
    numbers의 모든 수는 0 이상 100 이하입니다.
'''
#풀이
def solution1(numbers):
    answer = []
    if len(numbers) >= 2 and len(numbers) <= 100:
        for i in range(len(numbers)-1) :
            for j in range(i+1, len(numbers)) :
                num = numbers[i] + numbers[j]
                if (num not in answer) :
                    answer.append(num)                
    answer.sort()
    return answer

# 다른 사람의 풀이
def solution2(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))