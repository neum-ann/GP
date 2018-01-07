#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

basedir=os.path.abspath(os.path.dirname(__file__))
CSRF_ENABLED=True
SECRET_KEY='321519'    
SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO=os.path.join(basedir, 'db_repository')

# Действия если запускается именно этот файл
if __name__=='__main__':
	pass