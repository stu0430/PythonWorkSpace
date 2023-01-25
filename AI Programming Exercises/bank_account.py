import datetime
from util import util

class Account():
    def __init__(self, name, balance, password, accountNum):
        self.name = name
        self.balance = balance
        self.password = password
        self.accountNum = accountNum

    def deposit(self, amount, password):
        if password != self.password:
            raise AbortTransaction('>>> [ERROR] 비밀번호가 일치하지 않습니다.\n')
        
        if amount <= 0:
            raise AbortTransaction('>>> [ERROR] 0이나 음수의 금액은 입금할 수 없습니다.\n')
        
        self.balance += amount

        return self.balance

    def withdraw(self, amount, password):
        if password != self.password:
            raise AbortTransaction('>>> [ERROR] 비밀번호가 일치하지 않습니다.\n')
        
        if amount <= 0:
            raise AbortTransaction('>>> [ERROR] 0이나 음수의 금액은 출금할 수 없습니다.\n')
        
        self.balance -= amount
        
        return self.balance

    def getBalance(self, accountNum, password):
        if password != self.password:
            raise AbortTransaction('>>> [ERROR] 비밀번호가 일치하지 않습니다.\n')
        
        if accountNum != self.accountNum:
            raise AbortTransaction('>>> [ERROR] 계좌번호가 일치하지 않습니다.\n')
        
        return self.balance

    def show(self, accountNum, password):
        if password != self.password:
            raise AbortTransaction('>>> [ERROR] 비밀번호가 일치하지 않습니다.\n')
        
        if accountNum != self.accountNum:
            raise AbortTransaction('>>> [ERROR] 계좌번호가 일치하지 않습니다.\n')
        
        print(f'이름 : {self.name}')
        print(f'잔고 : {self.balance}원')
        print(f'계좌번호 : {self.accountNum}')

class Bank():
    def __init__(self):
        self.accountList = []

    def createAccount(self, name, amount, password):
        today = datetime.date.today()
        year = str(today.year)
        lastNo = str(len(self.accountList)).zfill(4)
        accountNum = year + '-' + lastNo
        
        Account(name, amount, password, accountNum)
        
        newAccount = Account(name, amount, password, accountNum)
        
        self.accountList.append(newAccount)
        
        return accountNum

    def openAccount(self):
        print('\n[계좌 개설]')
        
        name = input('>>> 계좌를 개설할 사용자의 이름을 입력하세요 : ')
        sAmount = int(input('>>> 계좌 개설 시 입금할 금액을 입력하세요 : '))
        password = input('>>> 계좌의 비밀번호를 입력하세요 : ')
        
        accountNum = self.createAccount(name, sAmount, password)
        
        print(f'>>> 당신의 계좌번호는 {accountNum} 입니다.\n')

    def closeAccount(self):
        print('\n[계좌 폐쇄]')
        accountNum = input('>>> 폐쇄할 계좌의 계좌번호를 입력하세요 : ')

        accountidx = int(accountNum[5:])
        if accountidx < 0 or accountidx >= len(self.accountList):
            raise AbortTransaction('>>> [ERROR] 계좌번호가 바르지 않습니다.\n')

        curAccount = self.accountList[accountidx]

        password = input('>>> 계좌의 비밀번호를 입력하세요 : ')

        if password != curAccount.password:
            raise AbortTransaction('>>> [ERROR] 비밀번호가 일치하지 않습니다.\n')

        del self.accountList[accountidx]

        print('>>> 계좌가 성공적으로 폐쇄되었습니다.\n')

    def deposit(self):
        print('\n[입금]')
        accountNum = input('>>> 사용자의 계좌번호를 입력하세요 : ')

        accountidx = int(accountNum[5:])
        if accountidx < 0 or accountidx >= len(self.accountList):
            raise AbortTransaction('>>> [ERROR] 계좌번호가 바르지 않습니다.\n')

        curAccount = self.accountList[accountidx]

        amount = int(input('>>> 입금할 금액을 입력하세요 : '))

        password = input('>>> 계좌의 비밀번호를 입력하세요 : ')

        newBalance = curAccount.deposit(amount, password)

        print(f'>>> 당신의 현재 잔고는 {newBalance}원 입니다.\n')

    def withdraw(self):
        print('\n[출금]')
        accountNum = input('>>> 사용자의 계좌번호를 입력하세요 : ')

        accountidx = int(accountNum[5:])
        if accountidx < 0 or accountidx >= len(self.accountList):
            raise AbortTransaction('>>> [ERROR] 계좌번호가 바르지 않습니다.\n')
        
        curAccount = self.accountList[accountidx]

        amount = int(input('>>> 출금할 금액을 입력하세요 : '))

        password = input('>>> 계좌의 비밀번호를 입력하세요 : ')

        newBalance = curAccount.withdraw(amount, password)

        print(f'>>> 당신의 현재 잔고는 {newBalance}원 입니다.\n')
    
    def getBalance(self):
        print('\n[잔액 조회]')
        accountNum = input('>>> 사용자의 계좌번호를 입력하세요 : ')

        accountidx = int(accountNum[5:])
        if accountidx < 0 or accountidx >= len(self.accountList):
            raise AbortTransaction('>>> [ERROR] 계좌번호가 바르지 않습니다.\n')

        curAccount = self.accountList[accountidx]

        password = input('>>> 계좌의 비밀번호를 입력하세요 : ')

        balance = curAccount.getBalance(password)

        print(f'>>> 당신의 현재 잔고는 {balance}원 입니다.\n')

    def show(self):
        print('\n[전체 계좌 조회]')
        
        if self.accountList == []:
            print('>>> [ERROR] 계좌가 존재하지 않습니다.\n')
        
        else:
            for account in self.accountList:
                account.show(account.accountNum, account.password)
                print()
    
class AbortTransaction(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

def main():
    util.print_header("Bank Account", "2023.01.25", "(c) Lee, Sang-gwon")

    bank = Bank()

    msg = '>>> 원하는 업무를 선택하세요 : '
    choiceList = ['계좌 개설', '계좌 폐쇄', '입금', '출금', '잔액 조회', '전체 계좌 조회']

    while True:
        choice = util.menu(msg, choiceList)

        try:
            if choice == 1:
                bank.openAccount()

            elif choice == 2:
                bank.closeAccount()

            elif choice == 3:
                bank.deposit()

            elif choice == 4:
                bank.withdraw()
                
            elif choice == 5:
                bank.getBalance()
                
            elif choice == 6:
                bank.show()

            else:
                print('>>> 프로그램을 종료합니다.')
                break

        except AbortTransaction as error:
            print(error)
            continue

if __name__ == '__main__':
    main()