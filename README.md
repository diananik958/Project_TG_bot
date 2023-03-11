# Project_TG_bot

# 1. Цель проекта

Повышение осведомленности сотрудников по теме ???

# 2. Функциональные блоки

Бот должен состоять из следующих функциональных блоков.
- Регистрация сотрудников
- Изучение теории по выбранной теме
- Прохождение теста

## 2.1. Типы пользователей

В системе будет 2 роли пользователей:
- Пользователь
- Владелец

## 2.2. Функционал обычного пользователя

### 2.2.1. Регистрация.

Для регистрации команды пользователю будет необходимо ввести следующие данные в форму регистрации:
1. Корпоративный email

### 2.2.2. Изучение теории по теме.

Выбрать пункт меню "Изучить теорию".

### 2.2.3. Прохождение теста.

Выбрать пункт меню "Пройти тест".

## 2.3. Функционал владельца

Владелец обладает всеми возможностями пользователя.

# 3. Стек технологий

1. Python
2. aiogram
3. MS SQL: таблица Users - поля UserID (bigint), TelegramID (bigint), ChatID (bigint), corp_email (text), created_date (datetime)

# 4. Требование к дизайну

Команды через слэш будут вводиться

# 5. Запуск

```
set BOT_API_KEY=<key>
python3 start.py
```

# 6. Git
```# Если проекта нет
git clone https://github.com/diananik958/Project_TG_bot.git

# Если проект есть и надо запулить изменения (добавить изменения других/обновить проект)
git pull

# Если проект есть и надо запушить изменения (если ты что-то сделал в проекте)
git add .
git commit -m "Сообщение о том что вы сделали"
git push


```
