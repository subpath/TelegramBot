# TelegramBot
Самый простой способ создания Бота в Телеграм с использованием Google App Engine.

### Инструкция
#####1.Создайте свой уникальный токен. 

Для этого напишите Отцу всех Ботов  https://telegram.me/botfather
![1 step](https://cloud.githubusercontent.com/assets/11722602/13633698/7d23901c-e612-11e5-918b-9c9986f7bae0.PNG)
Выберите `/newbot`

Введите имя вашего Бота

В результате у вас появится свой уникальный токен, a так же адрес вашего Бота, которым можно поделиться с друзьями (`telegram.me/имя-вашего-бота`)

![step1 1](https://cloud.githubusercontent.com/assets/11722602/13633778/ffe2f0ba-e612-11e5-8d16-791731fab9a7.PNG)
Сохраните токен и никому не сообщайте.

#####2.Создайте новый проект в Google App  Engine
https://console.developers.google.com/project
Залогинтесь с вашим Гугл-аккаунтом, или создайте новый, если его нет.
![step 2](https://cloud.githubusercontent.com/assets/11722602/13633866/86060560-e613-11e5-97af-ad440fb4c6ae.PNG)

Создайте новый проект. Введите любое название проекта, на названии вашего Бота это никак не отразится.
![step2 1](https://cloud.githubusercontent.com/assets/11722602/13633901/ca7b7932-e613-11e5-816d-f09d1587022b.PNG)

![step2 2](https://cloud.githubusercontent.com/assets/11722602/13633939/2e2eab8e-e614-11e5-8c2f-258fcc4cb7bd.PNG)


Скопируйте ProjectID

![step 2 3](https://cloud.githubusercontent.com/assets/11722602/13633969/754df966-e614-11e5-838d-0b97ad09242c.PNG)

Более в консоли проекта нам делать нечего. 
#####3.Создание Бота на Python.

Клонируйте данный репозиторий или скачайте ZIP-архив.

Откройте файл app.yalm в любом текством редакторе и измените `application` на имя вашего проекта в Google Engine


![step3 1](https://cloud.githubusercontent.com/assets/11722602/13660682/0ddf8b6a-e6ae-11e5-8f25-2b29f9f517ba.PNG)


Больше в файле app.yalm ничего менять не нужно, сохраните изменения и закройте его.

Откройте файл main.py

![step3 2](https://cloud.githubusercontent.com/assets/11722602/13661093/8d975164-e6b1-11e5-80d0-59f1b7d72d54.PNG)

В данном файле нужно вставить ВАШ_ТОКЕН, полученный при регистрации бота.

Далее вы можете изменить команды Бота, следуя комментариям в файле.

Бот готов! Осталось установить web hook.

#####4.Web Hook и последние шаги

  - Скачайте SDK Google App Engine для Python по ссылке https://cloud.google.com/appengine/downloads и установите.
  - Запустите Google App Engine Launcher
  

![step3 3](https://cloud.githubusercontent.com/assets/11722602/13661161/f588dcb6-e6b1-11e5-9b82-6959fc0f2cee.PNG)


  - В меню кликните `File`, выберете `Add Existing Application` и укажите путь до папки, в которой содержится файл app.yalm и main.py
  - В колонке `Name` имя должно соответствовать названию вашего проекта в Google Engine
  - Кликните `Deploy` и подождите пока файлы загрузятся на сервер
  - В браузере перейдите по ссылки `https://ИМЯ-ВАШЕГО-ПРОЕКТА.appspot.com/me` (Замените `ИМЯ-ВАШЕГО-ПРОЕКТА` на имя вашего проекта в Google Engine). После небольшого ожидание, вы должны увидеть `"ok": true`, если это не так, попробуйте перезагрузить страницу
  - Теперь перейдите по ссылке `https://ИМЯ-ВАШЕГО-ПРОЕКТА.appspot.com/set_webhook?url=https://ИМЯ-ВАШЕГО-ПРОЕКТА.appspot.com/webhook`. Вы должны увидеть `Webhook was set`
  
**Все готово! Вы можете написать вышему боту, найдя его по ссылке `telegram.me/имя-вашего-бота`**

Инструкцию по использованию сторонних модулей можно найти [здесь](https://github.com/subpath/TelegramBot/blob/master/libs/Using%20site-packages.md)

А [здесь](https://github.com/subpath/TelegramBot/tree/master/example) можно найти пример рабочего Телеграм Бота, использующего Вконтаке API

[Оригинал иструкции](https://github.com/yukuku/telebot)
  
