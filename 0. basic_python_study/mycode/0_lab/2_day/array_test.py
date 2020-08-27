# 2차원 배열
# 학생별 과목의 평균을 계산

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]

midterm_score = [kor_score, math_score, eng_score]

print(midterm_score[0])
print(midterm_score[1])
print(midterm_score[2])
print(midterm_score[0][2])

print('')
print('학생 점수 평균', '-' * 5)

# 학생별 과목의 합계를 저장할 리스트
# 중첩된 for 루프 안에서 학생별 과목 점수 합계를 저장한다.
# 과목이 바뀌면 학생을 구분하는 인덱스 값을 초기화 해야 합니다.
student_score = [0, 0, 0, 0, 0]

# 학생을 구분하기 위한 인덱스
idx = 0

for subject in midterm_score:  # 과목 점수 loop
    print('subject ', subject)
    for score in subject:
        # print(score)
        student_score[idx] += score # 각 학생마다 개별로 과목점수를 누적
        print(student_score[idx])
        # 학생 인덱스 구분
        idx += 1    # packing
    print('----------')
    # 과목이 바뀔때 마다 학생 인덱스를 초기화
    idx = 0

else:
    print('학생별 누적 점수', student_score)
    a, b, c, d, e = student_score # unpacking
    student_average = [int(a/3), int(b/3), int(c/3), int(d/3), int(e/3)]
    print('학생별 평균 점수', student_average)