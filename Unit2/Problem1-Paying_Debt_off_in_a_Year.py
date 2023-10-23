# Paste your code into this box

monthlyInterestRate = annualInterestRate/12



def f(balance, month):
    if month == 0:
        unbalance = balance 
        return round(unbalance, 2)
    else:
        unbalance = balance * (1 - monthlyPaymentRate)  #ub1 = b1 -p1
        balance = unbalance * (1 + annualInterestRate/12)  #  b2 = ub1 + r/12*ub1
    return round(f(balance, month-1),2)

print("Remaining balance: ", f(balance, 12))