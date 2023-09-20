# Задача 38: Отлично в одного человека надо сделать консольное приложение Телефонный справочник с внешним хранилищем информации, 
# и чтоб был реализован основной функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.
# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных
# для отлично в группах надо выполнить или ТГ бот или ГУИ (это когда кнопочки и поля ввода как в Виндовс приложениях) или БД
# ГУИ можно сделать просто на EasyGUI или Tkinter

import csv
import os
import easygui
import sys

def load_contacts():
    contacts = []
    if os.path.exists("contacts.csv"):
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
    return contacts

def save_contacts(contacts):
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def add_contact():
    msg = "Введите данные контакта"
    title = "Добавление контакта"
    fieldNames = ["Имя", "Номер телефона", "e-mail"]
    fieldValues = easygui.multenterbox(msg, title, fieldNames)
    if fieldValues is None:
        sys.exit(0)

    while 1:
        errmsg = ""
        for i, name in enumerate(fieldNames):
            if fieldValues[i].strip() == "":
                errmsg += "{} необходимое поле.\n\n".format(name)
        if errmsg == "":
            name = fieldValues[0]
            phone = fieldValues[1]
            email = fieldValues[2]
            break
    
    contacts.append([name, phone, email])
    save_contacts(contacts)
    msg="Контакт успешно добавлен"
    title = "Добавление контакта"
    easygui.msgbox(msg, title)
    main_menu

def view_contacts():
    if len(contacts) > 0:
        for contact in contacts:
            print(f"Имя: {contact[0]}\nТелефон: {contact[1]}\nEmail: {contact[2]}\n")
    else:
        msg="Список контактов пуст"
        title = "Просмотр контактов"
        easygui.msgbox(msg, title)
        main_menu

def search_contact():
    search_term = input("Введите имя или фамилию для поиска: ")
    
    filtered_contacts = [contact for contact in contacts if search_term in contact[0]]
    
    if len(filtered_contacts) > 0:
        for contact in filtered_contacts:
            print(f"Имя: {contact[0]}\nТелефон: {contact[1]}\nEmail: {contact[2]}\n")
    else:
        msg="Контакт не найден"
        title = "Поиск контактов"
        easygui.msgbox(msg, title)
        main_menu

def update_contact():
    search_term = input("Введите имя или фамилию контакта для изменения: ")
    
    filtered_contacts = [contact for contact in contacts if search_term in contact[0]]
    
    if len(filtered_contacts) > 0:
        for contact in filtered_contacts:
            print(f"Имя: {contact[0]}\nТелефон: {contact[1]}\nEmail: {contact[2]}\n")
        
        idx = int(input("Введите номер контакта, который вы хотите изменить: ")) - 1
        
        name = input("Введите новое имя: ")
        phone = input("Введите новый номер телефона: ")
        email = input("Введите новый адрес электронной почты: ")
        
        contacts[idx] = [name, phone, email]
        save_contacts(contacts)
        msg="Контакт успешно обновлен"
        title = "Изменение контактов"
        easygui.msgbox(msg, title)
        main_menu
    else:
        msg="Контакт не найден"
        title = "Изменение контактов"
        easygui.msgbox(msg, title)
        main_menu

def delete_contact():
    search_term = input("Введите имя или фамилию контакта для удаления: ")
    
    filtered_contacts = [contact for contact in contacts if search_term in contact[0]]
    
    if len(filtered_contacts) > 0:
        for contact in filtered_contacts:
            print(f"Имя: {contact[0]}\nТелефон: {contact[1]}\nEmail: {contact[2]}\n")
        
        idx = int(input("Введите номер контакта, который вы хотите удалить: ")) - 1
    
        contacts.pop(idx)
        save_contacts(contacts)
        msg="Контакт успешно удален"
        title = "Удаление контактов"
        easygui.msgbox(msg, title)
        main_menu
    else:
        msg="Контакт не найден"
        title = "Удаление контактов"
        easygui.msgbox(msg, title)
        main_menu

def main_menu():
    msg ="Выберете действие:"
    title = "Телефонный справочник"
    choices = ["Просмотреть контакты", "Добавить контакт", "Искать контакт", "Изменить контакт", "Удалить контакт", "Выход" ]
    choice = easygui.indexbox(msg, title, choices)
    
    if choice == 0:
        view_contacts()
    elif choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        update_contact()
    elif choice == 4:
        delete_contact()
    else:
        sys.exit(0)

contacts = load_contacts()

while True:
    main_menu()    
    