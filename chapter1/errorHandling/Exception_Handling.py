
class InsufficentBalanceException(Exception):
    '''Exception raised for errors in the withdrawal process '''

    def __init__(self, amount, balance, msg="Insufficent Balance"):
        self.amount = amount
        self.balance = balance
        self.msg = msg
        super().__init__(self.msg)


def withdrawal(withdrawal, amount):
    if amount < withdrawal:
        raise InsufficentBalanceException(withdrawal, amount)
    return withdrawal


try:
    print("Reading card....")
    withdrawal(10, 5)
except InsufficentBalanceException as e:
    print(e)
finally:
    print("take out your atm card")
