Тестовое задание для Backend разработчика (junior)
Описание задания:

    Написать сервис, который принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер, который может обрабатывать запрос до 60 секунд. Затем должен отдавать результат запроса. Считается, что внешний сервер может ответить true или false.

    Данные запроса на сервер и ответ с внешнего сервера должны быть сохранены в БД. Нужно написать АПИ для получения истории всех запросов/истории по кадастровому номеру.

    Сервис должен содержать следующие эндпоинты: "/query" - для получения запроса “/result" - для отправки результата "/ping" - проверка, что сервер запустился “/history” - для получения истории запросов

    Добавить Админку.

    Сервис завернуть в Dockerfile.

    В качестве дополнительного задания. Можно добавить дополнительный сервис, который будет принимать запросы первого сервиса и эмулировать внешний сервер.
