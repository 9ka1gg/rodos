from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
import subprocess
import sys
import requests
import os
import time


TIMEOUT = 0.5


window = Tk()

window.title('EasyRODOS')
window.geometry('1280x720')


def execute_command(input_ip, input_login, input_password, input_relay, input_action):
    address = f'http://{input_login}:{input_password}@{input_ip}/protect/rb{input_relay}{input_action}.cgi'
    print(f'Отправляется запрос по адресу {address} ... ', end='')
    try:
        requests.get(address, timeout=TIMEOUT)
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
    return {'ip': ip, 'login': login, 'password': password}


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
    filename = fd.askopenfilename(title='Сохранить сценарий как...', initialdir='scenarios', defaultextension='bat')
    with open(filename) as scenario:
        for line in scenario.readlines():
            line = line.rstrip()
            if line[-1] == 'w':
                time.sleep(float(line[:-1]))

            else:
                execute_command(data['ip'], data['login'], data['password'], line[:-1], line[-1])


def execute_command_button():
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], data['relay'], data['action'])


def open_editor_button():
    subprocess.run([sys.executable, 'editor.pyw'])

def impulse_relay(selected_relay):
    data = get_data()
    execute_command(data['ip'], data['login'], data['password'], selected_relay, 's')


def select_relay(relay_number):
    data = get_data()
    relay_var = globals()[f'relay{relay_number}']
    if relay_var.get() == 1:
        execute_command(data['ip'], data['login'], data['password'], relay_number, 'n')
    elif relay_var.get() == 0:
        execute_command(data['ip'], data['login'], data['password'], relay_number, 'f')




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

button_load_scenario = Button(window, text='Выполнить сценарий...', command=load_scenario_button)
button_load_scenario.place(relx=0.8, rely=0.25, anchor=CENTER)

text_execute = Label(window, text='Выполнить', font=('calibri light', 20))
text_execute.place(relx=0.5, rely=0.12, anchor=CENTER)

for n in range(16):
    position_x = 0.44+(0.09*(n//8))
    position_y = 0.17+float(f'0.0{n%8}')*3
    text_relay = f'text_relay{n}'
    checkbutton_relay = f'relay{n}_checkbutton'
    button_relay = f'relay{n}_button'
    relay= f'relay{n}'
    widgets = globals()
    widgets[text_relay] = Label(window, text=f'Реле {n}:', font=('calibri light', 12))
    widgets[text_relay].place(relx=position_x, rely=position_y, anchor=CENTER)
    widgets[relay] = IntVar()
    widgets[checkbutton_relay] = ttk.Checkbutton(variable=widgets[relay], command=lambda current_n=n: select_relay(current_n))
    widgets[checkbutton_relay].place(relx=position_x+0.03, rely=position_y, anchor=CENTER)
    widgets[button_relay] = Button(window, text='↨', command=lambda current_n=n: impulse_relay(current_n))
    widgets[button_relay].place(relx=position_x+0.045, rely=position_y, anchor=CENTER)

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