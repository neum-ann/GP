#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Подключение бд
from app import db

# Таблица пользователей
class User(db.Model):
	__tablename__='User'
	id=db.Column(db.Integer, primary_key=True)
	password=db.Column(db.String(64))
	email=db.Column(db.String(64))
	login=db.Column(db.String(64))
	surname=db.Column(db.String(64))
	name=db.Column(db.String(64))
	middle_name=db.Column(db.String(64))
	role=db.Column(db.String(64))
	result=db.Column(db.String(64))

	def __repr__(self):
		return '<User %r>' % (self.login)

# Таблица для хранения теста
class Test(db.Model):
	__tablename__='Test'
	id=db.Column(db.Integer, primary_key=True)
	question_A=db.Column(db.String(64))
	question_B=db.Column(db.String(64))

	def __repr__(self):
		return '<Test %r>' % (self.id)

# Таблица для хранения результатов тестирования
class Results(db.Model):
	__tablename__='Results'
	id=db.Column(db.Integer, primary_key=True)
	id_user=db.Column(db.Integer)
	count_sopernichestvo=db.Column(db.String(64))
	count_sotrudnichestvo=db.Column(db.String(64))
	count_kompromis=db.Column(db.String(64))
	count_izbeganie=db.Column(db.String(64))
	count_prispososoblenie=db.Column(db.String(64))
	more_count=db.Column(db.String(64))
	delete=db.Column(db.String(64))
	data=db.Column(db.String(64))
	time=db.Column(db.Integer)

	def __repr__(self):
		return '<Results %r>' % (self.id)

# Таблица для групп
class Group(db.Model):
	__tablename__='Group'
	id=db.Column(db.Integer, primary_key=True)
	person_1=db.Column(db.String(64))
	person_2=db.Column(db.String(64))
	person_3=db.Column(db.String(64))
	person_4=db.Column(db.String(64))
	person_5=db.Column(db.String(64))
	person_6=db.Column(db.String(64))
	person_7=db.Column(db.String(64))

	def __repr__(self):
		return '<Group %r>' % (self.id)

# Действия если запускается именно этот файл
if __name__=='__main__':
	pass