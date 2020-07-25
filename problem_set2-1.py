'''
1년 뒤의 신용 카드 잔고 계산하기.
balance: 신용카드의 잔고
annualInterestRate: 연간 이자율
monthlyPaymentRate: 월별 지불율
return: balance, 2 decimal digit
return: annual, 1 decimal digit
한달 뒤의 잔액을 계산하고, 열 두달 뒤에 연간 이자율을 더한 최종 remaining balance를 반환
'''

def solve(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    for i in range(12):
        minimumMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        i += 1
    print("Remaining balance:", round(balance, 2))

solve(42, 0.2, 0.04)
