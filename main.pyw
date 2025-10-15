from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import requests
import os

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
    pass

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