year = int(input("당신이 태어난 연도를 입력하세요."))

age = 2020 - year + 1
if age <= 26 and age >= 20:
    print('대학생')
elif age < 20 and age >= 17:
    print('고등학생')
elif 17 > age and age >=14:
    print('중학생')
elif 14 > age and age >= 8:
    print('초등학생')
else:
    print('학생이 아닙니다.')