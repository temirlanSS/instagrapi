from instagrapi import Client
from decouple import config

INSTAGRAM_TOKEN = config('INSTAGRAM_TOKEN', default='')

# Создаем объект сессии для взаимодействия с Instagram
client = Client()

# Вход в аккаунт
client.login(username='bboostt123', password='Bishkek312')

# Проверяем успешность авторизации
if client.is_authenticated:
    print("Авторизация успешна!")
else:
    print("Авторизация не удалась.")

# Получаем список диалогов (чатов) в директе
dialogs = client.direct_v2.get_inbox()

# Выводим список диалогов
for dialog in dialogs:
    user_id = dialog['users'][0]['pk']  # ID пользователя, отправившего сообщение
    messages = dialog['last_permanent_item']['text']  # Последние сообщения в диалоге

    print(f"Диалог с пользователем {user_id}")
    for message in messages:
        if message['item_type'] == 'text':
            received_message = message['text']
            print(f"Получено сообщение: {received_message}")

            if received_message.lower() == 'hello':
                response = 'hi'
                client.direct_v2.send_text(user_ids=[user_id], text=response)
                print(f"Отправлен ответ '{response}' на сообщение '{received_message}'")

try:
    dialogs = client.direct_v2.get_inbox()
    # Ваш код для обработки диалогов
except Exception as e:
    print("Произошла ошибка:", str(e))
