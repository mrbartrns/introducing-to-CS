def solve(balance, annualInterestRate):
    '''
    To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year.
    What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that.
    If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month.
    One-twelfth of the original balance is a good lower bound.

    What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year.
    What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month.
    So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.
    '''
    monthlyInterestRate = annualInterestRate / 12.0
    lowerMonthly = balance / 12.0
    upperMonthly = balance * (1 + monthlyInterestRate)**12 / 12.0
    monthlyPayment = (lowerMonthly + upperMonthly) / 2.0
    newBalance = balance
    epsilon = 0.01

    while abs(newBalance) >= epsilon:
        newBalance = balance

        for i in range(12):
            newBalance -= monthlyPayment
            newBalance += monthlyInterestRate * newBalance

        if abs(newBalance) < epsilon:
            break
        elif newBalance > 0:
            lowerMonthly = monthlyPayment
        else:
            upperMonthly = monthlyPayment

        monthlyPayment = (lowerMonthly + upperMonthly) / 2.0

    print('Lowest Payment:', round(monthlyPayment, 2))