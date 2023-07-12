### Как запустить проект через докер

1.  Подключитесь к удаленному серверу, используя SSH.
    
2. Установите Docker и Docker Compose на удаленный сервер.
    
3.  Скопируйте файл `docker-compose.production.yml` на удаленный сервер.
    
4.  На удаленном сервере перейдите в каталог, содержащий файл `docker-compose.production.yml`.
    
5.  Выполните следующую команду, чтобы запустить контейнеры:
        
    `sudo docker-compose -f docker-compose.production.yml up -d` 
        
6.  Проверьте статус контейнеров с помощью команды:
    
    `sudo docker-compose -f docker-compose.production.yml ps` 
    

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram_backend.git
```

```
cd kittygram_backend
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```