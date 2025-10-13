from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import requests
import os
import subprocess

window = Tk()

window.title('EasyRODOS')
window.geometry('1280x720')


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
    scenario = scenario_widget.get()
    return {'ip': ip, 'login': login, 'password': password, 'scenario': scenario}


def save_data():
    data = get_data()
    with open('data.txt', 'w') as file:
        file.write(f'{data["ip"]}:{data["login"]}:{data["password"]}')
    showinfo('Успех', 'Данные сохранены.')


def load_data():
    with open('data.txt', 'r') as file:
        data = file.read()
        ip, login, password = data.split(':')
        return ip, login, password


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

def impulse_relay0():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 0, 's')

def impulse_relay1():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 1, 's')

def impulse_relay2():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 2, 's')

def impulse_relay3():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 3, 's')


def impulse_relay4():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 4, 's')


def impulse_relay5():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 5, 's')


def impulse_relay6():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 6, 's')


def impulse_relay7():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 7, 's')


def impulse_relay8():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 8, 's')


def impulse_relay9():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 9, 's')


def impulse_relay10():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 10, 's')


def impulse_relay11():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 11, 's')


def impulse_relay12():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 12, 's')


def impulse_relay13():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 13, 's')


def impulse_relay14():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 14, 's')


def impulse_relay15():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], 15, 's')


def select_relay0():
    data = get_data()
    if relay0.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 0, 'n')
    elif relay0.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 0, 'f')

def select_relay1():
    data = get_data()
    if relay1.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 1, 'n')
    elif relay1.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 1, 'f')

def select_relay2():
    data = get_data()
    if relay2.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 2, 'n')
    elif relay2.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 2, 'f')

def select_relay3():
    data = get_data()
    if relay3.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 3, 'n')
    elif relay3.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 3, 'f')

def select_relay4():
    data = get_data()
    if relay4.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 4, 'n')
    elif relay4.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 4, 'f')

def select_relay5():
    data = get_data()
    if relay5.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 5, 'n')
    elif relay5.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 5, 'f')

def select_relay6():
    data = get_data()
    if relay6.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 6, 'n')
    elif relay6.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 6, 'f')

def select_relay7():
    data = get_data()
    if relay7.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 7, 'n')
    elif relay7.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 7, 'f')

def select_relay8():
    data = get_data()
    if relay8.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 8, 'n')
    elif relay8.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 8, 'f')

def select_relay9():
    data = get_data()
    if relay9.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 9, 'n')
    elif relay9.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 9, 'f')

def select_relay10():
    data = get_data()
    if relay10.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 10, 'n')
    elif relay10.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 10, 'f')

def select_relay11():
    data = get_data()
    if relay11.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 11, 'n')
    elif relay11.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 11, 'f')

def select_relay12():
    data = get_data()
    if relay12.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 12, 'n')
    elif relay12.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 12, 'f')

def select_relay13():
    data = get_data()
    if relay13.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 13, 'n')
    elif relay13.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 13, 'f')

def select_relay14():
    data = get_data()
    if relay14.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 14, 'n')
    elif relay14.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 14, 'f')

def select_relay15():
    data = get_data()
    if relay15.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], 15, 'n')
    elif relay15.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], 15, 'f')




title = Label(window, text='EasyRODOS', font=('Calibri Bold', 40))
title.place(relx=0.5, rely=0.05, anchor=CENTER)

text_auth = Label(window, text='Авторизация', font=('Calibri light', 25))
text_auth.place(relx=0.1, rely=0.12, anchor=CENTER)

text_ip = Label(window, text='IP:', font=('calibri light', 15))
text_ip.place(relx=0.1, rely=0.17, anchor=CENTER)
ip_widget = Entry(window, width=25)
ip_widget.place(relx=0.1, rely=0.2, anchor=CENTER)

text_login = Label(window, text='Логин:', font=('calibri light', 15))
text_login.place(relx=0.1, rely=0.25, anchor=CENTER)
login_widget = Entry(window, width=25)
login_widget.place(relx=0.1, rely=0.28, anchor=CENTER)

text_password = Label(window, text='Пароль:', font=('calibri light', 15))
text_password.place(relx=0.1, rely=0.33, anchor=CENTER)
password_widget = Entry(window, width=25)
password_widget.place(relx=0.1, rely=0.36, anchor=CENTER)

button_confirm_auth = Button(window, text='Сохранить данные', command=save_data)
button_confirm_auth.place(relx=0.1, rely=0.41, anchor=CENTER)

text_scenario = Label(window, text='Загрузить сценарий', font=('calibri light', 20))
text_scenario.place(relx=0.8, rely=0.12, anchor=CENTER)

scenario_widget = Combobox(window)
scenario_widget['values'] = (get_scenarios())
scenario_widget.place(relx=0.8, rely=0.19, anchor=CENTER)

button_load_scenario = Button(window, text='Выполнить', command=load_scenario_button)
button_load_scenario.place(relx=0.8, rely=0.25, anchor=CENTER)

text_execute = Label(window, text='Выполнить', font=('calibri light', 20))
text_execute.place(relx=0.5, rely=0.12, anchor=CENTER)


# РЕЛЕ


text_relay0 = Label(window, text='Реле 0:', font=('calibri light', 12))
text_relay0.place(relx=0.44, rely=0.17, anchor=CENTER)
relay0 = IntVar()
# relay0.set(0)
relay0_checkbutton = ttk.Checkbutton(variable=relay0, command=select_relay0)
relay0_checkbutton.place(relx=0.47, rely=0.17, anchor=CENTER)
relay0_button = Button(window, text='↨', command=impulse_relay0)
relay0_button.place(relx=0.485, rely=0.17, anchor=CENTER)

text_relay1 = Label(window, text='Реле 1:', font=('calibri light', 12))
text_relay1.place(relx=0.44, rely=0.20, anchor=CENTER)
relay1 = IntVar()
# relay1.set(0)
relay1_checkbutton = ttk.Checkbutton(variable=relay1, command=select_relay1)
relay1_checkbutton.place(relx=0.47, rely=0.20, anchor=CENTER)
relay1_button = Button(window, text='↨', command=impulse_relay1)
relay1_button.place(relx=0.485, rely=0.20, anchor=CENTER)

text_relay2 = Label(window, text='Реле 2:', font=('calibri light', 12))
text_relay2.place(relx=0.44, rely=0.23, anchor=CENTER)
relay2 = IntVar()
# relay2.set(0)
relay2_checkbutton = ttk.Checkbutton(variable=relay2, command=select_relay2)
relay2_checkbutton.place(relx=0.47, rely=0.23, anchor=CENTER)
relay2_button = Button(window, text='↨', command=impulse_relay2)
relay2_button.place(relx=0.485, rely=0.23, anchor=CENTER)

text_relay3 = Label(window, text='Реле 3:', font=('calibri light', 12))
text_relay3.place(relx=0.44, rely=0.26, anchor=CENTER)
relay3 = IntVar()
# relay3.set(0)
relay3_checkbutton = ttk.Checkbutton(variable=relay3, command=select_relay3)
relay3_checkbutton.place(relx=0.47, rely=0.26, anchor=CENTER)
relay3_button = Button(window, text='↨', command=impulse_relay3)
relay3_button.place(relx=0.485, rely=0.26, anchor=CENTER)

text_relay4 = Label(window, text='Реле 4:', font=('calibri light', 12))
text_relay4.place(relx=0.44, rely=0.29, anchor=CENTER)
relay4 = IntVar()
# relay4.set(0)
relay4_checkbutton = ttk.Checkbutton(variable=relay4, command=select_relay4)
relay4_checkbutton.place(relx=0.47, rely=0.29, anchor=CENTER)
relay4_button = Button(window, text='↨', command=impulse_relay4)
relay4_button.place(relx=0.485, rely=0.29, anchor=CENTER)

text_relay5 = Label(window, text='Реле 5:', font=('calibri light', 12))
text_relay5.place(relx=0.44, rely=0.32, anchor=CENTER)
relay5 = IntVar()
# relay5.set(0)
relay5_checkbutton = ttk.Checkbutton(variable=relay5, command=select_relay5)
relay5_checkbutton.place(relx=0.47, rely=0.32, anchor=CENTER)
relay5_button = Button(window, text='↨', command=impulse_relay5)
relay5_button.place(relx=0.485, rely=0.32, anchor=CENTER)

text_relay6 = Label(window, text='Реле 6:', font=('calibri light', 12))
text_relay6.place(relx=0.44, rely=0.35, anchor=CENTER)
relay6 = IntVar()
# relay6.set(0)
relay6_checkbutton = ttk.Checkbutton(variable=relay6, command=select_relay6)
relay6_checkbutton.place(relx=0.47, rely=0.35, anchor=CENTER)
relay6_button = Button(window, text='↨', command=impulse_relay6)
relay6_button.place(relx=0.485, rely=0.35, anchor=CENTER)

text_relay7 = Label(window, text='Реле 7:', font=('calibri light', 12))
text_relay7.place(relx=0.44, rely=0.38, anchor=CENTER)
relay7 = IntVar()
# relay7.set(0)
relay7_checkbutton = ttk.Checkbutton(variable=relay7, command=select_relay7)
relay7_checkbutton.place(relx=0.47, rely=0.38, anchor=CENTER)
relay7_button = Button(window, text='↨', command=impulse_relay7)
relay7_button.place(relx=0.485, rely=0.38, anchor=CENTER)

text_relay8 = Label(window, text='Реле 8:', font=('calibri light', 12))
text_relay8.place(relx=0.53, rely=0.17, anchor=CENTER)
relay8 = IntVar()
# relay8.set(0)
relay8_checkbutton = ttk.Checkbutton(variable=relay8, command=select_relay8)
relay8_checkbutton.place(relx=0.56, rely=0.17, anchor=CENTER)
relay8_button = Button(window, text='↨', command=impulse_relay8)
relay8_button.place(relx=0.575, rely=0.17, anchor=CENTER)

text_relay9 = Label(window, text='Реле 9:', font=('calibri light', 12))
text_relay9.place(relx=0.53, rely=0.20, anchor=CENTER)
relay9 = IntVar()
# relay9.set(0)
relay9_checkbutton = ttk.Checkbutton(variable=relay9, command=select_relay9)
relay9_checkbutton.place(relx=0.56, rely=0.20, anchor=CENTER)
relay9_button = Button(window, text='↨', command=impulse_relay9)
relay9_button.place(relx=0.575, rely=0.20, anchor=CENTER)

text_relay10 = Label(window, text='Реле 10:', font=('calibri light', 12))
text_relay10.place(relx=0.53, rely=0.23, anchor=CENTER)
relay10 = IntVar()
# relay10.set(0)
relay10_checkbutton = ttk.Checkbutton(variable=relay10, command=select_relay10)
relay10_checkbutton.place(relx=0.56, rely=0.23, anchor=CENTER)
relay10_button = Button(window, text='↨', command=impulse_relay10)
relay10_button.place(relx=0.575, rely=0.23, anchor=CENTER)

text_relay11 = Label(window, text='Реле 11:', font=('calibri light', 12))
text_relay11.place(relx=0.53, rely=0.26, anchor=CENTER)
relay11 = IntVar()
# relay11.set(0)
relay11_checkbutton = ttk.Checkbutton(variable=relay11, command=select_relay11)
relay11_checkbutton.place(relx=0.56, rely=0.26, anchor=CENTER)
relay11_button = Button(window, text='↨', command=impulse_relay11)
relay11_button.place(relx=0.575, rely=0.26, anchor=CENTER)

text_relay12 = Label(window, text='Реле 12:', font=('calibri light', 12))
text_relay12.place(relx=0.53, rely=0.29, anchor=CENTER)
relay12 = IntVar()
# relay12.set(0)
relay12_checkbutton = ttk.Checkbutton(variable=relay12, command=select_relay12)
relay12_checkbutton.place(relx=0.56, rely=0.29, anchor=CENTER)
relay12_button = Button(window, text='↨', command=impulse_relay12)
relay12_button.place(relx=0.575, rely=0.29, anchor=CENTER)

text_relay13 = Label(window, text='Реле 13:', font=('calibri light', 12))
text_relay13.place(relx=0.53, rely=0.32, anchor=CENTER)
relay13 = IntVar()
# relay13.set(0)
relay13_checkbutton = ttk.Checkbutton(variable=relay13, command=select_relay13)
relay13_checkbutton.place(relx=0.56, rely=0.32, anchor=CENTER)
relay13_button = Button(window, text='↨', command=impulse_relay13)
relay13_button.place(relx=0.575, rely=0.32, anchor=CENTER)

text_relay14 = Label(window, text='Реле 14:', font=('calibri light', 12))
text_relay14.place(relx=0.53, rely=0.35, anchor=CENTER)
relay14 = IntVar()
# relay14.set(0)
relay14_checkbutton = ttk.Checkbutton(variable=relay14, command=select_relay14)
relay14_checkbutton.place(relx=0.56, rely=0.35, anchor=CENTER)
relay14_button = Button(window, text='↨', command=impulse_relay14)
relay14_button.place(relx=0.575, rely=0.35, anchor=CENTER)

text_relay15 = Label(window, text='Реле 15:', font=('calibri light', 12))
text_relay15.place(relx=0.53, rely=0.38, anchor=CENTER)
relay15 = IntVar()
# relay15.set(0)
relay15_checkbutton = ttk.Checkbutton(variable=relay15, command=select_relay15)
relay15_checkbutton.place(relx=0.56, rely=0.38, anchor=CENTER)
relay15_button = Button(window, text='↨', command=impulse_relay15)
relay15_button.place(relx=0.575, rely=0.38, anchor=CENTER)

button_open_editor = Button(window, text='открыть Редактор', font=('calibri bold', 30), command=open_editor_button)
button_open_editor.place(relx=0.5, rely=0.75, anchor=CENTER)

try:
    saved_ip, saved_login, saved_password = load_data()
    ip_widget.insert(0, saved_ip)
    login_widget.insert(0, saved_login)
    password_widget.insert(0, saved_password)
except FileNotFoundError:
    pass
except ValueError:
    print('Данные файла data.txt повреждены')



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
