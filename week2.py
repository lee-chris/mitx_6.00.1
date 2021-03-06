def number_guess():
    """Simple program to guess the user's number."""
    
    print("Please think of a number between 0 and 100!")
    
    low = 0
    high = 100
    guess = 50
    i = ""
    
    while i != "c":
        print("Is your secret number {0}?".format(guess))
        i = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        
        if i == "l":
            low = guess
            guess = int(guess + ((high - guess) / 2))
        elif i == "h":
            high = guess
            guess = int(guess - ((guess - low) / 2))
        elif i == "c":
            print("Game over. Your secret number was: {0}".format(guess))
        else:
            print("Sorry, I did not understand your input.")


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    test = None

    if (a < b):
        test = a
    else:
        test = b

    while test > 0:
        if a % test == 0 and b % test == 0:
            return test
        test -= 1


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if a == b:
        return a

    if a < b:
        return gcdRecur(a, b - a)
    else:
        return gcdRecur(a - b, b)


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    if len(aStr) == 0:
        return False

    midpoint = len(aStr) // 2
    test = aStr[midpoint]
    
    if test == char:
        return True
    
    if len(aStr) == 1:
        return False
    
    if char < test:
        return isIn(char, aStr[:midpoint])
    else:
        return isIn(char, aStr[midpoint:])


balance = 320000
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def problem1():
    """Calculate interest after 12 months."""

    monthly_interest_rate = annualInterestRate / 12.0
    previous_balance = balance
    
    for i in range(0, 12):
    
        min_monthly_payment = monthlyPaymentRate * previous_balance
        monthly_unpaid_balance = previous_balance - min_monthly_payment
        previous_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    
    print ("Remaining balance: {0:.2f}".format(previous_balance))


def problem2():
    """Calculate lowest monthly payment to settle balance in 12 months."""
    
    monthly_interest_rate = annualInterestRate / 12.0
    
    def calculate_interest(monthly_rate):
        
        previous_balance = balance
    
        for i in range(0, 12):
    
            monthly_unpaid_balance = previous_balance - monthly_rate
            previous_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        
        return previous_balance
    
    i = 10
    while i < balance:
        
        value = calculate_interest(i)
        
        if value < 0.005:
            print("Lowest Payment: {0}".format(i))
            return
        
        i += 10


def problem3():
    """Bisection search to solve lowest monthly payment problem (see problem2)"""

    monthly_interest_rate = annualInterestRate / 12.0
    
    def calculate_interest(monthly_rate):
        
        previous_balance = balance
    
        for i in range(0, 12):
    
            monthly_unpaid_balance = previous_balance - monthly_rate
            previous_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        
        return previous_balance
    
    lower = balance / 12
    upper = (balance * (1 + monthly_interest_rate) ** 12) / 12.0
    
    payment = (upper + lower) / 2.0
    old_balance = balance
    
    while True:
        
        new_balance = calculate_interest(payment)
        
        if abs(new_balance - old_balance) < 0.005:
            break
        
        if new_balance < 0:
            upper = payment
            payment = (upper + lower) / 2.0
            #print("too high: {0}, {1}".format(lower, upper))
        else:
            lower = payment
            payment = (upper + lower) / 2.0
            #print("too low: {0}, {1}".format(lower, upper))
        
        old_balance = new_balance

    print("Lowest payment: {0:.2f}".format(payment))

























