a = balance
monthlyInterestRate = annualInterestRate/12
lowpay0 = balance/12

if lowpay0 % 10 == 0:
    aa = lowpay0
else:
    aa = lowpay0 // 10 + 1
lowpay = aa*10

def f(balance, lowpay, month):
    if month == 0 and balance <= 0:
        return lowpay
    elif month == 0 and balance > 0:
        lowpay += 10
        return f(a, lowpay, 12)
    else:
        unbalance = balance - lowpay
        balance = unbalance + monthlyInterestRate*unbalance
    return f(balance, lowpay, month-1)
print("Lowest Payment:", f(balance,lowpay,12))