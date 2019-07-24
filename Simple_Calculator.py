class Calculator():
    def __init__(self, type_of_calculator):
        self.type_of_calculator = type_of_calculator

    def get_type(self):
        print(self.type_of_calculator)

    def Add(self, val1, val2):
        return val1 + val2    #better than print(val1 + val2) due to KISS

    def Minus(self, val1, val2):
        return val1 - val2

    def Multiply(self, val1, val2):
        return val1 * val2

    def Divide(self, val1, val2):
        return val1 / val2