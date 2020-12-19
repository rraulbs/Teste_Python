# -*- coding: utf-8 -*-5
"""
Created on Sat Dec 19 09:29:38 2020

@author: Raul
"""
#   TESTE DE PYTHON
import math
from statistics import *

def question_1(interval):
    count = 0
    for number in range(1, interval + 1):
        if (number%2)==0 and (number%37)==0 and (number%49)==0:
            count = count + 1
    return count
print ("QUESTÃO 1:")
print ("A resposta para o intervalo de 1 a 5 milhões é: ", question_1(5000000))

def question_2():
    x = [None]*10
    for position in range(len(x)):
        if(position%2 == 0):
            x[position] = 3**position + 7*(math.factorial(position))
        else:
            x[position] = 2**position + 4*(math.log(position))
    
    position_biggest_element = x.index(max(x))
    mean_elements = round(mean(x),2) 
    return (position_biggest_element, mean_elements)

print ("QUESTÃO 2:")
print("A posição do maior elemento desse vetor é: ", question_2()[0])
print("A média dos elementos contidos nesse vetor é: ", question_2()[1])

def question_3(grades):
    dict_students = {}
    for i in range(len(grades)):
        dict_students['studant' + '_' + str(i)] = grades[i]  
    best_grade = dict_students[max(dict_students, key=dict_students.get)]
    best_student = [key for key, student in dict_students.items() if student == best_grade]
    return (best_student, best_grade)
#   Obs.: Estudante(s) pois duas pessoas podem ter tirado 10 por exemplo, então teriamos 2 estudantes com maior nota
print ("QUESTÃO 3:")
print( "Estudante(s) com maior nota: ", question_3([7,2,8,10])[0])
print( "A maior nota: ", question_3([7,2,8,10])[1])