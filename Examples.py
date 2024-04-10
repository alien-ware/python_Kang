import  os
import  numpy as np
from    pathlib import Path
from    numpy import linspace, ones
#                                                                                                                       -
#                                                                                                                       -
a              = 1
A              = 1
number         = 2
my_number      = 2
my_temp_number = 2
CONST_NUMBER   = 10
per_gv         = 100
#                                                                                                                       -
#                                                                                                                       -
def func1_f(numberList = [], numberFlag = None):
    '''this is a func1 example without annotation'''
    # the function doc, i.e., __doc__, is presented above
    pass
#
def func2_f(numberList: list[int] = [], numberFlag: bool = None) -> None:
    '''this is a func2 example with annotation'''
    pass
#
def func3_f(numberList1: list[int] = [], numberList2: list[int] = [], numberList3: list[int] = [],
        numberList4: list[float] = [], numberFlag: bool = True) -> None:
    '''this is a func3 example with annotation, multi-line arguments'''
    pass
#
def compare_number_f(number: float) -> None:
    '''compare the number with initial numbers'''
    if number < 10:
        print(f'{number} is smaller than 10')
    elif 20 < number and number <30:
        print(f'{number} is smaller than 30, and bigger than 20')
    else:
        print(f'{number} is out of the range')
#
def func_add_gv_f():
    '''add one per executation'''
    global per_gv
    per_gv += 1
#
def test_exception_f(denominator: float):
    '''try except finally'''
    try:
        1/denominator
    except ZeroDivisionError as e:
        print(e)
    finally:
        print('finally')
#                                                                                                                       -
#                                                                                                                       -
class Animal:
    '''this is an animal model'''
    def __init__(self,  age: int ,color: str = 'red'):
        self.color_p = color
        self.age_p   = age
    #
    def run_m(self,):
        '''run method'''
        # pass
        print('father running')
    #
    def eat_m(self,):
        '''eat method'''
        pass
#
class Cat(Animal):
    ''' subclass of the Animal class'''
    def __init__(self, color, age):
        '''在基础类中定义了变量的类型，在定义子类的时候可以不再指定变量的类型'''
        super().__init__(color, age)
        # self.name_m = name
    #
    def run_m(self):
        super().run_m()
        print('cat running')

#                                                                                                                       -
if __name__ == "__main__":
    red_cat = Cat(color = 'red', age = 10)
    # test global variable
    print(f'initial per_gv: {per_gv}')
    func_add_gv_f()
    print(f'current per_gv: {per_gv} after executing func_add_gv ')
    func_add_gv_f()
    print(f'current per_gv: {per_gv} after executing func_add_gv ')
    # test global variable
    compare_number_f(25)
#                                                                                                                       -
