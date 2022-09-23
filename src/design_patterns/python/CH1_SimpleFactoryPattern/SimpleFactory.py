# -*- coding:utf-8 -*-
'''
@File    :   SimpleFactory.py
@Time    :   2022/09/23 11:19:07
@Author  :   SheltonXiao
@Version :   1.0
@Contact :   pi620903@163.com
@Desc    :   None
@License :

    (c) Copyright 2022 SheltonXiao

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or(at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY;without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
    GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with this program.If not, see < https: //www.gnu.org/licenses/>.
'''

class Operation(object):
    __numberA = 0
    __numberB = 0
    def get_numberA(self):
        return self.__numberA
    def set_numberA(self,numberA):
        self.__numberA = numberA
    def get_numberB(self):
        return self.__numberB
    def set_numberB(self,numberB):
        self.__numberB = numberB
    def get_result():
        result = 0
        return result
    numberA = property(get_numberA,set_numberA)
    numberB = property(get_numberB,set_numberB)

class OperationAdd(Operation):
    def get_result(self):
        result = self.numberA + self.numberB
        return result

class OperationSub(Operation):
    def get_result(self):
        result = self.numberA - self.numberB
        return result

class OperationMul(Operation):
    def get_result(self):
        result = self.numberA * self.numberB
        return result

class OperationDiv(Operation):
    def get_result(self):
        if self.numberB == 0:
            raise Exception("除数不能为0")
        result = self.numberA / self.numberB
        return result

class OperationFactory(object):
    def createOperate(self,operate):
        if operate == "+":
            self.oper = OperationAdd()
        elif operate == "-":
            self.oper = OperationSub()
        elif operate == "*":
            self.oper = OperationMul()
        elif operate == "/":
            self.oper = OperationDiv()
        return self.oper


if __name__ == '__main__':
    oper = OperationFactory().createOperate("+")
    oper.numberA = 1
    oper.numberB = 2
    result = oper.get_result()
