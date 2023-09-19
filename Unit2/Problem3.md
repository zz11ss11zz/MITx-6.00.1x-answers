## Problem 3 - Using Bisection Search to Make the Program Faster 
Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) 
to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. 
Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). 
Produce the same return value as you did in Problem 2. 
* In short  \
Monthly interest rate = (Annual interest rate) / 12.0 \
Monthly payment lower bound = Balance / 12 \
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)<sup> 12 </sup>) / 12.0
* Test Cases: \
 balance = 320000 \
 annualInterestRate = 0.2 \
 Result Your Code Should Generate: \
 Lowest Payment: 29157.09

