class Payment:
    def __init__(self, price):
        self.__price=price

book=Payment(20)
book._Payment__price=21
print(book._Payment__price)