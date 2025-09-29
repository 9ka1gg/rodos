from tkinter import *
from tkinter.ttk import Combobox
import requests
import os
import subprocess

window = Tk()

window.title('EasyRODOS')
window.geometry('600x800')


def execute_command(ip, login, password, relay, action):
    address = f'http://{login}:{password}@{ip}/protect/rb{relay}{action}.cgi'
    print(f'Отправляется запрос по адресу {address} ... ', end='')
    try:
        response = requests.get(address)
        print('Запрос отправлен.\n')
    except Exception as error:
        print(f'Не удалось отправить запрос. {error}\n')


def get_scenarios():
    scenarios = []
    for scenario_file in os.listdir('scenarios'):
        if '.bat' in scenario_file:
            scenarios.append(scenario_file)
    return scenarios


def get_data():
    ip = ip_widget.get()
    login = login_widget.get()
    password = password_widget.get()
    relay = relay_widget.get()
    action = action_widget.get()
    action = action.replace('On', 'n')
    action = action.replace('Off', 'f')
    action = action.replace('Impulse', 's')
    scenario = scenario_widget.get()
    return {'ip': ip, 'login': login, 'password': password, 'relay': relay, 'action': action, 'scenario': scenario}


def authed():
    ip_widget.config(state='disabled')
    login_widget.config(state='disabled')
    password_widget.config(state='disabled')


def load_scenario_button():
    data = get_data()
    with open(f'scenarios/{data["scenario"]}') as scenario:
        for line in scenario.readlines():
            line = line.rstrip()
            execute_command(ip=data['ip'], login=data['login'], password=data['password'], relay=line[:-1], action=line[-1])

def execute_command_button():
    data = get_data()
    print(data)
    execute_command(data['ip'], data['login'], data['password'], data['relay'], data['action'])


def open_editor_button():
    subprocess.run(['python', 'editor.py'])

title = Label(window, text='EasyRODOS', font=('Calibri Bold', 40))
title.place(relx=0.5, rely=0.05, anchor=CENTER)

text_auth = Label(window, text='Авторизация', font=('Calibri light', 25))
text_auth.place(relx=0.5, rely=0.12, anchor=CENTER)

text_ip = Label(window, text='IP:', font=('calibri light', 15))
text_ip.place(relx=0.5, rely=0.17, anchor=CENTER)
ip_widget = Entry(window, width=25)
ip_widget.place(relx=0.5, rely=0.2, anchor=CENTER)

text_login = Label(window, text='Логин:', font=('calibri light', 15))
text_login.place(relx=0.5, rely=0.25, anchor=CENTER)
login_widget = Entry(window, width=25)
login_widget.place(relx=0.5, rely=0.28, anchor=CENTER)

text_password = Label(window, text='Пароль:', font=('calibri light', 15))
text_password.place(relx=0.5, rely=0.33, anchor=CENTER)
password_widget = Entry(window, width=25)
password_widget.place(relx=0.5, rely=0.36, anchor=CENTER)

button_confirm_auth = Button(window, text='Подтвердить', command=authed)
button_confirm_auth.place(relx=0.5, rely=0.41, anchor=CENTER)

text_scenario = Label(window, text='Загрузить сценарий', font=('calibri light', 20))
text_scenario.place(relx=0.20, rely=0.45, anchor=CENTER)

scenario_widget = Combobox(window)
scenario_widget['values'] = (get_scenarios())
scenario_widget.place(relx=0.20, rely=0.5, anchor=CENTER)

button_load_scenario = Button(window, text='Выполнить', command=load_scenario_button)
button_load_scenario.place(relx=0.20, rely=0.59, anchor=CENTER)

text_scenario = Label(window, text='Выполнить', font=('calibri light', 20))
text_scenario.place(relx=0.80, rely=0.45, anchor=CENTER)

text_relays = Label(window, text='Реле:', font=('calibri light', 12))
text_relays.place(relx=0.75, rely=0.5, anchor=CENTER)

relay_widget = Combobox(window, width=7)
relay_widget['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
relay_widget.place(relx=0.86, rely=0.5, anchor=CENTER)

text_actions = Label(window, text='Действие:', font=('calibri light', 12))
text_actions.place(relx=0.73, rely=0.54, anchor=CENTER)

action_widget = Combobox(window, width=7)
action_widget['values'] = ('On', 'Off', 'Impulse')
action_widget.place(relx=0.86, rely=0.54, anchor=CENTER)

button_execute_command = Button(window, text='Выполнить', command=execute_command_button)
button_execute_command.place(relx=0.8, rely=0.59, anchor=CENTER)

button_open_editor = Button(window, text='открыть Редактор', font=('calibri bold', 30), command=open_editor_button)
button_open_editor.place(relx=0.5, rely=0.75, anchor=CENTER)

window.mainloop()



# import os
#
# DEBUG_MODE = False
#
# def debug(debug_text):
#     if DEBUG_MODE:
#         print(f'// DEBUG: {debug_text} //')

#
#
# def scenarios_handler():
#     while True:
#         print('Выберите сценарий:\n\n', end='')
#         for scenario_file in os.listdir('scenarios'):
#             if '.bat' in scenario_file:
#                 print(scenario_file.replace('.bat', ''), end=' ')
#         selected_scenario = input('\n\nЗагрузить сценарий (-1 для выхода): ')
#         if selected_scenario == '-1':
#             return 0
#         scenario_existing = False
#         for existing_scenario in os.listdir('scenarios'):
#             if selected_scenario == existing_scenario.replace('.dll', ''):
#                 is_scenario_existing = True
#                 break
#         if not scenario_existing:
#             print('Введён несуществующий сценарий. Попробуйте снова.')
#             pass
#         with open(f'scenarios/{selected_scenario}.bat') as scenario:
#             for line in scenario.readlines():
#                 line = line.rstrip()
#                 command(ip=ip, relay=line[:-1], action=line[-1])
#
#
# def scenarios_editor():
#     while True:
#         debug('start of the scenarios_editor cycle')
#         print('\nСоздать сценарий - 0\nРедактировать сценарий - 1\nВыход - -1')
#         mode = input('\nВыберите действие: ')
# # создание
#         if mode == '0':
#             print('Добро пожаловать в редактор сценариев!')
#             scenario_name = input('Выберите название для сценария (-1 для отмены): ')
#             if scenario_name == '-1':
#                 return 0
#             for other_scenario_name in os.listdir('scenarios'):
#                 if scenario_name == other_scenario_name.replace('bat', ''):
#                     print('Введено название уже существующего сценария.\n0 - удалить существующий\n-1 - отмена')
#                     del_or_can = input('Действие: ')
#                     if del_or_can == '0':
#                         os.remove(other_scenario_name)
#                         print(f'Сценарий {other_scenario_name} удалён.')
#                     elif del_or_can == '-1':
#                         pass
#             open(f'scenarios/{scenario_name}.bat', '+w').close()
#             print('\nНачинайте вводить шаги сценария через абзац.\nдля завершения сценария введите -1.\n')
#             while True:
#                 relay = int(input('Реле (0-15): '))
#                 if relay == -1:
#                     print('Создание сценария завершено. Возвращение в главное меню.')
#                     return 0
#                 action = input('Действие (n - включить, f - выключить, s - импульс): ')
#                 if action == -1:
#                     print('Создание сценария завершено. Возвращение в главное меню.')
#                     return 0
#                 if 0 <= relay <= 15 and action == 'n' or action == 'f' or action == 's':
#                     with open(f'scenarios/{scenario_name}.bat', 'a') as new_scenario:
#                         new_scenario.write(f'{relay}{action}\n')
# # модификация
#         elif mode == '1':
#             print('Список сценариев:\n\n', end='')
#             for scenario_file in os.listdir('scenarios'):
#                 if '.bat' in scenario_file:
#                     print(scenario_file.replace('.bat', ''), end=' ')
#             selected_scenario = input('\n\nРедактировать сценарий (-1 для выхода): ')
#             if selected_scenario == '-1':
#                 return 0
#             scenario_existing = False
#             for existing_scenario in os.listdir('scenarios'):
#                 if f'{selected_scenario}.bat' == existing_scenario:
#                     scenario_existing = True
#                     break
#             if not scenario_existing:
#                 print('Введён несуществующий сценарий. Попробуйте снова.')
#                 pass
#             mode_editing = input('\nИзменить существующие команды - 0\nДополнить сценарий - 1\nВыход - -1\nВыберите действие: ')
# ## изменение
#             if mode_editing == '0':
#                 while True:
#                     debug('start of the cycle')
#                     with open(f'scenarios/{selected_scenario}.bat', 'r') as scenario:
#                         debug(f'successfully opened file scenarios/{selected_scenario}.bat')
#                         data_list = scenario.readlines()
#                         line_number = 0
#                         for line in data_list:
#                             line = line.strip("''\n")
#                             print(f'{line_number}. Реле {line[:-1]}, Действие {line[-1]}')
#                             line_number += 1
#
#                     try:
#                         edit_line = int(input('Выберите номер команды (-1 для выхода): '))
#                     except ValueError:
#                         print('Ошибка: введите число.')
#                         continue
#
#                     if edit_line == -1:
#                         break
#                     if edit_line < 0 or edit_line >= len(data_list):
#                         print('Введён несуществующий номер команды.')
#                         continue
#
#                     try:
#                         new_relay = int(input('Введите новый номер реле (-1 для отмены): '))
#                     except ValueError:
#                         print('Ошибка: введите число.')
#                         continue
#
#                     if new_relay == -1:
#                         print('Изменение отменено.')
#                         continue
#                     if new_relay < 0 or new_relay > 15:
#                         print('Несуществующий номер реле.')
#                         continue
#
#                     new_action = input('Введите новое действие (n/f/s, -1 для отмены): ').lower()
#                     if new_action == '-1':
#                         print('Изменение отменено.')
#                         continue
#                     if new_action not in ['n', 'f', 's']:
#                         print('Несуществующая команда.')
#                         continue
#
#                     data_list[edit_line] = f"{new_relay}{new_action}\n"
#
#                     with open(f'scenarios/{selected_scenario}.bat', 'w') as scenario:
#                         scenario.writelines(data_list)
#                     print('Команда успешно изменена.\n')
# ## дополнение
#             elif mode_editing == '1':
#                 print('\nНачинайте вводить шаги сценария через абзац.\nдля завершения сценария введите -1.\n')
#                 while True:
#                     print('Список команд:')
#                     with open(f'scenarios/{selected_scenario}.bat', 'r') as scenario:
#                         debug(f'successfully opened file scenarios/{selected_scenario}.bat')
#                         data_list = scenario.readlines()
#                         line_number = 0
#                         for line in data_list:
#                             line = line.strip("''\n")
#                             print(f'{line_number}. Реле {line[:-1]}, Действие {line[-1]}')
#                             line_number += 1
#                     relay = int(input('Реле (0-15): '))
#                     if relay == -1:
#                         print('Создание сценария завершено. Возвращение в главное меню.')
#                         return 0
#                     action = input('Действие (n - включить, f - выключить, s - импульс): ')
#                     if action == -1:
#                         print('Создание сценария завершено. Возвращение в главное меню.')
#                         return 0
#                     if 0 <= relay <= 15 and action == 'n' or action == 'f' or action == 's':
#                         with open(f'scenarios/{selected_scenario}.bat', 'a') as scenario:
#                             scenario.write(f'{relay}{action}\n')
#
#
#
# def commands_handler():
#     while True:
#         debug('commands_handler cycle start')
#         relay = input('Выберите номер реле от 0 до 15 (-1 для выхода): ')
#         debug(f'relay={relay}')
#         if relay == '-1':
#             debug('returning 0')
#             return 0
#         action = input('Список возможных действий:\nn - включить\nf - выключить\ns - импульс\nОтмена - -1\nВыберите действие: ')
#         debug(f'action={action}')
#         if action == '-1':
#             debug('returning 0')
#             return 0
#         debug('using command()')
#         command(ip=ip, relay=relay, action=action)
#
# # начало программы
# ip = input('Вход\nВведите IP (-1 чтобы продолжить без входа): ')
# login = 'admin'
#
# if '/debug' in ip:
#     DEBUG_MODE = True
#     debug('DEBUG_MODE = True')
#     ip = ip.replace('/debug', '')
#
# if ip != '-1':
#     login = input('Логин: ')
#     debug(f'login={login}')
#     password = input('Пароль: ')
#     debug(f'password={password}')
#
#
# while True:
#     debug('цикл запущен')
#     if ip != '-1':
#         print(f'Главное меню // {login} [{ip}]// Выберите функцию:\n\nИспользовать сценарий - 0\nРедактор сценариев - 1\nОбработчик команд - 2\nВыход - -1')
#     else:
#         print(f'Главное меню // [НЕ АВТОРИЗОВАН] // Выберите функцию: \nРедактор сценариев - 1\nВыход - -1')
#     func = input('\nВыберите функцию: ')
#     debug(f'func={func}')
#     if func == '0' and ip != '-1':
#         debug('обработана команда на использование сценария')
#         scenarios_handler()
#     elif func == '1':
#         debug('обработана команда на редактирование сценариев')
#         scenarios_editor()
#     elif func == '2' and ip != '-1':
#         debug('обработана команда на использование команд')
#         commands_handler()
#     elif func == '-1':
#         debug('выход')
#         break
