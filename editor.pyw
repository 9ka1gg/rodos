from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk


def new():
    scenario = fd.asksaveasfilename(title='Сохранить сценарий как...', initialdir='scenarios', defaultextension='bat')
    with open(scenario, 'w') as new_file:
        new_file.write('')


def save():
    with open(filename, 'w') as writing_file:
        saving_commands = []
        for saving_ui_command in commands:
            saving_ui_relay, saving_ui_action = saving_ui_command.split(',')
            saving_relay = saving_ui_relay[saving_ui_relay.index('Р'):].replace('Реле ', '')
            saving_action = saving_ui_action.replace(' Действие ', '').replace('OFF', 'f').replace('ON', 'n').replace('IMPULSE', 's')
            saving_command = f'{saving_relay}{saving_action}'
            saving_commands.append(f'{saving_command}\n')
        writing_file.writelines(saving_commands)


def add():
    new_relay = relay_combobox.get()
    new_action = action_combobox.get()
    commands.append(f'{commands.index(commands[-1])+1}. Реле {new_relay}, Действие {new_action}')
    commands_var.set(commands)


def delete():
    selection = commands_listbox.curselection()
    commands_listbox.delete(selection[0])
    commands.pop(selection[0])


def edit():
    selection = commands_listbox.curselection()
    new_relay = relay_combobox.get()
    new_action = action_combobox.get()
    commands_listbox.delete(selection[0])
    commands_listbox.insert(selection[0], f'{selection[0]}. Реле {new_relay}, Действие {new_action}')
    commands[selection[0]] = f'{selection[0]}. Реле {new_relay}, Действие {new_action}'


def open_scenario():
    global filename, commands, commands_var, commands_listbox
    try:
        filename = fd.askopenfile(title='Открыть сценарий', initialdir='scenarios', filetypes=[('BAT Files', '*.bat')])
        filename = filename.name
        ttk.Label(text=filename).grid(row=0, column=0, padx=6, pady=6)
        commands = []
        with open(filename, 'r') as file:
            for n, line in enumerate(file.readlines()):
                command = line.rstrip()
                ui_command = {'relay': command[:-1], 'action': command[-1]}
                commands.append(
                    f'{n}. Реле {ui_command["relay"]}, Действие {ui_command["action"].replace("n", "ON").replace("f", "OFF").replace("s", "IMPULSE")}')
            commands_var = Variable(value=commands)
        commands_listbox = Listbox(listvariable=commands_var, width=30)
        commands_listbox.grid(row=1, column=0)
    except AttributeError:
        pass


window = Tk()

window.title('EasyScenario')
window.geometry('700x250')

file_menu = Menu(tearoff=0)
file_menu.add_command(label='Новый сценарий', command=new)
file_menu.add_separator()
file_menu.add_command(label='Сохранить', command=save)
file_menu.add_command(label='Открыть...', command=open_scenario)

main_menu = Menu()
main_menu.add_cascade(label='Файл', menu=file_menu)

ttk.Button(text="Удалить", command=delete).grid(column=1, row=1, padx=6, pady=6)
ttk.Label(text='Реле').grid(column=0, row=2, padx=6, pady=6)
relay_combobox = ttk.Combobox(width=2, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
relay_combobox.grid(column=1, row=2, padx=6, pady=6)
ttk.Label(text='Действие').grid(column=2, row=2, padx=6, pady=6)
action_combobox = ttk.Combobox(width=8, values=['ON', 'OFF', 'IMPULSE'])
action_combobox.grid(column=3, row=2, padx=6, pady=6)
ttk.Button(text="Изменить", command=edit).grid(column=4, row=2, padx=6, pady=6)
ttk.Button(text="Добавить", command=add).grid(column=5, row=2, padx=6, pady=6)

window.config(menu=main_menu)
window.mainloop()
