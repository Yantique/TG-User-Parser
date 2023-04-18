from pyrogram import Client


API_ID = <API_ID>  # Заменить на свой API_ID
API_HASH = '<API_HASH>'  # Заменить на свой API_HASH


def get_chat_ids():
    with client:
        dialogs = client.get_dialogs()

        print("Список чатов:")
        for dialog in dialogs:
            print(f"Название: {dialog.chat.title}; id: {dialog.chat.id}")


def get_members(chat_id):
    with client:
        members = client.get_chat_members(chat_id)
        with open('members.txt', 'w', encoding='utf-8') as f:
            f.write("user_id, username\n")
            for member in members:
                f.write(f"{member.user.id}, @{member.user.username}\n")


if __name__ == '__main__':
    try:
        client = Client('account', api_id=API_ID, api_hash=API_HASH)
        get_chat_ids()
        chat = int(input('Введите id чата: '))
        get_members(chat)
    except:
        print('Что-то пошло не так :(')
