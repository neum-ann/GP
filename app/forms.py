#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Подключение модулей фласки
from flask_wtf import Form
from wtforms.validators import DataRequired, Email
from wtforms import StringField, PasswordField, RadioField, BooleanField, FileField, TextAreaField, SubmitField

# Форма для входа на сайт
class Login(Form):
	login=StringField('Логин', validators=[DataRequired()])
	password=PasswordField('Пароль', validators=[DataRequired()])

# Форма для регистрации респондента
class Respondent(Form):
	email=StringField('E-mail', validators=[Email(), DataRequired()])
	login=StringField('Логин', validators=[DataRequired()])
	password=PasswordField('Пароль', validators=[DataRequired()])
	surname=StringField('Фамилия', validators=[DataRequired()])
	name=StringField('Имя', validators=[DataRequired()])
	middle_name=StringField('Отчество', validators=[DataRequired()])

# Форма для регистрации админа
class Admin(Form):
	email=StringField('E-mail', validators=[Email(), DataRequired()])
	login=StringField('Логин', validators=[DataRequired()])
	surname=StringField('Фамилия', validators=[DataRequired()])
	name=StringField('Имя', validators=[DataRequired()])
	middle_name=StringField('Отчество', validators=[DataRequired()])

# Форма для сбора ответов
class Answer(Form):
	# Чекбосы
	# answer1_A=BooleanField('Ответ 1', validators=[DataRequired()])
	# answer1_B=BooleanField('Ответ 1', validators=[DataRequired()])
	# answer2_A=BooleanField('Ответ 2', validators=[DataRequired()])
	# answer2_B=BooleanField('Ответ 2', validators=[DataRequired()])
	# answer3_A=BooleanField('Ответ 3', validators=[DataRequired()])
	# answer3_B=BooleanField('Ответ 3', validators=[DataRequired()])
	# answer4_A=BooleanField('Ответ 4', validators=[DataRequired()])
	# answer4_B=BooleanField('Ответ 4', validators=[DataRequired()])
	# answer5_A=BooleanField('Ответ 5', validators=[DataRequired()])
	# answer5_B=BooleanField('Ответ 5', validators=[DataRequired()])
	# answer6_A=BooleanField('Ответ 6', validators=[DataRequired()])
	# answer6_B=BooleanField('Ответ 6', validators=[DataRequired()])
	# answer7_A=BooleanField('Ответ 7', validators=[DataRequired()])
	# answer7_B=BooleanField('Ответ 7', validators=[DataRequired()])
	# answer8_A=BooleanField('Ответ 8', validators=[DataRequired()])
	# answer8_B=BooleanField('Ответ 8', validators=[DataRequired()])
	# answer9_A=BooleanField('Ответ 9', validators=[DataRequired()])
	# answer9_B=BooleanField('Ответ 9', validators=[DataRequired()])
	# answer10_A=BooleanField('Ответ 10', validators=[DataRequired()])
	# answer10_B=BooleanField('Ответ 10', validators=[DataRequired()])
	# answer11_A=BooleanField('Ответ 11', validators=[DataRequired()])
	# answer11_B=BooleanField('Ответ 11', validators=[DataRequired()])
	# answer12_A=BooleanField('Ответ 12', validators=[DataRequired()])
	# answer12_B=BooleanField('Ответ 12', validators=[DataRequired()])
	# answer13_A=BooleanField('Ответ 13', validators=[DataRequired()])
	# answer13_B=BooleanField('Ответ 13', validators=[DataRequired()])
	# answer14_A=BooleanField('Ответ 14', validators=[DataRequired()])
	# answer14_B=BooleanField('Ответ 14', validators=[DataRequired()])
	# answer15_A=BooleanField('Ответ 15', validators=[DataRequired()])
	# answer15_B=BooleanField('Ответ 15', validators=[DataRequired()])
	# answer16_A=BooleanField('Ответ 16', validators=[DataRequired()])
	# answer16_B=BooleanField('Ответ 16', validators=[DataRequired()])
	# answer17_A=BooleanField('Ответ 17', validators=[DataRequired()])
	# answer17_B=BooleanField('Ответ 17', validators=[DataRequired()])
	# answer18_A=BooleanField('Ответ 18', validators=[DataRequired()])
	# answer18_B=BooleanField('Ответ 18', validators=[DataRequired()])
	# answer19_A=BooleanField('Ответ 19', validators=[DataRequired()])
	# answer19_B=BooleanField('Ответ 19', validators=[DataRequired()])
	# answer20_A=BooleanField('Ответ 20', validators=[DataRequired()])
	# answer20_B=BooleanField('Ответ 20', validators=[DataRequired()])
	# answer21_A=BooleanField('Ответ 21', validators=[DataRequired()])
	# answer21_B=BooleanField('Ответ 21', validators=[DataRequired()])
	# answer22_A=BooleanField('Ответ 22', validators=[DataRequired()])
	# answer22_B=BooleanField('Ответ 22', validators=[DataRequired()])
	# answer23_A=BooleanField('Ответ 23', validators=[DataRequired()])
	# answer23_B=BooleanField('Ответ 23', validators=[DataRequired()])
	# answer24_A=BooleanField('Ответ 24', validators=[DataRequired()])
	# answer24_B=BooleanField('Ответ 24', validators=[DataRequired()])
	# answer25_A=BooleanField('Ответ 25', validators=[DataRequired()])
	# answer25_B=BooleanField('Ответ 25', validators=[DataRequired()])
	# answer26_A=BooleanField('Ответ 26', validators=[DataRequired()])
	# answer26_B=BooleanField('Ответ 26', validators=[DataRequired()])
	# answer27_A=BooleanField('Ответ 27', validators=[DataRequired()])
	# answer27_B=BooleanField('Ответ 27', validators=[DataRequired()])
	# answer28_A=BooleanField('Ответ 28', validators=[DataRequired()])
	# answer28_B=BooleanField('Ответ 28', validators=[DataRequired()])
	# answer29_A=BooleanField('Ответ 29', validators=[DataRequired()])
	# answer29_B=BooleanField('Ответ 29', validators=[DataRequired()])
	# answer30_A=BooleanField('Ответ 30', validators=[DataRequired()])
	# answer30_B=BooleanField('Ответ 30', validators=[DataRequired()])

	# Для радио
	answer1=RadioField('Ответ 1', choices=[('A',''),('B','')])
	answer2=RadioField('Ответ 2', choices=[('A',''),('B','')])
	answer3=RadioField('Ответ 3', choices=[('A',''),('B','')])
	answer4=RadioField('Ответ 4', choices=[('A',''),('B','')])
	answer5=RadioField('Ответ 5', choices=[('A',''),('B','')])
	answer6=RadioField('Ответ 6', choices=[('A',''),('B','')])
	answer7=RadioField('Ответ 7', choices=[('A',''),('B','')])
	answer8=RadioField('Ответ 8', choices=[('A',''),('B','')])
	answer9=RadioField('Ответ 9', choices=[('A',''),('B','')])
	answer10=RadioField('Ответ 10', choices=[('A',''),('B','')])
	answer11=RadioField('Ответ 11', choices=[('A',''),('B','')])
	answer12=RadioField('Ответ 12', choices=[('A',''),('B','')])
	answer13=RadioField('Ответ 13', choices=[('A',''),('B','')])
	answer14=RadioField('Ответ 14', choices=[('A',''),('B','')])
	answer15=RadioField('Ответ 15', choices=[('A',''),('B','')])
	answer16=RadioField('Ответ 16', choices=[('A',''),('B','')])
	answer17=RadioField('Ответ 17', choices=[('A',''),('B','')])
	answer18=RadioField('Ответ 18', choices=[('A',''),('B','')])
	answer19=RadioField('Ответ 19', choices=[('A',''),('B','')])
	answer20=RadioField('Ответ 20', choices=[('A',''),('B','')])
	answer21=RadioField('Ответ 21', choices=[('A',''),('B','')])
	answer22=RadioField('Ответ 22', choices=[('A',''),('B','')])
	answer23=RadioField('Ответ 23', choices=[('A',''),('B','')])
	answer24=RadioField('Ответ 24', choices=[('A',''),('B','')])
	answer25=RadioField('Ответ 25', choices=[('A',''),('B','')])
	answer26=RadioField('Ответ 26', choices=[('A',''),('B','')])
	answer27=RadioField('Ответ 27', choices=[('A',''),('B','')])
	answer28=RadioField('Ответ 28', choices=[('A',''),('B','')])
	answer29=RadioField('Ответ 29', choices=[('A',''),('B','')])
	answer30=RadioField('Ответ 30', choices=[('A',''),('B','')])

# Форма для создания групп
class Group_create(Form):
	person_1=StringField('Первый участник группы', validators=[DataRequired()])
	person_2=StringField('Второй участник группы', validators=[DataRequired()])
	person_3=StringField('Третий участник группы', validators=[DataRequired()])
	person_4=StringField('Четвёртный учатник группы', validators=[DataRequired()])
	person_5=StringField('Пятый участник группы', validators=[DataRequired()])
	person_6=StringField('Пятый участник группы', validators=[DataRequired()])
	person_7=StringField('Пятый участник группы', validators=[DataRequired()])
	count=RadioField('Количество человек в группах', choices=[('3','По 3 человека'), ('4','По 4 человека'), ('5','По 5 человек'), ('6','По 6 человек'), ('7','По 7 человек')])

# Форма для сохранения конкретной группы
class Save_this(Form):
	number=StringField('Номер группы для сохранения', validators=[DataRequired()])

# Форма для выбора количества человек для генерации групп
class Generation_group(Form):
	count=RadioField('Количество человек в группах', choices=[('3','По 3 человека'), ('4','По 4 человека'), ('5','По 5 человек'), ('6','По 6 человек'), ('7','По 7 человек')])

# Действия если запускается именно этот файл
if __name__=='__main__':
	pass