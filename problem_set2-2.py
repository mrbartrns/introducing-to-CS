def solve(balance, annualInterestRate):
    '''
    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    한달 내는 금액을 열 두번내어 balance를 0으로 만드는 금액> 정답
    balance를 더하여 그것을 12로 나누면?
    '''
    minimumFixedMonthlyPayment = 0
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyUnpaidBalance = balance - minimumFixedMonthlyPayment
    balance = (monthlyUnpaidBalance) * (1 + monthlyInterestRate)
    for i in range(12):
        pass