import pickle
import os

class Contact:
    def __init__ (self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return "Name {0}, \nEmail adress: {1}, \nPhone: {2}".format(self.name, self.email, self.phone)

    def change_name(self, name):
        self.name = name

    def change_email(self, email):
        self.email = email

    def change_phone(self, phone):
        self.phone = phone

def add_contact():
    adress_book_file = open("adress.txt", "rb")
    is_file_empty = os.path.getsize("adress.txt") == 0
    if not is_file_empty:
        list_contact = pickle.load("adress.txt")
    else:
        list_contact = []
    try:
        contact = get_contact_info_from_user()
        adress_book_file = open("adress.txt", "wb")
        list_contact.append(contact)
        pickle.dump(list_contact, adress_book_file)
        print("Контакт добавлен")
    except KeyboardInterrupt:
        print("Контакт не добавлен")
    except EOFError:
        print("Контакт не добавлен, проблема с файлом")
    finally:
        adress_book_file.close()

def get_contact_info_from_user():
    try:
        contact_name = input("Введите имя контакта:\n")
        contact_email = input("Введите email контакта:\n")
        contact_phone = input("Введите телефон контакта:\n")
        contact = Contact(contact_name, contact_email, contact_phone)
        return contact
    except EOFError as e:
        raise e #Contact nod added
    except KeyboardInterrupt as e:
        raise e

def display_contacts():
    adress_book_file = open("adress.txt", "rb")
    is_file_empty = os.path.getsize("adress.txt") == 0
    if not is_file_empty:
        list_contact = pickle.load(adress_book_file)
        for each_contact in list_contact:
            print(each_contact)
    else:
        print("Нет контакта в адресе")
        return
    adress_book_file.close()


def search_contact():
    adress_book_file = open("adress.txt", "rb")
    is_file_empty = os.path.getsize("adress.txt") == 0
    if not is_file_empty:
        search_name = input("Введите имя\n")
        is_contact_found = False
        list_contact = pickle.load(adress_book_file)
        for each_contact in list_contact:
            contact_name = each_contact.name
            search_name = search_name.lower()
            contact_name = contact_name.lower()
            if (contact_name == search_name):
                print(each_contact)
                is_contact_found = True
                break
        if not is_contact_found: # not False == True
            print("Нет соответствующего имени контакта")
    else:
        print("Адресная книга пустая. Нет контакта для поиска")
    adress_book_file.close()

def delete_contact():
    adress_book_file = open("adress.txt", "rb")
    is_file_empty = os.path.getsize("adress.txt") == 0
    if not is_file_empty:
        name = input("Введенное имя было удалено")
        list_contact = pickle.load(adress_book_file)
        is_contact_delete = False
        for i in range(0, len(list_contact)):
            each_contact = list_contact[i]
            if each_contact.name == name:
                del list_contact[i]
                is_contact_deleted = True
                print("Контакт удален")
                adress_book_file = open("adress.txt", "wb")
                if (len(list_contact) == 0):
                    adress_book_file.write(b"")
                else:
                    pickle.dump(list_contact, adress_book_file)
                break
        if not is_contact_deleted:
            print("Нет контакта с таким именем")
    else:
        print("Адресная книга пуста. Нет контактов для удаления")
    adress_book_file.close()

def modify_contact():
    adress_book_file = open("adress.txt", "rb")
    is_file_empty = os.path.getsize("adress.txt") == 0
    if not is_file_empty:
        name = input("Введите имя для изменения\n")
        list_contact = pickle.load(adress_book_file)
        is_contact_modified = False
        for each_contact in list_contact:
            if each_contact.name == name:
                do_modification(each_contact)
                adress_book_file = open("adress.txt", "wb")
                pickle.dump(list_contact, adress_book_file)
                is_contact_modified = True
                print("Контакт был изменен")
                break
        if not is_contact_modified:
            print("Нет контакта с таким именем")
    else:
        print("Адресная книга пуста. Нет контакта для изменения")

def do_modification(contact):
    try:
        while True:
            print("Введите 1 для изменения email\n 2 для изменения адреса\n 3 для изменения имени\n 4 для выхода")
            choise = input()
            if(choise == "1"):
                new_email = input("Пожалуйста, введите новый email: ")
                contact.change_email(new_email)
                break
            elif(choise == "2"):
                new_phone = input("Пожалуйста, введите новый телефон: ")
                contact.change_phone(new_phone)
                break
            elif(choise == "3"):
                new_name = input("Пожалуйста, введите новое имя: ")
                contact.change_name(new_name)
                break
            else:
                print("Неверный выбор")
    except EOFError:
        print("Error by EOFError")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")

print("Введите 'a' для добавления контактов\n Введите 'b' для обзора контактов\n Введите 'd' для удаления контактов\n Введите 'm' для изменения контактов\n Введите 's' для поиска контактов\n Введите 'q' для выхода")
while True:
    choise = input("Введите свой выбор: \n")
    if choise == 'q':
        print("Спасибо за использование приложения")
        break
    elif(choise.lower() == 'b'):
        display_contacts()
    elif (choise.lower() == 'a'):
        add_contact()
    elif(choise.lower()  == 'd'):
        delete_contact()
    elif(choise.lower()  == 'm'):
        modify_contact()
    elif(choise.lower()  == 's'):
        search_contact()
    else:
        print("Невеный выбор")
