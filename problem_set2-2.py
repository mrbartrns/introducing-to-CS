def solve(balance, annualInterestRate):
    minimumFixedMonthlyPayment = 10
    original = balance
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyUnpaidBalance = balance - minimumFixedMonthlyPayment
    while balance > 0:
        for i in range(12):
            monthlyUnpaidBalance = balance - minimumFixedMonthlyPayment
            balance = monthlyUnpaidBalance * (1 + monthlyInterestRate)
            i += 1
        if balance > 0:
            balance = original
            minimumFixedMonthlyPayment += 10
    print("Lowest Payment:", minimumFixedMonthlyPayment)

solve(3330, 0.2)