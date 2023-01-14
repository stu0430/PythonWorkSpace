import re

# 정규 표현식 패턴
regex = re.compile('(\d{6})-(\d{1})(\d{6})')

n = int(input('입력할 주민등록번호의 개수를 입력하세요 : '))

# 파일 입력
with open('people.txt', 'w', encoding='utf-8') as file:
    for i in range(n):
        person = input('이름과 주민등록번호를 입력하세요 (ex. Lee 642738-4723781) : ')
        file.write(person+'\n')

# 파일 출력
with open('people.txt', 'r', encoding='utf-8') as file:
    for person in file:
        # 주민등록번호의 뒤 6자리를 *로 치환
        new_num = regex.sub(r'\1-\2******', person)
        print(new_num.strip())