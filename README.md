Установка необходимых инструментов
Запустите виртуальную машину с Ubuntu в VirtualBox.
Обновите систему:
bash

sudo apt update && sudo apt upgrade -y
Установите Python и pip, если они не установлены:
bash

sudo apt install python3 python3-pip -y
Установите виртуальное окружение:
bash

sudo apt install python3-venv -y
Установите Flask (фреймворк для создания веб-приложений):
bash

pip3 install flask
Шаг 2. Создание проекта
Создайте директорию для проекта:
bash

mkdir python_compiler && cd python_compiler
Создайте виртуальное окружение:
bash

python3 -m venv venv
source venv/bin/activate
Установите Flask в виртуальном окружении:
bash

pip install flask
Создайте файл app.py с содержимым

Запуск приложения
Активируйте виртуальное окружение, если оно не активно:

source venv/bin/activate
Запустите приложение:

python app.py
Шаг 5. Доступ к сайту
Узнайте IP-адрес виртуальной машины:

ip addr show
Откройте браузер на хостовой машине и введите:
arduino

http://<IP-адрес>:5000
Шаг 6. (Опционально) Настройка автоматического запуска
Для запуска приложения как сервиса:

Создайте файл сервиса:

sudo nano /etc/systemd/system/python_compiler.service
Добавьте содержимое:

[Unit]
Description=Python Compiler Flask App
After=network.target

[Service]
User=<ваш_пользователь>
WorkingDirectory=/path/to/python_compiler
ExecStart=/path/to/python_compiler/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
Активируйте и запустите сервис:


sudo systemctl daemon-reload
sudo systemctl enable python_compiler
sudo systemctl start python_compiler
 
