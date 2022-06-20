import time
import json
from get_users import Client
from get_users.errors.exceptions import FloodWait

app = Client('session', workdir='./session')  # Настройки сессии клиента
chat = 'test_group_bot'  # Название чата или его ID
string_format = 'ID: {id} \n'  # Формат строки для записи


def parser(id):
    """ Функция парсинга пользователей """
    members = []
    offset = 0
    limit = 200

    while True:
        try:
            chunk = app.get_chat_members(id, offset)
        except FloodWait as e:
            time.sleep(e.x)
            continue
        if not chunk.chat_members:
            break

        members.extend(chunk.chat_members)
        offset += len(chunk.chat_members)

    return members


def template(data, template):
    """ Функция нормализатора строк """
    data = json.loads(str(data))
    data['user'].setdefault('first_name', '-')
    data['user'].setdefault('last_name', '-')
    data['user'].setdefault('username', '-')
    data['user'].setdefault('phone_number', '-')
    return template.format(id=data['user']['id'],
                           first_name=data['user']['first_name'],
                           last_name=data['user']['last_name'],
                           username=data['user']['username'],
                           phone_number=data['user']['phone_number'],
                           status=data['status'])


def wfile(data, template_format, path):
    """ Функция записи строк в файл """
    with open(path, 'w', encoding='utf8') as file:
        file.writelines('Количество пользователей: {0}\n\n'.format(len(data)))
        file.writelines([template(user, template_format) for user in data])


def main():
    with app:
        data = parser(chat)
        wfile(data, string_format, './chats/{0}.txt'.format(chat))
        print('Сбор данных закончен!')


if __name__ == '__main__':
    main()
