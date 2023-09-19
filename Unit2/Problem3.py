a = balance
monthlyInterestRate = annualInterestRate/12
lowpay = balance/12
uppay = (balance*(1+monthlyInterestRate)**12)/12
pay0 = (lowpay+uppay)/2


def f(balance, pay0, month):
    global lowpay
    global uppay
    if month == 0 and balance < -0.01:
        (lowpay, uppay) = (lowpay, pay0)
        pay0 = (lowpay+uppay)/2
        return f(a, pay0, 12)
    elif month == 0 and balance > 0.01:
#        print("1", lowpay, uppay, pay0)
        (lowpay, uppay) = (pay0, uppay)
        pay0 = (lowpay+uppay)/2
#        print("2", lowpay, uppay, pay0)
        return f(a, pay0, 12)
    elif month == 0 and balance <= 0.01 and balance >= -0.01:
        return pay0
    else:
        unbalance = balance - pay0
        balance = unbalance + monthlyInterestRate*unbalance
#        print(13-month, "balance=", balance, "uppay=", uppay, "lowpay=", lowpay, "pay0=",pay0)
    return f(balance, pay0, month-1)
print(round(f(balance,pay0,12),2))