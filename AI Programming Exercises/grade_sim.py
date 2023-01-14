import time
import random
import numpy as np
from util import util

INIT_STD_ID = 20220001
NUM_STD = 30

def genVars():
    subjects = [{'name' : '과목A', 'credit' : 3},
                {'name' : '과목B', 'credit' : 3}, 
                {'name' : '과목C', 'credit' : 3}, 
                {'name' : '과목D', 'credit' : 3}, 
                {'name' : '과목E', 'credit' : 3}, 
                {'name' : '과목F', 'credit' : 2}, 
                {'name' : '과목G', 'credit' : 2},
                {'name' : '과목H', 'credit' : 2}]
    
    studentIDs = [str(i) for i in range(INIT_STD_ID, INIT_STD_ID + NUM_STD)]
    
    exams = ['midterm', 'final']
    
    return subjects, studentIDs, exams

def genScoreData(subjects, studentIDs, exams):
    scoreData = {}
    
    for subject in subjects:
        scoreData[subject['name']] = {}    
        for exam in exams:
            mean = round(random.gauss(50, 15), 2)
            std = round(random.gauss(15, 5), 2)
            
            scoreData[subject['name']][exam] = {'scores' : {}, 'average' :  {}, 'stdev' : {}}
            
            for studentID in studentIDs:
                score = round(random.gauss(mean, std), 2)
                
                if score > 100:
                    score = 100
                    
                elif score < 0:
                    score = 0
                    
                scoreData[subject['name']][exam]['scores'][studentID] = score  
                 
            scoreData[subject['name']][exam]['average']['config'] = mean
            scoreData[subject['name']][exam]['average']['real'] = round(np.mean(list(scoreData[subject['name']][exam]['scores'].values())), 2)
            
            scoreData[subject['name']][exam]['stdev']['config'] = std
            scoreData[subject['name']][exam]['stdev']['real'] = round(np.std(list(scoreData[subject['name']][exam]['scores'].values())), 2)
            
    return scoreData

def calcScores(scoreData):
    for subject in scoreData:
        scoreData[subject]['total'] = {'scores': {}, 'average':  {}, 'stdev': {}}
        for studentID in scoreData[subject]['midterm']['scores']:
            scoreData[subject]['total']['scores'][studentID] = round(scoreData[subject]['midterm']['scores'][studentID] * 0.5 + scoreData[subject]['final']['scores'][studentID] * 0.5, 2)
       
        scoreData[subject]['total']['average']['config'] = round(scoreData[subject]['midterm']['average']['config'] * 0.5 + scoreData[subject]['final']['average']['config'] * 0.5, 2)
        scoreData[subject]['total']['average']['real'] = round(np.mean(list(scoreData[subject]['total']['scores'].values())), 2)
        
        scoreData[subject]['total']['stdev']['config'] = round(scoreData[subject]['midterm']['stdev']['config'] * 0.5 + scoreData[subject]['final']['stdev']['config'] * 0.5, 2)
        scoreData[subject]['total']['stdev']['real'] = round(np.std(list(scoreData[subject]['total']['scores'].values())), 2)   
        
    return scoreData
    
def calcGrades(scoreData):
    for subject in scoreData:
        scores = scoreData[subject]['total']['scores']
        scores = sorted(scores.items(), key=lambda score: score[1], reverse=True)
        scores = [0] + scores

        grades = []
        for i in scores:
            if scores.index(i) == 0:
                pass
            
            elif scores.index(i) <= int((len(scores) - 1) * 0.15):
                grades.append((i[0], 'A+'))
                
            elif scores.index(i) <= int((len(scores) - 1) * 0.3):
                grades.append((i[0], 'A')) 
                              
            elif scores.index(i) <= int((len(scores) - 1) * 0.45):
                grades.append((i[0], 'B+'))
                
            elif scores.index(i) <= int((len(scores) - 1) * 0.6):
                grades.append((i[0], 'B'))       
                        
            elif scores.index(i) <= int((len(scores) - 1) * 0.75):
                grades.append((i[0], 'C+'))
                
            elif scores.index(i) <= int((len(scores) - 1) * 0.9):
                grades.append((i[0], 'C'))    
                            
            elif scores.index(i) <= int((len(scores) - 1) * 0.95):
                grades.append((i[0], 'D+'))
                
            else:
                grades.append((i[0], 'D')) 

        grades = sorted(grades, key=lambda score: score[0])
        grades = dict(grades)
        scoreData[subject]['grade'] = grades

    return scoreData

def calcStuData(scoreData, studentID, subjects):
    stuData = {}
    
    stuData['ID'] = studentID
    stuData['scores'] = {}
    
    credit_sum = 0
    score = 0
    
    grades = {'A+': 4.5, 'A': 4.0, 'B+': 3.5, 'B': 3.0,
              'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0}
    
    for subject in subjects:
        stuData['scores'][subject['name']] = {'midterm' : scoreData[subject['name']]['midterm']['scores'][studentID],
                                              'final' : scoreData[subject['name']]['final']['scores'][studentID],
                                              'average' : scoreData[subject['name']]['total']['scores'][studentID],
                                              'grade' : scoreData[subject['name']]['grade'][studentID]}
        
        score += grades[stuData['scores'][subject['name']]['grade']] * subject['credit']
        credit_sum += subject['credit']
        
    stuData['GPA'] = round(score / credit_sum, 2)
    
    return stuData

def printSubScores(scoreData, subject, sort=None):
    scores = scoreData[subject]['total']['scores']
    
    if sort == 'ascending':
        scores = sorted(scores.items(), key = lambda score: score[1])
        
    elif sort == 'descending':
        scores = sorted(scores.items(), key = lambda score: score[1], reverse=True)
    
    scores = dict(scores)
    
    print(f'Subject : {subject}')
    util.char_line('-', 38)
    print()
    print(f"{'ID':^8} {'Midterm':^6} {'Final':^7} {'Total':^5} {'Grade':^8}")
    util.char_line('-', 38)
    print()
    
    if sort != None:
        for studentID in scores.keys():
            print(f'{studentID} {scoreData[subject]["midterm"]["scores"][studentID]:^8} {scoreData[subject]["final"]["scores"][studentID]:^6} {scoreData[subject]["total"]["scores"][studentID]:^6} {scoreData[subject]["grade"][studentID]:^6}')
    
    else:
        for studentID in scoreData[subject]['total']['scores']:
            print(f'{studentID} {scoreData[subject]["midterm"]["scores"][studentID]:^8} {scoreData[subject]["final"]["scores"][studentID]:^6} {scoreData[subject]["total"]["scores"][studentID]:^6} {scoreData[subject]["grade"][studentID]:^6}')
    
    util.char_line('-', 23)
    for exam in scoreData[subject]:
        if exam == 'grade':
            break
        else:
            print(f'\n{exam:^23}')
            util.char_line('-', 23)
            print(f"\nconfig average : {scoreData[subject][exam]['average']['config']}")
            print(f"real average   : {scoreData[subject][exam]['average']['real']}")
            print(f"config stdev   : {scoreData[subject][exam]['stdev']['config']}")
            print(f"real stdev     : {scoreData[subject][exam]['stdev']['real']}")
            util.char_line('-', 23)
    
def printStuGPAs(stuData, sort=None):
    grades = [(subject, stuData['scores'][subject]['grade']) for subject in stuData['scores']]
    
    if sort == 'ascending':
        grades = sorted(grades, key=lambda grade: (grade[1][0], -len(grade[1])), reverse=True)
        
    elif sort == 'descending':
        grades = sorted(grades, key = lambda grade: (grade[1][0], -len(grade[1])))

    print(f'ID : {stuData["ID"]}')
    util.char_line('-', 15)
    print()
    print(f'{"Subject":^6} {"Grade":^8}')
    util.char_line('-', 15)
    print()
    if sort != None:
        for subject, grade in grades:
            print(f'{subject:^6} {grade:^6}')
    else:
        for subject in stuData['scores']:
            print(f'{subject:^6} {stuData["scores"][subject]["grade"]:^6}')

def printGPAStat(stuDatas):
    grades = [stuData['GPA'] for stuData in stuDatas]
    grades.sort(reverse=True)
    
    a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0

    for grade in grades:
        if grade >= 4.0:
            a += 1
        elif grade >= 3.5:
            b += 1
        elif grade >= 3.0:
            c += 1
        elif grade >= 2.5:
            d += 1
        elif grade >= 2.0:
            e += 1
        elif grade >= 1.5:
            f += 1
        else:
            g += 1
            
    print(f'4.0 이상 : {round(a / len(grades) * 100, 2)}%')
    print(f'3.5 이상 ~ 4.0 미만 : {round(b / len(grades) * 100, 2)}%')
    print(f'3.0 이상 ~ 3.5 미만 : {round(c / len(grades) * 100, 2)}%')
    print(f'2.5 이상 ~ 3.0 미만 : {round(d / len(grades) * 100, 2)}%')
    print(f'2.0 이상 ~ 2.5 미만 : {round(e / len(grades) * 100, 2)}%')
    print(f'1.5 이상 ~ 2.0 미만 : {round(f / len(grades) * 100, 2)}%')
    print(f'1.5 미만 : {round(g / len(grades) * 100, 2)}%')

def main():
    util.print_header("Grade Simulator", "2022.12.07", "(c) Lee, Sang-gwon")
    
    while True:
        # 변수 생성
        subjects, studentIDs, exams = genVars()

        # 성적 데이터 생성
        scoreData = genScoreData(subjects, studentIDs, exams)

        # 성적 산출
        scoreData = calcScores(scoreData)

        # 학점 산출
        scoreData = calcGrades(scoreData)

        # 개인 성적 데이터 산출
        stuDatas = [calcStuData(scoreData, studentID, subjects) for studentID in studentIDs]
        
        time.sleep(1)
        
        print('>>> 데이터 생성 및 산출이 완료되었습니다.')
        
        choice = util.int_get('>>> 메뉴를 선택하세요.(1.시뮬레이션 결과 보기  2.종료) : ', minval=1, maxval=2, default=1)
        
        if choice == 1: 
            while True: 
                menusel = util.int_get('>>> 메뉴를 선택하세요.(1.과목별 성적 명렬표  2.학생별 평점 명렬표  3.평점 구간별 비율  4.종료) : ', minval=1, maxval=4, default=1)

                if menusel == 1:
                    sort = util.int_get('>>> 정렬 방식을 선택하세요.(1.정렬 안함  2.오름차순  3.내림차순) : ', minval=1, maxval=3, default=1)

                    if sort == 1:
                        sort = None
                    elif sort == 2:
                        sort = 'ascending'
                    elif sort == 3:
                        sort = 'descending'

                    for subject in subjects:
                        printSubScores(scoreData, subject['name'], sort)
                        print()

                elif menusel == 2:
                    sort = util.int_get('>>> 정렬 방식을 선택하세요.(1.정렬 안함  2.오름차순  3.내림차순) : ', minval=1, maxval=3, default=1)

                    if sort == 1:
                        sort = None
                    elif sort == 2:
                        sort = 'ascending'
                    elif sort == 3:
                        sort = 'descending'

                    for stuData in stuDatas:
                        printStuGPAs(stuData, sort)

                elif menusel == 3:
                    printGPAStat(stuDatas)

                else:
                    break
        else:
            print('>>> 프로그램을 종료합니다.')
            break
    
if __name__ == '__main__':
    main()
