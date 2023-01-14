from util import util

class Book():
    def __init__(self, title, author, publisher, year, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.isbn = isbn
        self.rent = False
        self.reservation = False
        self.renter = ''
        self.reserver = ''

    def rentBook(self):
        if self.rent:
            raise AbortTransaction('>>> [ERROR] 대출 중인 도서입니다.\n')
        else:
            self.rent = True
            
    def returnBook(self):
        if self.rent:
            self.rent = False
        else:
            raise AbortTransaction('>>> [ERROR] 대출 중인 도서가 아닙니다.\n')
        
    def reserveBook(self):
        if self.reservation:
            raise AbortTransaction('>>> [ERROR] 이미 예약된 도서입니다.\n')
        else:
            self.reservation = True
            
    def cancelReservation(self):    
        if self.reservation:
            self.reservation = False
        else:
            raise AbortTransaction('>>> [ERROR] 예약된 도서가 아닙니다.\n')
        
    def bookInfo(self):
        print(f'제목 : {self.title}')
        print(f'저자 : {self.author}')
        print(f'출판사 : {self.publisher}')
        print(f'출판 연도: {self.year}')
        print(f'ISBN : {self.isbn}')
        print(f'대출 여부 : {"O" if self.rent else "X"}')
        print(f'예약 여부 : {"O" if self.reservation else "X"}\n')

class Member():
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.rentalList = []
        self.reserveList = []
    
    def rentBook(self, book):
        book.rentBook()
        book.renter = self.name
        self.rentalList.append(book)
            
    def returnBook(self, book):
        book.returnBook()
        book.renter = ''
        self.rentalList.remove(book)
            
    def reserveBook(self, book):
        book.reserveBook()
        book.reserver = self.name
        self.reserveList.append(book)
        
    def cancelReservation(self, book):
        book.cancelReservation()
        book.reserver = ''
        self.reserveList.remove(book)
            
    def memberInfo(self):
        print(f'이름 : {self.name}')
        print(f'학번 : {self.num}')
        print(f'대출 목록 : {[book.title for book in self.rentalList] if len(self.rentalList) != 0 else "없음"}')
        print(f'예약 목록 : {[book.title for book in self.reserveList] if len(self.reserveList) != 0 else "없음"}\n')
    
class Library():
    def __init__(self):
        self.books = []
        self.members = []
        
    def addBook(self):
        print('\n[도서 등록]')
        title = input('>>> 도서 제목을 입력하세요 : ')
        author = input('>>> 도서 저자를 입력하세요 : ')
        publisher = input('>>> 도서 출판사를 입력하세요 : ')
        year = int(input('>>> 도서 출판년도를 입력하세요 : '))
        isbn = int(input('>>> 도서 ISBN을 입력하세요 : '))
        book = Book(title, author, publisher, year, isbn)
        self.books.append(book)
        print('>>> 도서 등록이 완료되었습니다.\n')
    
    def addMember(self):
        print('\n[회원 등록]')
        name = input('>>> 회원 이름을 입력하세요 : ')
        num = int(input('>>> 회원 학번을 입력하세요 : '))
        member = Member(name, num)
        self.members.append(member)
        print('>>> 회원 등록이 완료되었습니다.\n')
        
    def rentBook(self):
        print('\n[도서 대출]')
        member = input('>>> 대출할 회원의 이름을 입력하세요 : ') 
        for m in self.members:
            if m.name == member:
                book = input('>>> 대출할 도서의 제목을 입력하세요 : ')
                for b in self.books:
                    if b.title == book and b.renter != m.name:
                        m.rentBook(b)
                        print('>>> 대출되었습니다.\n')
                        break
                else:
                    raise AbortTransaction('>>> [ERROR] 도서 정보가 없습니다.\n')
                break
        else:
            raise AbortTransaction('>>> [ERROR] 회원 정보가 없습니다.\n')
            
    def returnBook(self):
        print('\n[도서 반납]')
        member = input('>>> 반납할 회원의 이름을 입력하세요 : ')
        for m in self.members:
            if m.name == member:
                book = input('>>> 반납할 도서의 제목을 입력하세요 : ')
                for b in self.books:
                    if b.title == book and b.renter == m.name:
                        m.returnBook(b)
                        print('>>> 반납되었습니다.\n')
                        if b.reservation:
                            for m in self.members:
                                if b in m.reserveList:
                                    m.rentBook(b)
                                    m.cancelReservation(b)
                                    print(f'>>> {m.name}님의 예약 도서가 대출되었습니다.\n')
                                    break
                        break
                else:
                    raise AbortTransaction('>>> [ERROR] 도서 정보가 없습니다.\n')
                break
        else:
            raise AbortTransaction('>>> [ERROR] 회원 정보가 없습니다.\n')
        
    def reserveBook(self):
        print('\n[도서 예약]')
        member = input('>>> 예약할 회원의 이름을 입력하세요 : ')
        for m in self.members:
             if m.name == member:
                book = input('>>> 예약할 도서의 제목을 입력하세요 : ')
                for b in self.books:
                    if b.title == book and b.reserver != m.name:
                        m.reserveBook(b)
                        print('>>> 예약되었습니다.')
                        print('>>> 대출된 도서가 반납되면 예약된 도서가 대출됩니다.\n')
                        break
                else:
                    raise AbortTransaction('>>> [ERROR] 도서 정보가 없습니다.\n')
                break
        else:
            raise AbortTransaction('>>> [ERROR] 회원 정보가 없습니다.\n')
        
    def reserveCancel(self):
        print('\n[예약 취소]')
        member = input('>>> 예약 취소할 회원의 이름을 입력하세요 : ')
        for m in self.members:
            if m.name == member:
                book = input('>>> 예약 취소할 도서의 제목을 입력하세요 : ')
                for b in self.books:
                    if b.title == book and b.reserver == m.name:
                        m.cancelReserve(b)
                        print('>>> 예약이 취소되었습니다.\n')
                        break
                else:
                    raise AbortTransaction('>>> [ERROR] 도서 정보가 없습니다.\n')
                break
        else:
            raise AbortTransaction('>>> [ERROR] 회원 정보가 없습니다.\n')
            
    def membersInfo(self):
        print('\n[전체 회원 정보]')
        if len(self.members) == 0:
            raise AbortTransaction('>>> [ERROR] 회원 정보가 없습니다.\n')
        
        for m in self.members:
            m.memberInfo()
            
    def booksInfo(self):
        print('\n[전체 도서 정보]')
        if len(self.books) == 0:
            raise AbortTransaction('>>> [ERROR] 도서 정보가 없습니다.\n')
        
        for b in self.books:
            b.bookInfo()
            
    def rentalInfo(self):
        print('\n[대출 현황]')
        rentCnt = 0
        for b in self.books:
            if b.rent:
                rentCnt = 1
                print(f'>>> {b.title} : {b.renter}\n')
                
        if rentCnt == 0:
            raise AbortTransaction('>>> [ERROR] 대출된 도서가 없습니다.\n')
                
    def reservationInfo(self):
        print('\n[예약 현황]')
        rsvCnt = 0
        for b in self.books:
            if b.reservation:
                rsvCnt = 1
                print(f'>>> {b.title} : {b.reserver}\n')
                
        if rsvCnt == 0:
            raise AbortTransaction('>>> [ERROR] 예약된 도서가 없습니다.\n')
                
    def searchBook(self):
        print('\n[도서 검색]')
        searchMethod = ['제목', '저자', '출판사', 'ISBN']
        while True:
            methodSel = util.int_get('>>> 검색 방법을 선택하세요.(1.제목, 2.저자, 3.출판사, 4.ISBN, 5.종료) : ', minval=1, maxval=5, default=1)
            if methodSel == 5:
                print('>>> 검색을 종료합니다.\n')
                break
            else:
                search = input(f'>>> 검색할 도서의 {searchMethod[methodSel - 1]}을(를) 입력하세요 : ')
                for b in self.books:
                    if methodSel == 1 and search in b.title:
                        b.bookInfo()
                        break
                    elif methodSel == 2 and search in b.author:
                        b.bookInfo()
                        break
                    elif methodSel == 3 and search in b.publisher:
                        b.bookInfo()
                        break
                    elif methodSel == 4 and search in str(b.isbn):
                        b.bookInfo()
                        break
                else:
                    raise AbortTransaction('>>> [ERROR] 도서 정보가 없습니다.\n')

class AbortTransaction(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

def menu(msg, menuList):
    print('[Menu]')
    for i in range(len(menuList)):
        print(f'{i+1}. {menuList[i]}')
    print('0. 종료')
    while True:
        try:
            num = int(input(msg))
            if num == 0:
                break
            elif num > 0 and num <= len(menuList):
                return num
            else:
                print(f'>>> [ERROR] 0 ~ {len(menuList)} 사이의 숫자를 입력하세요.')
        except:
            print('>>> [ERROR] 숫자를 입력하세요.')

def main():
    util.print_header("3-3 Library management", "2022.11.19", "(c) Lee, Sang-gwon")
    
    lib = Library()
    
    msg = '>>> 원하는 업무를 선택하세요 : '
    libMenuList = ['도서 등록', '대출 현황 보기', '예약 현황 보기', '전체 회원 보기']
    userMenuList = ['회원 등록', '도서 대출', '도서 반납', '도서 예약', '예약 취소', '도서 검색', '전체 도서 보기']
    
    while True:
        menuSel = util.int_get('\n>>> 메뉴를 선택하세요.(1.도서관 관리 2.사용자 서비스  3.종료) : ', minval=1, maxval=3, default=1)
        
        if menuSel == 1:
            while True:
                sel = menu(msg, libMenuList)
                
                try:
                    if sel == 1:
                        lib.addBook()
                    elif sel == 2:
                        lib.rentalInfo()
                    elif sel == 3:
                        lib.reservationInfo()
                    elif sel == 4:
                        lib.membersInfo()
                    else:
                        break
                
                except AbortTransaction as error:
                    print(error)
                    continue
                
        elif menuSel == 2:
            while True:
                sel = menu(msg, userMenuList)
                
                try:
                    if sel == 1:
                        lib.addMember()
                    elif sel == 2:
                        lib.rentBook()
                    elif sel == 3:
                        lib.returnBook()
                    elif sel == 4:
                        lib.reserveBook()
                    elif sel == 5:
                        lib.reserveCancel()
                    elif sel == 6:
                        lib.searchBook()
                    elif sel == 7:
                        lib.booksInfo()
                    else:
                        break
                    
                except AbortTransaction as error:
                    print(error)
                    continue
                  
        else:
            print('>>> 프로그램을 종료합니다.')
            break

if __name__ == '__main__':
    main()
