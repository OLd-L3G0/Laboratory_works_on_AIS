# Laboratory_works_on_AIS
Лабораторные работы по Прикладным информационным системам, выполнил студен группы УБСТ2301 Анисимов Олег

Работы были выполнены в среде PyCharm, версия Python 3.10. В папке "lab1" находится две чати работ. 
В "lab1.1" первая чать первой лабораторной работы, а в "newProjects" вторая.

Использованные команды
ЛР 1
-------------------------------------------------------
py -m django startproject newProject

py manage.py runserver

py manage.py migrate

pu manage.py makemigrations

py manage.py createsuperuser

-------------------------------------------------------

ЛР 2 
-------------------------------------------------------
py -m django startproject firstwebpage 

py manage.py startapp flatpages

-------------------------------------------------------

ЛР 3 - ЛР 4
-------------------------------------------------------
py -m django startproject blog

py manage.py startapp articles

Пример запросов
SELECT * FROM articles_article

UPDATE articles_article SET text = 'Изменённый текст через sqlite' WHERE id = 1;
UPDATE articles_article SET title = 'Новое название через sqlite' WHERE id = 2;

INSERT INTO articles_article (title, author_id, text, created_date)
VALUES ('Заголовок', 1, 'Текст', '2025-10-07');

-------------------------------------------------------
