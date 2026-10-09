## С1 Тема 4 - Модули в Python - Урок 2
# from math import *
# from cmath import *

# print(sqrt(4))


# import math
# import cmath

# print(math.sqrt(4))   # 2.0
# print(cmath.sqrt(4))  # (2+0j)


# from math import factorial as fact
# from random import randint as rnd


# value = rnd(1,10)
# result = fact(value)
# print('Факториал', value, 'равен', result)

## C1 Тема 4 - Модули в Python - Урок 4
# bash = 31
# c_and_c_plus_plus = 29
# c_sharp = 11
# html_css = 36
# java = 19
# javascript = 37
# sql = 34


# def analyze_skills():
#     min_share = min(bash, c_and_c_plus_plus, c_sharp, html_css, java, javascript, sql)
#     max_share = max(bash, c_and_c_plus_plus, c_sharp, html_css, java, javascript, sql)
#     print('Доля питонистов, у которых есть наименее популярный навык (в %):', min_share)
#     print('Доля питонистов, у которых есть наиболее популярный навык (в %):', max_share)


# # Не удаляйте вызов функции.
# analyze_skills()

# Количество вакансий для различных языков программирования:
# c_sharp = 375
# java = 546
# java_script = 915
# php = 288
# python = 603

# def analyze_jobs():
#     # Вычислите общее количество исследованных вакансий.
#     total_jobs = total_jobs = c_sharp + java + java_script + php + python
#     # Вычислите процент вакансий для Python от общего числа вакансий
#     # и округлите результат до двух знаков (до сотых долей):
#     python_percent = round(python / total_jobs * 100, 2)
#     # Напечатайте фразы, описанные в задании (две строки).
#     print('Общее число исследованных вакансий, в тысячах:', total_jobs)
#     print('Вакансии для Python-разработчиков, в %:', python_percent)

# analyze_jobs()

# Выполните импорт math как mt.

# git = 22.7
# sql = 35.2
# english = 28.3
# django = 31.8
# linux = 30.5


# import math as mt


# def analyze_skills_geometric():
#     max_skill = max(git, sql, english, django, linux)
#     min_skill = min(git, sql, english, django, linux)
#     geometric_mean = round(mt.sqrt(max_skill * min_skill),2)
#     print('Среднее геометрическое между наименее и наиболее популярным навыком (в %):', geometric_mean)
# # Вызов функции для проверки
# analyze_skills_geometric()