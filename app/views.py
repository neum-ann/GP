#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Подключение модулей фласки
from app import app, db
from .forms import *
from app.models import *
from flask import render_template, redirect, request, url_for, session

# Подключение собственных библиотек
from app.algorithm.step1 import work_at_answer
from app.algorithm.step2 import sorted_group

# Потенциально используемые библиотеки
# import os
# from sqlalchemy import update
# import numpy as np
# import matplotlib.pyplot as plt
# from time import gmtime, strftime
# import plotly
# plotly.tools.set_credentials_file(username='ViktorS', api_key='gk3itQcWHuFkAfuZleor')
# import plotly.plotly as py
# import plotly.graph_objs as go

# Глобальные переменные
idd=0

# Возвращает базовый шаблон
@app.route('/')
def base():

    return render_template('base.html')

# Статья о нас
@app.route('/about_us')
def about_us():

    return render_template('about_us.html')

# Инструкция в работе
@app.route('/instruction')
def instruction():

    return render_template('instruction.html')

# Главная страница
@app.route('/main', methods=['GET','POST'])
def main():
    global idd

    # Объявление формы
    form_login=Login(request.form)
    
    # Обработка ответа от пользователя
    if request.form and True:

    	# Изъятие данных из форм
        login=form_login.login.data
        password=form_login.password.data

        # Проверка ввели ли логин
        if login=='':
            
            return render_template('main.html',
                    form=form_login,
                    Error='Ошибка! Поле логина пустое.'
                )

        # Проверка ввели ли пароль
        if password=='':
            
            return render_template('main.html',
                    form=form_login,
                    Error='Ошибка! Поле пароля пустое.'
                )

        # Поиск пользователя в бд
        select=User.query.filter_by(login=login).first()

        # Если пользователь обнаружен
        if select!=None:

            # Если пароль совпадает
            if select.password==password:
                
                # Если заходит респондент
                if select.role=='resp':
                    idd=select.id

                    return redirect('http://localhost:5000/test')

                # Если заходит админинстратор
                elif select.role=='admin':
                    idd=select.id

                    return redirect('http://localhost:5000/admin')

                # Если роль неопознать
                else:
                    
                    return render_template('main.html',
                        form=form_login,
                        Error='Неизвестная ошибка! Этого просто не может быть! Код ошибки #001. Сообщите нам об этом пожалуйста!'
                    )

            # Если пароль не совпал
            else:
                
                return render_template('main.html',
                    form=form_login,
                    Error='Ошибка! Указан неверный пароль.'
                )

        # Если пользователя с таким логином нет
        else:
            
            return render_template('main.html',
                form=form_login,
                Error='Ошибка! Указан неверный логин или такого пользователя не существует.'
            )

    # Запуск главной страницы
    return render_template('main.html',
        form=form_login,
        )

# Страница регистрации респондента
@app.route('/reg_resp', methods=['GET','POST'])
def reg_resp():
    global idd

    # Создание формы для сбора данных
    form_resp=Respondent(request.form)

    # Обработка ответа от пользователя
    if request.form and True:
        
        # Проверка согласия на обработку персональных данных 
        soglasie=False
        for i in request.form:
            
            # Если он согласился, то отмечаем это
            if i=='soglasie':
                soglasie=True

        # Если согласен на обработку персональных данных
        if soglasie:

            # Изъятие данных
            email=form_resp.email.data
            password=form_resp.password.data
            login=form_resp.login.data
            surname=form_resp.surname.data
            name=form_resp.name.data
            # middle_name=form_resp.middle_name.data

            # проверка условиями
            # проверка почты на корректность
            if email=='':

                return render_template('reg_resp.html',
                    form=form_resp,
                    Error='Ошибка! Поле почта не заполнено.'
                )

            # проверка пароля на корректность
            if len(password)<6:

                return render_template('reg_resp.html',
                    form=form_resp,
                    Error='Ошибка! Пароль меньше 6 символов.'
                )

            # проверка логина на корректность
            if login=='':

                return render_template('reg_resp.html',
                    form=form_resp,
                    Error='Ошибка! Поле логина не заполнено.'
                )

            # проверка фамилии на корректность
            if surname=='':

                return render_template('reg_resp.html',
                    form=form_resp,
                    Error='Ошибка! Поле фамилии не заполнено.'
                )

            # проверка имени на корректность
            if name=='':

                return render_template('reg_resp.html',
                    form=form_resp,
                    Error='Ошибка! Поле имени не заполнено.'
                )

            # проверка отчества на корректность
            # if middle_name=='':

            #     return render_template('reg_resp.html',
            #         form=form_resp,
            #         Error='Ошибка! Поле отчества не заполнено.'
            #     )

            # проверка циклами
            # проверка почты на корректность
            for i in email:
                if i==' ':
                    
                    return render_template('reg_resp.html',
                        form=form_resp,
                        Error='Ошибка! В поле почты недопустимый символ.'
                    )

            # проверка пароля на корректность
            for i in password:
                if i==' ':
                    
                    return render_template('reg_resp.html',
                        form=form_resp,
                        Error='Ошибка! В поле пароля недопустимый символ.'
                    )

            # проверка логина на корректность
            for i in login:
                if i==' ':
                    return render_template('reg_resp.html',
                        form=form_resp,
                        Error='Ошибка! В поле логина недопустимый символ.'
                    )

            # проверка фамилии на корректность
            for i in surname:
                if i==' ':
                    
                    return render_template('reg_resp.html',
                        form=form_resp,
                        Error='Ошибка! В поле фамилии недопустимый символ.'
                    )

            # проверка имени на корректность
            for i in name:
                if i==' ':
                    
                    return render_template('reg_resp.html',
                        form=form_resp,
                        Error='Ошибка! В поле имени недопустимый символ.'
                    )

            # проверка отчества на корректность
            # for i in middle_name:
            #     if i==' ':
                    
            #         return render_template('reg_resp.html',
            #             form=form_resp,
            #             Error='Ошибка! В поле отчества недопустимый символ.'
            #         )

            # Поиск пользователей с таким емэйлом
            select=User.query.filter_by(email=email).first()

            # Если запрос не пустой
            if select!=None:
                
                # Если такой почты существует
                if select.email!=email:

                    # Поиск пользователей с таким логином
                    select=User.query.filter_by(login=login).first()

                    # Если такого логина не существует
                    if select.login!=login:

                        # Создание пользователя в бд
                        U=User(password=password, email=email, login=login, surname=surname, name=name, role='resp')
                        db.session.add(U)
                        db.session.commit()

                        # Сразу переходим к выполнению теста
                        select=User.query.filter_by(login=login).first()
                        idd=select.id

                        return redirect('http://localhost:5000/start_test')

                    # Если такой логин уже существует
                    else:

                        return render_template('reg_resp.html',
                            form=form_resp,
                            Error='Ошибка! Этот логин уже зарегистрирован!'
                        )

                # Если такая почта уже существует
                else:

                    return render_template('reg_resp.html',
                        form=form_resp,
                        Error='Ошибка! Эта почта уже зарегистрирована!'
                    )

            # Если запрос пустой, то можно спокойно создавать
            else:

                # Создани пользователя
                U=User(password=password, email=email, login=login, surname=surname, name=name, role='resp')
                db.session.add(U)
                db.session.commit()

                # Сразу переходим к выполнению теста
                select=User.query.filter_by(login=login).first()
                idd=select.id

                return redirect('http://localhost:5000/start_test')

        # Если не согласен на обработку персональных данных
        else:

            return render_template('reg_resp.html',
                form=form_resp,
                Error='Ошибка! Вы не дали согласие на обработку персональных данных!'
            )

    # Запуск страницы регистрации респондента
    return render_template('reg_resp.html',
        form=form_resp
        )

# Страница регистрации админинстратора
@app.route('/reg_admin', methods=['GET','POST'])
def reg_admin():
    global idd

    # Форма для сбора данных
    form_admin=Admin(request.form)

    # Обработка ответа пользователя
    if request.form and True:

        # Изъятие данных
        email=form_admin.email.data
        login=form_admin.login.data
        surname=form_admin.surname.data
        name=form_admin.name.data
        middle_name=form_admin.middle_name.data

        # проверка условиями
        # проверка почты на корректность
        if email=='':

            return render_template('reg_admin.html',
                form=form_admin,
                Error='Ошибка! Поле почта не заполнено.'
            )

        # проверка логина на корректность
        if login=='':

            return render_template('reg_admin.html',
                form=form_admin,
                Error='Ошибка! Поле логина не заполнено.'
            )

        # проверка фамилии на корректность
        if surname=='':

            return render_template('reg_admin.html',
                form=form_admin,
                Error='Ошибка! Поле фамилии не заполнено.'
            )

        # проверка имени на корректность
        if name=='':

            return render_template('reg_admin.html',
                form=form_admin,
                Error='Ошибка! Поле имени не заполнено.'
            )

        # проверка отчества на корректность
        if middle_name=='':

            return render_template('reg_admin.html',
                form=form_admin,
                Error='Ошибка! Поле отчества не заполнено.'
            )

        # проверка циклами
        # проверка почты на корректность
        for i in email:
            if i==' ':
                
                return render_template('reg_admin.html',
                    form=form_admin,
                    Error='Ошибка! В поле почты недопустимый символ.'
                )

        # проверка логина на корректность
        for i in login:
            if i==' ':
                
                return render_template('reg_admin.html',
                    form=form_admin,
                    Error='Ошибка! В поле логина недопустимый символ.'
                )

        # проверка фамилии на корректность
        for i in surname:
            if i==' ':
                
                return render_template('reg_admin.html',
                    form=form_admin,
                    Error='Ошибка! В поле фамилии недопустимый символ.'
                )

        # проверка имени на корректность
        for i in name:
            if i==' ':
                
                return render_template('reg_admin.html',
                    form=form_admin,
                    Error='Ошибка! В поле имени недопустимый символ.'
                )

        # проверка отчества на корректность
        for i in middle_name:
            if i==' ':
                
                return render_template('reg_admin.html',
                    form=form_admin,
                    Error='Ошибка! В поле отчества недопустимый символ.'
                )

        # Сбор такой почты из бд
        select=User.query.filter_by(email=email).first()

        # Если запрос не пустой
        if select!=None:

            # Проверка на уникальность почты
            if select.email!=email: 

                # Сбор такого логина из бд
                select=User.query.filter_by(login=login).first()
        
                # Проверка на уникальность логина
                if select.login!=login:

                    # Создание пользователя в бд
                    U=User(password='321519', email=email, login=login, surname=surname, name=name, middle_name=middle_name, role='admin')
                    db.session.add(U)
                    db.session.commit()

                    # Сразу переходим к выполнению теста
                    select=User.query.filter_by(login=login).first()
                    idd=select.id

                    return redirect('http://localhost:5000/admin')

                # Если логин уже есть
                else:

                    return render_template('reg_admin.html',
                        form=form_admin,
                        Error='Ошибка! Такой логин уже есть.'
                    )

            # Если такая почта уже есть
            else:

                return render_template('reg_admin.html',
                    form=form_admin,
                    Error='Ошибка! Такая почта уже есть.'
                )

        # Если запрос пустой
        else:

            # Создание пользователя в бд
            U=User(password='321519', email=email, login=login, surname=surname, name=name, middle_name=middle_name, role='admin')
            db.session.add(U)
            db.session.commit()       

            # Сразу переходим на страницу
            select=User.query.filter_by(login=login).first()
            idd=select.id

            return redirect('http://localhost:5000/admin')     

    # Создание страницы
    return render_template('reg_admin.html',
        form=form_admin
        )

# Инструкция перед прохождением тэста
@app.route('/start_test')
def start_test():
    global idd
    
    return render_template('start_test.html')

# Тест для респондента
@app.route('/test', methods=['GET','POST'])
def test():
    global idd

    # Создание формы для сбора ответов
    form_answ=Answer(request.form)

    # Обработка ответов
    if request.form and True:

        # Сбор ответов
        arr_answ=[]
        for i in request.form:
            arr_answ.append(i)  

        # Проверка на наличие всех ответов
        if len(arr_answ)<30:

            # Создание массиво для сбора вопросов из бд
            arr_question_A=[]
            arr_question_B=[]

            # Выбор всех данных теста из бд
            select=Test.query.filter_by().all()

            # Разбиение всех вопросов по А и Б
            for i in range(len(select)):
                arr_question_A.append(select[i].question_A)
                arr_question_B.append(select[i].question_B)

            # Выборка данных респондента из бд
            select=User.query.filter_by(id=idd).first()

            return render_template('test.html',
                surname=select.surname,
                name=select.name,
                middle_name=select.middle_name,
                arr_A=arr_question_A,
                arr_B=arr_question_B,
                Answ=form_answ,
                Error='Ошибка! Вы пропустили один или более вопросов.'
            )       

        # Обработка ответов в корректный вид
        arr=work_at_answer(arr_answ)

        # Если в ходе проверки возникла ошибка
        if arr=='Error':
            
            return render_template('test.html',
                surname=select.surname,
                name=select.name,
                middle_name=select.middle_name,
                arr_A=arr_question_A,
                arr_B=arr_question_B,
                Answ=form_answ,
                Error='Ошибка! Вы дважды ответили на один и тот же вопрос.'
            ) 

        # Распаковка обработанных данных
        count_sopernichestvo=arr[0]
        count_sotrudnichestvo=arr[1]
        count_kompromis=arr[2]
        count_izbeganie=arr[3]
        count_prispososoblenie=arr[4]

        # Сортировка данных обработанных
        arr=sorted(arr)

        # Выделяющая характеристика
        more_count=arr[4]

        # Подтвержение наибольшого характера
        if count_sopernichestvo==more_count:
            more_count='sopernichestvo'

        elif count_sotrudnichestvo==more_count:
            more_count='sotrudnichestvo'

        elif count_kompromis==more_count:
            more_count='kompromis'

        elif count_izbeganie==more_count:
            more_count='izbeganie'

        elif count_prispososoblenie==more_count:
            more_count='prisposoblenie'

        # Сохранение ответов респондента в бд
        R=Results(id_user=idd, count_sopernichestvo=count_sopernichestvo, count_sotrudnichestvo=count_sotrudnichestvo, count_kompromis=count_kompromis, count_izbeganie=count_izbeganie, count_prispososoblenie=count_prispososoblenie, more_count=more_count)
        db.session.add(R)
        db.session.commit()

        # Объявление формы
        form_login=Login(request.form)

        # После ответа переход на главную
        # return render_template('main.html',
            # form=form_login,
            # Error='Спасибо за прохождение тэста!'
        # )

        # После ответа результат
        return render_template('result.html')

    # Создание массиво для сбора вопросов из бд
    arr_question_A=[]
    arr_question_B=[]

    # Выбор всех данных теста из бд
    select=Test.query.filter_by().all()

    # Разбиение всех вопросов по А и Б
    for i in range(len(select)):
        arr_question_A.append(select[i].question_A)
        arr_question_B.append(select[i].question_B)

    # Выборка данных респондента из бд
    select=User.query.filter_by(id=idd).first()

    # Создание страницы
    return render_template('test.html',
        surname=select.surname,
        name=select.name,
        middle_name=select.middle_name,
        arr_A=arr_question_A,
        arr_B=arr_question_B,
        Answ=form_answ
        )

# Результат тестирования
@app.route('/result')
def result():
    
    return render_template('result.html')

# Страница админинстратора
@app.route('/admin', methods=['GET','POST'])
def admin():
    global idd

    # Обработка ответа
    if request.form and True:

        # Извлечение данных
        for i in request.form:
            to_do=i

        # Такое невозможно, но мало ли
        if len(to_do)=='':
            
            # выборка данных админа
            select=User.query.filter_by(id=idd).first()

            return render_template('admin.html',
                surname=select.surname,
                name=select.name,
                middle_name=select.middle_name,
                data='.',
                last='.',
                Error='Неизвестная ошибка! Этого просто не может быть! Код ошибки #002. Сообщите нам об этом пожалуйста!'
            )

        # Если надо сгенерировать группы
        if to_do=='generation':

            # Собираем всех респондентов
            arr_people=[]
            select=User.query.filter_by(role='resp').all()

            # Если запрос не пустой
            if select!=None:
                for i in select:
                    arr_people.append(i.id)
            
            # Если запрос пустой
            else:

                # выборка данных админа
                select=User.query.filter_by(id=idd).first()

                return render_template('admin.html',
                    surname=select.surname,
                    name=select.name,
                    middle_name=select.middle_name,
                    data='.',
                    last='.',
                    Error='Респондентов нет.'
                )

            # Если не респондентов
            if len(arr_people)==0:

                # выборка данных админа
                select=User.query.filter_by(id=idd).first()

                return render_template('admin.html',
                    surname=select.surname,
                    name=select.name,
                    middle_name=select.middle_name,
                    data='.',
                    last='.',
                    Error='Респондентов нет.'
                )

            # создание списков всех характеров
            arr_sotrudnichestvo=[]
            arr_sopernichestvo=[]
            arr_izbeganie=[]
            arr_kompromis=[]
            arr_prispososoblenie=[]

            # цикл по всем респондентам
            for i in arr_people:
                
                # выборка результатов пользователя
                select=Results.query.filter_by(id_user=i).first()

                # Если запрос не пустой
                if select!=None:

                    # Выбор основного характера респондента и добавление его в списки характера
                    if select.more_count=='sotrudnichestvo':
                        arr_sotrudnichestvo.append(i)
                        arr_sotrudnichestvo.append(select.count_sotrudnichestvo)

                    elif select.more_count=='sopernichestvo':
                        arr_sopernichestvo.append(i)
                        arr_sopernichestvo.append(select.count_sopernichestvo)

                    elif select.more_count=='kompromis':
                        arr_kompromis.append(i)
                        arr_kompromis.append(select.count_kompromis)

                    elif select.more_count=='izbeganie':
                        arr_izbeganie.append(i)
                        arr_izbeganie.append(select.count_izbeganie)

                    elif select.more_count=='prisposoblenie':
                        arr_prispososoblenie.append(i)
                        arr_prispososoblenie.append(select.count_prispososoblenie)

                # Если запрос пустой
                else:
                    
                    # выборка данных админа
                    select=User.query.filter_by(id=idd).first()

                    return render_template('admin.html',
                        surname=select.surname,
                        name=select.name,
                        middle_name=select.middle_name,
                        data='.',
                        last='.',
                        Error='Неизвестная ошибка! Этого просто не может быть! Код ошибки #003. Сообщите нам об этом пожалуйста!'
                    )

            # сортировка характеров, что бы вначале списка был самый большой балл
            arr_sotrudnichestvo=sorted_group(arr_sotrudnichestvo)
            arr_sopernichestvo=sorted_group(arr_sopernichestvo)
            arr_kompromis=sorted_group(arr_kompromis)
            arr_izbeganie=sorted_group(arr_izbeganie)
            arr_prispososoblenie=sorted_group(arr_prispososoblenie)

            # выясняем какое минимальное число людей в характере
            max_people=100
            if max_people>int(len(arr_sopernichestvo)/2):
                if len(arr_sopernichestvo)!=0:

                        max_people=int(len(arr_sopernichestvo)/2)

                else:
                    max_people=0
            
            if max_people>int(len(arr_sotrudnichestvo)/2):
                if len(arr_sotrudnichestvo)!=0:

                    max_people=int(len(arr_sotrudnichestvo/2))

                else:
                    max_people=0
            
            if max_people>int(len(arr_kompromis)/2):
                if len(arr_kompromis)!=0:

                    max_people=int(len(arr_kompromis)/2)

                else:
                    max_people=0
            
            if max_people>int(len(arr_izbeganie)/2):
                if len(arr_izbeganie)!=0:

                    max_people=int(len(arr_izbeganie)/2)

                else:
                    max_people=0
            
            if max_people>int(len(arr_prispososoblenie)/2):
                if len(arr_prispososoblenie)!=0:

                    max_people=int(len(arr_prispososoblenie)/2)

                else:
                    max_people=0

            # начинаем создавать группы
            arr_group=[]
            group=[]
            count_people=int((len(arr_sotrudnichestvo)+len(arr_sopernichestvo)+len(arr_kompromis)+len(arr_izbeganie)+len(arr_prispososoblenie))/2)

            # ПОТОМ УБРАТЬ
            max_people=0

            # Если есть характеры без людей
            if max_people==0:
                
                # Цикл пока есть люди для распределения
                while True:

                    # Если в характере есть люди
                    if len(arr_sopernichestvo)!=0:
                        # добавление человека с максимальным баллом в группу
                        group.append(arr_sopernichestvo[0])
                        # Удалиение добавленного из характера
                        arr_sopernichestvo.pop(0)
                        arr_sopernichestvo.pop(0)
                        # логично что на одного человека незанятого стало меньше
                        count_people-=1

                        # если группа набралась
                        if len(group)==5:
                            # добавляем группу в большой список групп и обновляем её
                            arr_group.append(group)
                            group=[]

                            # если людей для новой группы не осталось, выходим из цикла
                            if count_people<5:
                                break

                    # Аналогично первому условию в этом цикле
                    if len(arr_sotrudnichestvo)!=0:
                        group.append(arr_sotrudnichestvo[0])
                        arr_sotrudnichestvo.pop(0)
                        arr_sotrudnichestvo.pop(0)
                        count_people-=1

                        if len(group)==5:
                            arr_group.append(group)
                            group=[]

                            if count_people<5:
                                break

                    # Аналогично первому условию в этом цикле
                    if len(arr_kompromis)!=0:
                        group.append(arr_kompromis[0])
                        arr_kompromis.pop(0)
                        arr_kompromis.pop(0)
                        count_people-=1

                        if len(group)==5:
                            arr_group.append(group)
                            group=[]

                            if count_people<5:
                                break

                    # Аналогично первому условию в этом цикле
                    if len(arr_izbeganie)!=0:
                        group.append(arr_izbeganie[0])
                        arr_izbeganie.pop(0)
                        arr_izbeganie.pop(0)
                        count_people-=1

                        if len(group)==5:
                            arr_group.append(group)
                            group=[]

                            if count_people<5:
                                break

                    # Аналогично первому условию в этом цикле
                    if len(arr_prispososoblenie)!=0:
                        group.append(arr_prispososoblenie[0])
                        arr_prispososoblenie.pop(0)
                        arr_prispososoblenie.pop(0)
                        count_people-=1

                        if len(group)==5:
                            arr_group.append(group)
                            group=[]

                            if count_people<5:
                                break
             
            # если все характеры полные                   
            else:
                # цикл пока не появятся характеры без людей
                for i in range(max_people):
                    pass

            # Сохраняем в бд группы
            for i in arr_group:
                G=Group(person_1=i[0], person_2=i[1], person_3=i[2], person_4=i[3], person_5=i[4])
                db.session.add(G)
                db.session.commit()

            # Удаляем из бд тэсты респондентов которые уже прошли тэст
            
            # набираем данные для отображения на странице
            data=[]

            # Добавление данных о созданных группах
            for i in range(len(arr_group)):
                data.append('Группа №'+str(i+1))
                for j in arr_group[i]:
                    select=User.query.filter_by(id=int(j)).first()
                    data.append(select.surname+' '+select.name+' '+select.middle_name)

            # Добавляем данные о тех, кто остался нерапспределённым
            last=[]
            for i in range(0, len(arr_sopernichestvo), 2):
                last.append(arr_sopernichestvo[i])

            for i in range(0, len(arr_sotrudnichestvo), 2):
                last.append(arr_sotrudnichestvo[i])

            for i in range(0, len(arr_kompromis), 2):
                last.append(arr_kompromis[i])

            for i in range(0, len(arr_izbeganie), 2):
                last.append(arr_izbeganie[i])

            for i in range(0, len(arr_prispososoblenie), 2):
                last.append(arr_prispososoblenie[i])

            # добавление персональных данных нераспределённых
            new_last=[]
            for i in last:
                select=User.query.filter_by(id=int(i)).first()
                new_last.append(select.surname+' '+select.name+' '+select.middle_name)

            # теперь нужны только персональные данные
            last=new_last

            # выборка данных админа
            select=User.query.filter_by(id=idd).first()

            # создание страницы админа
            return render_template('admin.html',
                surname=select.surname,
                name=select.name,
                middle_name=select.middle_name,
                data=data,
                last=last
                )

        else:
            pass

    # Выбор данных админа из бд
    select=User.query.filter_by(id=idd).first()

    # Создание страницы
    return render_template('admin.html',
        surname=select.surname,
        name=select.name,
        middle_name=select.middle_name,
        data='.',
        last='.'
        )

# Действия если запускается именно этот файл
if __name__=='__main__':
    pass