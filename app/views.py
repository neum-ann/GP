##!/usr/bin/env python
# -*- coding: utf-8 -*-

# Подключение модулей фласки
from app import app, db
from .forms import *
from app.models import *
from sqlalchemy import update
from flask import render_template, redirect, request, url_for, session

# Библиотеки для работы с графикой
import plotly
import numpy as np
plotly.tools.set_credentials_file(username='ViktorS', api_key='gk3itQcWHuFkAfuZleor')
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from plotly.offline import plot

# Подключение библиотек питона стандартные
import time
from time import gmtime, strftime

# Подключение собственных библиотек
from app.algorithm.step1 import work_at_answer
from app.algorithm.step2 import sorted_group

# Глобальные переменные
idd=0
result=''
start_time=0
finish_time=0
alldays=['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08', '2018-01-09', '2018-01-10', '2018-01-11', 
    '2018-01-12', '2018-01-13', '2018-01-14', '2018-01-15', '2018-01-16', '2018-01-17', '2018-01-18', '2018-01-19', '2018-01-20', '2018-01-21', '2018-01-22', '2018-01-23', 
    '2018-01-24', '2018-01-25', '2018-01-26', '2018-01-27', '2018-01-28', '2018-01-29', '2018-01-30', '2018-01-31',
    '2018-02-01', '2018-02-02', '2018-02-03', '2018-02-04', '2018-02-05', '2018-02-06', '2018-02-07', '2018-02-08', '2018-02-09', '2018-02-10', '2018-02-11', 
    '2018-02-12', '2018-02-13', '2018-02-14', '2018-02-15', '2018-02-16', '2018-02-17', '2018-02-18', '2018-02-19', '2018-02-20', '2018-02-21', '2018-02-22', '2018-02-23', 
    '2018-02-24', '2018-02-25', '2018-02-26', '2018-02-27', '2018-02-28', '2018-02-29', '2018-02-30', '2018-02-31', 
    '2018-03-01', '2018-03-02', '2018-03-03', '2018-03-04', '2018-03-05', '2018-03-06', '2018-03-07', '2018-03-08', '2018-03-09', '2018-03-10', '2018-03-11', 
    '2018-03-12', '2018-03-13', '2018-03-14', '2018-03-15', '2018-03-16', '2018-03-17', '2018-03-18', '2018-03-19', '2018-03-20', '2018-03-21', '2018-03-22', '2018-03-23', 
    '2018-03-24', '2018-03-25', '2018-03-26', '2018-03-27', '2018-03-28', '2018-03-29', '2018-03-30', '2018-03-31', 
    '2018-04-01', '2018-04-02', '2018-04-03', '2018-04-04', '2018-04-05', '2018-04-06', '2018-04-07', '2018-04-08', '2018-04-09', '2018-04-10', '2018-04-11', 
    '2018-04-12', '2018-04-13', '2018-04-14', '2018-04-15', '2018-04-16', '2018-04-17', '2018-04-18', '2018-04-19', '2018-04-20', '2018-04-21', '2018-04-22', '2018-04-23', 
    '2018-04-24', '2018-04-25', '2018-04-26', '2018-04-27', '2018-04-28', '2018-04-29', '2018-04-30', '2018-04-31', 
    '2018-05-01', '2018-05-02', '2018-05-03', '2018-05-04', '2018-05-05', '2018-05-06', '2018-05-07', '2018-05-08', '2018-05-09', '2018-05-10', '2018-05-11', 
    '2018-05-12', '2018-05-13', '2018-05-14', '2018-05-15', '2018-05-16', '2018-05-17', '2018-05-18', '2018-05-19', '2018-05-20', '2018-05-21', '2018-05-22', '2018-05-23', 
    '2018-05-24', '2018-05-25', '2018-05-26', '2018-05-27', '2018-05-28', '2018-05-29', '2018-05-30', '2018-05-31', 
    '2018-06-01', '2018-06-02', '2018-06-03', '2018-06-04', '2018-06-05', '2018-06-06', '2018-06-07', '2018-06-08', '2018-06-09', '2018-06-10', '2018-06-11', 
    '2018-06-12', '2018-06-13', '2018-06-14', '2018-06-15', '2018-06-16', '2018-06-17', '2018-06-18', '2018-06-19', '2018-06-20', '2018-06-21', '2018-06-22', '2018-06-23', 
    '2018-06-24', '2018-06-25', '2018-06-26', '2018-06-27', '2018-06-28', '2018-06-29', '2018-06-30', '2018-06-31',
    '2018-07-01', '2018-07-02', '2018-07-03', '2018-07-04', '2018-07-05', '2018-07-06', '2018-07-07', '2018-07-08', '2018-07-09', '2018-07-10', '2018-07-11', 
    '2018-07-12', '2018-07-13', '2018-07-14', '2018-07-15', '2018-07-16', '2018-07-17', '2018-07-18', '2018-07-19', '2018-07-20', '2018-07-21', '2018-07-22', '2018-07-23', 
    '2018-07-24', '2018-07-25', '2018-07-26', '2018-07-27', '2018-07-28', '2018-07-29', '2018-07-30', '2018-07-31', 
    '2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05', '2018-08-06', '2018-08-07', '2018-08-08', '2018-08-09', '2018-08-10', '2018-08-11', 
    '2018-08-12', '2018-08-13', '2018-08-14', '2018-08-15', '2018-08-16', '2018-08-17', '2018-08-18', '2018-08-19', '2018-08-20', '2018-08-21', '2018-08-22', '2018-08-23', 
    '2018-08-24', '2018-08-25', '2018-08-26', '2018-08-27', '2018-08-28', '2018-08-29', '2018-08-30', '2018-08-31', 
    '2018-09-01', '2018-09-02', '2018-09-03', '2018-09-04', '2018-09-05', '2018-09-06', '2018-09-07', '2018-09-08', '2018-09-09', '2018-09-10', '2018-09-11', 
    '2018-09-12', '2018-09-13', '2018-09-14', '2018-09-15', '2018-09-16', '2018-09-17', '2018-09-18', '2018-09-19', '2018-09-20', '2018-09-21', '2018-09-22', '2018-09-23', 
    '2018-09-24', '2018-09-25', '2018-09-26', '2018-09-27', '2018-09-28', '2018-09-29', '2018-09-30', '2018-09-31', 
    '2018-10-01', '2018-10-02', '2018-10-03', '2018-10-04', '2018-10-05', '2018-10-06', '2018-10-07', '2018-10-08', '2018-10-09', '2018-10-10', '2018-10-11', 
    '2018-10-12', '2018-10-13', '2018-10-14', '2018-10-15', '2018-10-16', '2018-10-17', '2018-10-18', '2018-10-19', '2018-10-20', '2018-10-21', '2018-10-22', '2018-10-23', 
    '2018-10-24', '2018-10-25', '2018-10-26', '2018-10-27', '2018-10-28', '2018-10-29', '2018-10-30', '2018-10-31', 
    '2018-11-01', '2018-11-02', '2018-11-03', '2018-11-04', '2018-11-05', '2018-11-06', '2018-11-07', '2018-11-08', '2018-11-09', '2018-11-10', '2018-11-11', 
    '2018-11-12', '2018-11-13', '2018-11-14', '2018-11-15', '2018-11-16', '2018-11-17', '2018-11-18', '2018-11-19', '2018-11-20', '2018-11-21', '2018-11-22', '2018-11-23', 
    '2018-11-24', '2018-11-25', '2018-11-26', '2018-11-27', '2018-11-28', '2018-11-29', '2018-11-30', '2018-11-31', 
    '2018-12-01', '2018-12-02', '2018-12-03', '2018-12-04', '2018-12-05', '2018-12-06', '2018-12-07', '2018-12-08', '2018-12-09', '2018-12-10', '2018-12-11', 
    '2018-12-12', '2018-12-13', '2018-12-14', '2018-12-15', '2018-12-16', '2018-12-17', '2018-12-18', '2018-12-19', '2018-12-20', '2018-12-21', '2018-12-22', '2018-12-23', 
    '2018-12-24', '2018-12-25', '2018-12-26', '2018-12-27', '2018-12-28', '2018-12-29', '2018-12-30', '2018-12-31']

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

                    # Проверка выполнял ли респондент тэст или нет
                    select=Results.query.filter_by(id_user=idd).first()

                    # Если он не пустой то тэст выполнялся и идёт он нахрен
                    if select!=None:

                        return render_template('main.html',
                            form=form_login,
                            Error='Вы уже проходили тест!'
                            )

                    # Если запрос пустой то он не выполнял тэст, тогда пусть выполняет
                    else:
                        
                        return redirect('/test')

                # Если заходит админинстратор
                elif select.role=='admin':
                    idd=select.id

                    return redirect('/admin')

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

            # Проверка почты на корректность ещё раз
            i=0
            index=0
            # Проходимся по каждому символу в строке
            while i<len(email):
                # если встречаем собаку то
                if email[i]=='@':
                    # объявляем переменные плюс за наличии собаки увеличиваем индекс
                    index+=1
                    i+=1
                    word=''

                    # продолжае цикл
                    while i<len(email):
                        # пока не встретим точку записываем слово
                        if email[i]!='.':

                            word+=email[i]
                        # если встретили точку
                        else:
                            # проверяем на существующие почты
                            i+=1
                            if word=='yandex':

                                # прибавляем к индексу 1 за соответсвие почте
                                index+=1
                                word=''

                                # продолжаем цикл
                                while i<len(email):
                                    # прибовляем всё что осталось от почты
                                    word+=email[i]

                                    i+=1
                            # следующие 2 условия по той же схеме

                            elif word=='gmail':

                                index+=1
                                word=''

                                while i<len(email):

                                    word+=email[i]

                                    i+=1

                            elif word=='mail':

                                index+=1
                                word=''

                                while i<len(email):

                                    word+=email[i]

                                    i+=1
                           
                            break

                        i+=1

                    break

                i+=1

            # проверяем оставшуюся часть почты на ру или ком
            if word=='ru':

                # прибавляем индекс за соответсвие
                index+=1
            # Аналогично
            elif word=='com':

                index+=1

            # если нет трёх соответсвий то почта некорректна
            if index!=3:

                # сообщение об ошибки
                return render_template('reg_resp.html',
                        form=form_resp,
                        Error='Ошибка! Почта указана некорректно.'
                    )

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

                        return redirect('/start_test')

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

                return redirect('/start_test')

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

                    return redirect('/admin')

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

            return redirect('/admin')     

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
    global idd, result, start_time, finish_time

    # Создание формы для сбора ответов
    form_answ=Answer(request.form)

    # Обработка ответов
    if request.form and True:
        # время окончания прохождения тэста
        finish_time=time.time()

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

        # Переменная для сохранения даты что бы знаить когда был пройден тэст
        data=''

        # Генерим сегодняшнюю дату
        data=strftime("%Y-%m-%d %H:%M:%S", gmtime())

        # итоговое время прохождения тэста
        total_time=finish_time-start_time

        # округление этого числа
        total_time=round(total_time)

        # Сохранение ответов респондента в бд
        R=Results(id_user=idd, count_sopernichestvo=count_sopernichestvo, count_sotrudnichestvo=count_sotrudnichestvo, count_kompromis=count_kompromis, count_izbeganie=count_izbeganie, count_prispososoblenie=count_prispososoblenie, more_count=more_count, delete='-', data=data, time=total_time)
        db.session.add(R)
        db.session.commit()

        # Сохранение характера в таблице пользователей
        select=User.query.filter_by(id=idd).first()
        select.result=more_count
        db.session.commit()

        # Объявление формы
        form_login=Login(request.form)

        # Передача результата на страницу с результатом
        result=more_count

        # После ответа переход на главную
        # return render_template('main.html',
            # form=form_login,
            # Error='Спасибо за прохождение тэста!'
        # )

        # После ответа результат
        return redirect('/result')

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

    # Время начала прохождения тэста
    start_time=time.time()

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
    global result

    # Переводим результат в удобный для пользователя
    txt_result=''

    if result=='prisposoblenie':
        txt_result='Приспособление'

    elif result=='sopernichestvo':
        txt_result='Соперничество'

    elif result=='sotrudnichestvo':
        txt_result='Сотрудничество'

    elif result=='kompromis':
        txt_result='Компромис'

    elif result=='izbeganie':
        txt_result='Избегание'

    # Если ни один из результатовне подошёл
    else:

        # Вывод ошибки
        return render_template('result.html',
            Error='Ошибка! Ни один из результатов не подходит, сообщите нам об этой ошибке.'
            )

    # Создание страницы
    return render_template('result.html',
        txt_result=txt_result
        )

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

                    # проверка на удаление
                    select=Results.query.filter_by(id_user=i.id).first()

                    # если респондент не удалён
                    if select.delete!='+':
                        arr_people.append(i.id)

                    # если респондент удалён
                    else:
                        pass

                    # востанавливаем селект для цикла
                    select=User.query.filter_by(role='resp').all()
            
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

            print(len(arr_people))
            # Если нет респондентов
            if len(arr_people)<5:

                # выборка данных админа
                select=User.query.filter_by(id=idd).first()

                return render_template('admin.html',
                    surname=select.surname,
                    name=select.name,
                    middle_name=select.middle_name,
                    data='.',
                    last='.',
                    Error='Респондентов меньше 5.'
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

                    # Если результат не удалён, то
                    if select.delete=='-':

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

                    # если результат удалён
                    else:
                        pass

                # Если запрос пустой
                # else:

                    # выборка данных админа
                    # select=User.query.filter_by(id=idd).first()

                    # return render_template('admin.html',
                    #     surname=select.surname,
                    #     name=select.name,
                    #     middle_name=select.middle_name,
                    #     data='.',
                    #     last='.',
                    #     Error='Неизвестная ошибка! Этого просто не может быть! Код ошибки #003. Сообщите нам об этом пожалуйста!'
                    # )

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

                    max_people=int(len(arr_sotrudnichestvo)/2)

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
            
            # набираем данные для отображения на странице
            data=[]

            # Добавление данных о созданных группах
            for i in range(len(arr_group)):
                data.append('Группа №'+str(i+1))

                for j in arr_group[i]:
                    select=User.query.filter_by(id=int(j)).first()
                    data.append(select.surname+' '+select.name+' Психотип: '+select.result)

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
                new_last.append(select.surname+' '+select.name+' Психотип: '+select.result)

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

        # если нужно сохранить все сгенерированные группы
        elif to_do=='save_all':
            
            # К сожалению кэш обновился, поэтому веьс процесс генерации групп происходит заного

            # Собираем всех респондентов
            arr_people=[]
            select=User.query.filter_by(role='resp').all()

            # Если запрос не пустой
            if select!=None:
                for i in select:
                    
                    # проверка на удаление
                    select=Results.query.filter_by(id_user=i.id).first()

                    # если респондент не удалён
                    if select.delete!='+':
                        arr_people.append(i.id)

                    # если респондент удалён
                    else:
                        pass

                    # востанавливаем селект для цикла
                    select=User.query.filter_by(role='resp').all()
            
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

            # Если нет респондентов
            if len(arr_people)<5:

                # выборка данных админа
                select=User.query.filter_by(id=idd).first()

                return render_template('admin.html',
                    surname=select.surname,
                    name=select.name,
                    middle_name=select.middle_name,
                    data='.',
                    last='.',
                    Error='Респондентов меньше 5.'
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

                    # Если результат не удалён, то
                    if select.delete=='-':

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

                    # если результат удалён
                    else:
                        pass

                # Если запрос пустой
                # else:

                    # выборка данных админа
                    # select=User.query.filter_by(id=idd).first()

                    # return render_template('admin.html',
                    #     surname=select.surname,
                    #     name=select.name,
                    #     middle_name=select.middle_name,
                    #     data='.',
                    #     last='.',
                    #     Error='Неизвестная ошибка! Этого просто не может быть! Код ошибки #003. Сообщите нам об этом пожалуйста!'
                    # )

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

                    max_people=int(len(arr_sotrudnichestvo)/2)

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
            # Прохожимся по всем группам
            for i in arr_group:
                # В каждой группе по 5 человек, поэтому проходимся по кажлому из них
                for j in range(5):
    
                    # выбираем строку которую надо удалить и удаляем
                    db.session.query(Results).filter_by(id_user=i[j]).update({'delete':'+'})
                    db.session.commit()

            # выборка данных админа
            select=User.query.filter_by(id=idd).first()

            # создание страницы админа
            return render_template('admin.html',
                surname=select.surname,
                name=select.name,
                middle_name=select.middle_name,
                masage='Группы сгенирированны'
                )

        # 
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

# Возвращает страницу для создания групп вручную
@app.route('/group_create', methods=['GET','POST'])
def group_create():
    # Объявление переменных
    arr_free_resp=[]

    # Выбриаем нераспределённых респондентов
    select=Results.query.filter_by(delete='-').all()
    
    # Проходимся циклом по всем нераспределённым
    for i in select:
        # Создаём место для его данных
        bucket=[]
        # Выбераем его айди в таблице юзеров
        id_resp=i.id_user
        # Делаем его выборку данных из бд
        select=User.query.filter_by(id=id_resp).first()
        # Записываем его данные
        arr_free_resp.append(str(select.id)+' | '+select.surname+' '+select.name+' Характер:'+select.result)
        # откатываем запрос данных
        select=Results.query.filter_by(delete='-').all()

    # Создание формы для сбора ответов
    form_group_create=Group_create(request.form)

    # Обработка ответов
    if request.form and True:
        
        # Извлечение данных
        person_1=form_group_create.person_1.data
        person_2=form_group_create.person_2.data
        person_3=form_group_create.person_3.data
        person_4=form_group_create.person_4.data
        person_5=form_group_create.person_5.data

        # Проверка на заполненность форм
        if len(person_1)==0 or len(person_2)==0 or len(person_3)==0 or len(person_4)==0 or len(person_5)==0:

            # вывод ошибки
            return render_template('group_create.html',
                form=form_group_create,
                arr_free_resp=arr_free_resp,
                Error='Одно из полей незаполненно!'
                )

        # Если все данные заполненны
        else:
            
            # Проверка на существование пользователя
            select=Results.query.filter_by(id_user=person_1).first()
            if select==None:
                
                # Вывод ошибки
                return render_template('group_create.html',
                    form=form_group_create,
                    arr_free_resp=arr_free_resp,
                    Error='Поле 1: Такого пользователя не существует'
                    )

            # Проверка на существование пользователя
            select=Results.query.filter_by(id_user=person_2).first()
            if select==None:
                
                # Вывод ошибки
                return render_template('group_create.html',
                    form=form_group_create,
                    arr_free_resp=arr_free_resp,
                    Error='Поле 2: Такого пользователя не существует'
                    )

            # Проверка на существование пользователя
            select=Results.query.filter_by(id_user=person_3).first()
            if select==None:
                
                # Вывод ошибки
                return render_template('group_create.html',
                    form=form_group_create,
                    arr_free_resp=arr_free_resp,
                    Error='Поле 3: Такого пользователя не существует'
                    )

            # Проверка на существование пользователя
            select=Results.query.filter_by(id_user=person_4).first()
            if select==None:
                
                # Вывод ошибки
                return render_template('group_create.html',
                    form=form_group_create,
                    arr_free_resp=arr_free_resp,
                    Error='Поле 4: Такого пользователя не существует'
                    )

            # Проверка на существование пользователя
            select=Results.query.filter_by(id_user=person_5).first()
            if select==None:
                
                # Вывод ошибки
                return render_template('group_create.html',
                    form=form_group_create,
                    arr_free_resp=arr_free_resp,
                    Error='Поле 5: Такого пользователя не существует'
                    )

            # Если мы дошли до сюда то всё хорошо и можно создавать группу
            G=Group(person_1=person_1, person_2=person_2, person_3=person_3, person_4=person_4, person_5=person_5)
            db.session.add(G)
            db.session.commit()

            # Теперь делаем отметку что они распределены
            db.session.query(Results).filter_by(id_user=person_1).update({'delete':'+'})
            db.session.query(Results).filter_by(id_user=person_2).update({'delete':'+'})
            db.session.query(Results).filter_by(id_user=person_3).update({'delete':'+'})
            db.session.query(Results).filter_by(id_user=person_4).update({'delete':'+'})
            db.session.query(Results).filter_by(id_user=person_5).update({'delete':'+'})
            db.session.commit()

            # Рендер страницы
            return render_template('group_create.html',
                form=form_group_create,
                arr_free_resp=arr_free_resp,
                masage='Группа создана'
                )

    # Рендер страницы
    return render_template('group_create.html',
        form=form_group_create,
        arr_free_resp=arr_free_resp
        )

# Возвращает страницу для просмотра существующих групп и ещё не распределённых респондентов
@app.route('/look_at_group', methods=['GET','POST'])
def look_at_group():
    # Объявление переменных
    arr_free_resp=[]
    arr_group=[]
    count=1

    # Выбираем уже созданные группы
    select=Group.query.filter_by().all()
    
    # Цикл по всем созданным группам
    for i in select:
        # За каждую итерацию будет добавляться одна группа
        bucket=[]
        # Записываем номер группы и добавляем
        text='Группа №'+str(count)
        arr_group.append(text)

        # Добавляем первого участника
        id_resp=i.person_1
        # Выбираем его данные из бд
        select=User.query.filter_by(id=id_resp).first()
        # Добавляем данные в группу
        arr_group.append(select.surname+' '+select.name+' Характер:'+select.result)
        # И так далее

        id_resp=i.person_2
        select=User.query.filter_by(id=id_resp).first()
        arr_group.append(select.surname+' '+select.name+' Характер:'+select.result)

        id_resp=i.person_3
        select=User.query.filter_by(id=id_resp).first()
        arr_group.append(select.surname+' '+select.name+' Характер:'+select.result)

        id_resp=i.person_4
        select=User.query.filter_by(id=id_resp).first()
        arr_group.append(select.surname+' '+select.name+' Характер:'+select.result)

        id_resp=i.person_5
        select=User.query.filter_by(id=id_resp).first()
        arr_group.append(select.surname+' '+select.name+' Характер:'+select.result)

        # Прибовляем каунт для следующей группы
        count+=1
        # Поскольку селект был изменён нужно снова запросить старый
        select=Group.query.filter_by().all()


    # Выбриаем нераспределённых респондентов
    select=Results.query.filter_by(delete='-').all()
    
    # Проходимся циклом по всем нераспределённым
    for i in select:
        # Создаём место для его данных
        bucket=[]
        # Выбераем его айди в таблице юзеров
        id_resp=i.id_user
        # Делаем его выборку данных из бд
        select=User.query.filter_by(id=id_resp).first()
        # Записываем его данные
        arr_free_resp.append(select.surname+' '+select.name+' Характер:'+select.result)
        # откатываем запрос данных
        select=Results.query.filter_by(delete='-').all()

    # Рендерим страницу
    return render_template('look_at_group.html',
        arr_group=arr_group,
        arr_free_resp=arr_free_resp
        )

# Возвращает страницу с статистикой
@app.route('/statistic', methods=['GET','POST'])
def statistic():

    # Создание графика о количестве характеров
    # счётчики характеров
    sopernichestvo=0
    sotrudnichestvo=0
    kompromis=0
    izbeganie=0
    prisposoblenie=0

    # Получаем информацию для графика
    select=Results.query.filter_by().all()

    # Проходимся по всем результатам для сбора данных
    for i in select:
        if i.more_count=='sopernichestvo':
            sopernichestvo+=1

            continue

        elif i.more_count=='sotrudnichestvo':
            sotrudnichestvo+=1

            continue

        elif i.more_count=='kompromis':
            kompromis+=1

            continue

        elif i.more_count=='izbeganie':
            izbeganie+=1

            continue

        elif i.more_count=='prisposoblenie':
            prisposoblenie+=1

            continue

    # Создание графика количества характеров
    trace=go.Bar(x=['Соперничество', 'Компромис', 'Избегание', 'Сотрудничество', 'Приспособление'], y=[sopernichestvo, kompromis, izbeganie, sotrudnichestvo, prisposoblenie])
    data=[trace]
    layout=go.Layout(title='Количество характеров', width=750, height=500)
    fig=go.Figure(data=data, layout=layout)

    # Сохроняем график как картинку
    # temp='app/static/grafics/haracter.png'
    # py.image.save_as(fig, filename=temp)

    # Сохроняем график как скрипт
    plot(fig,show_link = True, filename = 'app/static/haracter.html')

    # Достаём данные из файла
    f=open('app/static/haracter.html', 'r', encoding="utf-8")
    file=f.read()
    f.close()

    # Переменная для хранения скрипта
    script_1=''

    # Проходимся по всему файлу и удаляем начальные тэги и финальные
    for i in range(49, len(file)-14):
        script_1+=file[i]



    # Создание графика о дате прохождения тэста по дням
    # Объявление переменных
    arr_days=[]
    count_days=[]

    # Выборка данных из бд
    select=Results.query.filter_by().all()

    # обработа данных из бд
    for i in select:
        # рассмотрим каждую дату под микроскопом
        data_str=i.data
        day=''

        # отделим время из даты
        for j in data_str:
            # если пробела нет то ещё идёт дата
            if j!=' ':
                day+=j

            # если встретили пробел, то началось время
            else:
                # сохроняем результат
                arr_days.append(day)

                # выходим
                break

    # ищем пересечение всех дней и дней тэстов
    for i in alldays:
        # каждый день рассмотрим под микроскопом
        count=0

        # здесь каждая дата сравнивается с массивом дат результатов
        for j in arr_days:
            # и если одинаковые они то в каунт записывается
            if i==j:
                count+=1

        # ну и сохраняем количество пересечений
        count_days.append(count)

    # создаём график
    trace=go.Scatter(x=alldays, y=count_days)
    data=[trace]
    layout=go.Layout(title='Количество прохождений тэста в день', width=750, height=500)
    fig=go.Figure(data=data, layout=layout)

    # Сохроняем график как картинку
    # temp='app/static/grafics/count_test_in_day.png'
    # py.image.save_as(fig, filename=temp)

    # Сохроняем график как скрипт
    plot(fig,show_link = True, filename = 'app/static/count_test_in_day.html')

    # Достаём данные из файла
    f=open('app/static/count_test_in_day.html', 'r', encoding="utf-8")
    file=f.read()
    f.close()

    # Переменная для хранения скрипта
    script_2=''

    # Проходимся по всему файлу и удаляем начальные тэги и финальные
    for i in range(49, len(file)-14):
        script_2+=file[i]



    # Создание графика о том сколько времени на тэст тратит тот или иной характер
    sopernichestvo_time=0
    sotrudnichestvo_time=0
    kompromis_time=0
    izbeganie_time=0
    prisposoblenie_time=0

    select=Results.query.filter_by().all()

    for i in select:
        time=i.time

        if i.more_count=='sopernichestvo':
            sopernichestvo_time+=time

            continue

        elif i.more_count=='sotrudnichestvo':
            sotrudnichestvo_time+=time

            continue

        elif i.more_count=='kompromis':
            kompromis_time+=time

            continue

        elif i.more_count=='izbeganie':
            izbeganie_time+=time

            continue

        elif i.more_count=='prisposoblenie':
            prisposoblenie_time+=time

            continue

    if sopernichestvo!=0:
        sopernichestvo_time=sopernichestvo_time/sopernichestvo
    
    if sotrudnichestvo!=0:
        sotrudnichestvo_time=sotrudnichestvo_time/sotrudnichestvo
    
    if kompromis!=0:
        kompromis_time=kompromis_time/kompromis
    
    if izbeganie!=0:
        izbeganie_time=izbeganie_time/izbeganie
    
    if prisposoblenie!=0:
        prisposoblenie_time=prisposoblenie_time/prisposoblenie

    sopernichestvo_time=round(sopernichestvo_time)
    sotrudnichestvo_time=round(sotrudnichestvo_time)
    kompromis_time=round(kompromis_time)
    izbeganie_time=round(izbeganie_time)
    prisposoblenie_time=round(prisposoblenie_time)

    # print([sopernichestvo_time, kompromis_time, izbeganie_time, sotrudnichestvo_time, prisposoblenie_time])

    # Создание графика
    trace=go.Bar(x=['Соперничество', 'Компромис', 'Избегание', 'Сотрудничество', 'Приспособление'], y=[sopernichestvo_time, kompromis_time, izbeganie_time, sotrudnichestvo_time, prisposoblenie_time])
    data=[trace]
    layout=go.Layout(title='Среднее время прохождения теста характером', width=750, height=500)
    fig=go.Figure(data=data, layout=layout)

    # Сохроняем график как картинку
    # temp='app/static/grafics/time_haracter.png'
    # py.image.save_as(fig, filename=temp)

    # Сохроняем график как скрипт
    plot(fig,show_link = True, filename = 'app/static/time_haracter.html')

    # Достаём данные из файла
    f=open('app/static/time_haracter.html', 'r', encoding="utf-8")
    file=f.read()
    f.close()

    # Переменная для хранения скрипта
    script_3=''

    # Проходимся по всему файлу и удаляем начальные тэги и финальные
    for i in range(49, len(file)-14):
        script_3+=file[i]


    # Создание страницы
    # Начало страницы до парада граффиков
    before_script='''
<html>
    <head>
        <title>GROUP CREATOR - Сбор статистики</title>
        <meta charset='utf-8'>
        <link rel="stylesheet" type="text/css" href="../static/style.css">    
    </head>
    <body>
        <header class="page--centered m25 p25 clearfix">
        
            <a href="/main">
                <div class="header__menu fl_l">
                    <img src="../static/list.png">
                    <span class="header__menu-text"><span class='txt_up'>group creator</span></span>
                </div>
            </a>
            <a onclick="show('block')">
                <div class="header__user fl_r">
                    <img src="../static/user_circle.png">
                </div>
            </a>
        
        </header>

        <div class='content'>
            <div class="page--centered content">
                <div class="subscribe">
    '''

    # Конец страницы после граффиков
    after_script='''
                    <div class="subscribe__button-back">
                        <a href="/admin">
                            <div class="subscribe__button-b">
                                <span class='txt_up'>назад</span>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        </div>

    <footer class="page--centered p25 clearfix">
        <div class="footer__menu fl_l">
            <a class="footer__menu-link" href="/about_us"><span class='txt_up'>о нас</span></a>
            <a class="footer__menu-link" href="/instruction"><span class='txt_up'>инструкция</span></a>
        </div>

        <div class="footer__menu-follow fl_r">
            <a href="https://github.com/neum-ann"><span class='txt_up'>github</span></a>
        </div>

        <div class="footer__menu-c">
            <a href="https://t.me/neum_ann"><span class="footer__menu-c-year">&copy;2018 </span><span class='txt_up'>neumann a.</span></a>
        </div>
    </footer>
    
    </body>
</html>
    '''

    # Собираем страницу
    file=before_script+'<div class="zero_height"><table><tr><td>'+script_1+'</td></tr><tr><td>'+script_2+'</td></tr><tr><td>'+script_3+'</td></tr></table></div>'+after_script

    # Сохранение кода в файл
    f=open('app/templates/statistic.html', 'w', encoding="utf-8")
    f.write(file)
    f.close()

    # Рендер страницы
    return render_template('statistic.html')

# Действия если запускается именно этот файл
if __name__=='__main__':
    pass
