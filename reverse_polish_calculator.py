"""description - Reverse polish calculator

tests:
>>> ReversePolishCalculator([3, 2, 4], ['*', '+']).calculate()
11

>>> ReversePolishCalculator([0, 3, 2, 4], ['/', '+', '*']).calculate()
0.0

>>> ReversePolishCalculator([-5, 10, 3], ['*', '+']).calculate()
25

"""
import operator

class ReversePolishCalculator:
    def __init__(self, arguments=None, operators=None):
        self.mapper = {
            '+': operator.add,
            '*': operator.mul,
            '-': operator.sub,
            '/': operator.truediv
        }
        self.arguments = arguments or []
        self.operators = operators or []
    
    def insert_input(self):
        while(True):
            result = input('Please enter the numbers and then the operators (enter "end" to stop): ')
            try:  
                self.arguments.append(int(result))
            except ValueError:
                print('in except with value: {}'.format(result))
                if result in self.mapper.keys():
                    self.operators.append(result)
                elif result == 'end':
                    break
                

    def calculate(self):
        for op in self.operators:
            self.arguments[-1] = self.mapper[op](self.arguments.pop(), self.arguments[-1])
        
        return self.arguments[0]



if __name__ == "__main__":
    calculator = ReversePolishCalculator()
    calculator.insert_input()
    result = calculator.calculate()
    print('result: {}, or type: {}'.format(result, type(result)))

    import doctest
    
