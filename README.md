Лабораторная работа #4

3.1 Задание: 
Нужно реализовать веб-приложение на тему: 
Блог, в котором есть следующие возможности:
- просмотр ленты
- управление (CRUD) сообщениями, 
- комментарии к сообщениям
- комментарии к комментариям
- возможность добавить произвольное число тегов к одному сообщению блога
- управление (CRUD) списком тегов.
Технологии, которые нужно использовать: 
- фреймворк Django
- ХД mysql

3.2 Деплой инструкция под ubuntu

git clone https://github.com/ratm92/web.git
cd web
sudo apt-get install python-virtualenv
virtualenv env
source env/bin/activate 
sudo apt-get install build-essential python-dev libmysqlclient-dev
sudo apt-get install mysql-server mysql-client
_______________________________________________
Работа с БД:
mysql -uroot -p
CREATE USER 'bloguser'@'%' IDENTIFIED BY 'blog';


CREATE DATABASE blog_db;
USE blog_db;

GRANT ALL ON blog_db.* TO 'bloguser'@'%';
_______________________________________________

pip install mysql
pip install mysql-python
pip install django
sudo apt-get install python-mysqldb

cd myblog
python manage.py syncdb
python manage.py runserver


	


