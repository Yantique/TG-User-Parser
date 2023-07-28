from pyrogram import Client
from time import sleep
from tqdm import tqdm


API_ID = <API_ID>  # Заменить на свой API_ID
API_HASH = '<API_HASH>'  # Заменить на свой API_HASH


def get_chat_ids():
    with client:
        dialogs = client.get_dialogs()
        dialogs_list = []
        for dialog in dialogs:
            dialogs_list.append((dialog.chat.title, dialog.chat.id))
        return dialogs_list


def get_members(chat):
    chat_name, chat_id = chat
    if chat_name is not None:
        with client:
            members = client.get_chat_members(chat_id)
            with open('members.txt', 'a', encoding='utf-8') as f:
                f.write(f"{chat_name}\n")
                n = 1
                for member in members:
                    if member.user.username is not None:
                        f.write(f"{n}. @{member.user.username}\n")
                        n += 1
        sleep(30)  # Изменить если возникает ошибка в методе channels.GetParticipants


if __name__ == '__main__':
    try:
        client = Client('account', api_id=API_ID, api_hash=API_HASH)
        chats = get_chat_ids()
        with open('members.txt', 'w', encoding='utf-8') as f:
            pass
        for chat in tqdm(chats):
            get_members(chat)
    except Exception as ex:
        print('Что-то пошло не так :(')
        print(ex)
