Виноградов Анатолий  


Тестовое задание № 4:  [Тестовое задание Python асинхрон.pdf](https://github.com/user-attachments/files/16146618/Python.pdf)  

БД - MySQL, фреймворк FastApi, ORM - SQLAlchemy

Проект представляет из себя сервис, который принимает и отвечает на http запросы. Имеется база данных, хранящая информацию о городах, улицах городов и магазинах, находящихся на этих улицах. Сервис реализует несколько запросов: вывод списка всех городов, вывод улиц города по id города, и вывод магазинов по фильтруемым параметрам.

Замечание: название shop заменено на station (чтобы было отличие в задании по практике для университета). Синтаксис  http запросов не изменен, как в задании.
Проект состоит из нескольких файлов:
  1. main - запуск приложения и описание запросов.
  2. requirements - для установки необходимых библиотек.
  3. data(optional) - SQL код для заполнения пустых таблиц в БД. (Пояснение в разделе запуск).
  4. папка database - в ней происходит подключение к БД, описание таблиц и методов для выполнения запросов:
     1) __init__ - описывается класс Database, в котором подключаемся к MySQL и от которого будут наследоваться таблицы
     2) city, street, station - описание таблиц и их методов
     3) models - для класса NewStation, чтобы удобно было делать создание нового магазина.

  __Запуск:__
1. Для запуска и корректной работы необходимо войти в MySQL под пользователем root, создать там базу данных serv (CREATE DATABASE serv;).
2. В проекте в файлу "__ init__.py" в конструкторе необходимо вставить свой пароль от аккаунта root в БД и поменять название своей базы (если есть необходимость использовать другую, а не создавать serv).
3. Если таблиц city, street, station не существует, то после первого запуска проекта они автоматически создадутся (но будут пустыми).
   1) Чтобы облегчить процесс заполнения БД тестовыми данными, в проекте есть файл data(optional).txt, в котором содержаться SQL команды, которые заполнят пустые таблицы. Эти команды надо скопировать и запустить в MySQL.
4. После настройки и заполнения БД, еще раз запускаем проект и готово. Тестирование лучше проводить через [http://127.0.0.1:8001/docs], так как там сразу отображаются все запросы, да и просто удобно работать.
  
