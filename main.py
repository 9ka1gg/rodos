import requests
import os


def command(ip, relay, action):
    address = f'http://{login}:{password}@{ip}/protect/rb{relay}{action}.cgi'
    print(f'Отправляется запрос по адресу {address} ... ', end='')
    try:
        response = requests.get(address)
        print('Успешно. \n')
    except:
        print('Не удалось отправить запрос. \n')


def scenarios_handler():
    while True:
        print('Выберите сценарий:\n\n', end='')
        for scenario_file in os.listdir('scenarios'):
            if '.bat' in scenario_file:
                print(scenario_file.replace('.bat', ''), end=' ')
        selected_scenario = input('\n\nЗагрузить сценарий (-1 для выхода): ')
        if selected_scenario == '-1':
            return 0
        scenario_existing = False
        for existing_scenario in os.listdir('scenarios'):
            if selected_scenario == existing_scenario:
                is_scenario_existing = True
                break
        if not scenario_existing:
            print('Введён несуществующий сценарий. Попробуйте снова.')
            pass
        with open(f'scenarios/{selected_scenario}.bat') as scenario:
            for line in scenario.readlines():
                command(ip=ip, relay=line[0], action=line[1])


def scenarios_editor():
    while True:
        print('\nСоздать сценарий - 0\nРедактировать сценарий - 1\nВыход - -1')
        mode = input('\nВыберите действие: ')
        if mode == '0':
            print('Добро пожаловать в редактор сценариев!')
            scenario_name = input('Выберите название для сценария (-1 для отмены): ')
            if scenario_name == '-1':
                return 0
            for other_scenario_name in os.listdir('scenarios'):
                if scenario_name == other_scenario_name.replace('bat', ''):
                    print('Введено название существующего сценария.\n0 - удалить существующий\n-1 - отмена')
                    del_or_can = input('Действие: ')
                    if del_or_can == '0':
                        os.remove(other_scenario_name)
                        print(f'Сценарий {other_scenario_name} удалён.')
                    elif del_or_can == '-1':
                        pass
            open(f'scenarios/{scenario_name}.bat', '+w').close()
            print('\nНачинайте вводить шаги сценария через абзац.\nдля завершения сценария введите -1.\n')
            while True:
                relay = int(input('Реле (0-15): '))
                if relay == -1:
                    print('Создание сценария завершено. Возвращение в главное меню.')
                    return 0
                action = input('Действие (n - включить, f - выключить, s - импульс): ')
                if action == -1:
                    print('Создание сценария завершено. Возвращение в главное меню.')
                    return 0
                if 0 <= relay <= 15 and action == 'n' or action == 'f' or action == 's':
                    with open(f'scenarios/{scenario_name}.bat', 'a') as new_scenario:
                        new_scenario.write(f'{relay}{action}\n')
        elif mode == '1':
            print('Список сценариев:\n\n', end='')
            for scenario_file in os.listdir('scenarios'):
                if '.bat' in scenario_file:
                    print(scenario_file.replace('.bat', ''), end=' ')
            selected_scenario = input('\n\nРедактировать сценарий (-1 для выхода): ')
            if selected_scenario == '-1':
                return 0
            scenario_existing = False
            for existing_scenario in os.listdir('scenarios'):
                if selected_scenario == existing_scenario:
                    is_scenario_existing = True
                    break
            if not scenario_existing:
                print('Введён несуществующий сценарий. Попробуйте снова.')
                pass
            mode_editing = input('\nИзменить существующие команды - 0\nДополнить сценарий - 1\nВыход - -1\nВыберите действие: ')
            if mode_editing == '0':
                print('В разработке')
                # while True:
                #     with open(f'scenarios/{selected_scenario}.dll') as scenario:
                #         old_data = scenario.read()
                #         line_number = 0
                #         for line in scenario.readlines():
                #             print(f'{line_number}. Реле {line[0]}, Действие {line[1]}')
                #     edit_line = int(input('Выберите номер команды:'))
                #     if edit_line < 0 or edit_line > line_number:
                #         print('Введён несуществующий номер команды.')
                #     new_relay = int(input('Введите новый номер реле (-1 для отмены): '))
                #     if new_relay == '-1':
                #         pass
                #     if 0 > new_relay > 15:
                #         print('Несуществующий номер реле.')
                #         pass
                #     new_action = int(input('Введите новое действие (n/f/s): '))
                #     if new_action == '-1':
                #         pass
                #     if new_action != 'n' or new_action != 'f' or new_action != 's':
                #         print('Несуществующая команда.')
                #         pass
                #     with open(f'scenarios/{selected_scenario}.dll', 'w') as scenario:
                #         pass




def commands_handler():
    while True:
        relay = input('Выберите номер реле от 0 до 15 (-1 для выхода): ')
        if relay == '-1':
            return 0
        action = input('Список возможных действий:\nn - включить\nf - выключить\ns - импульс\nОтмена - -1\nВыберите действие: ')
        if action == '-1':
            return 0
        command(ip=ip, relay=relay, action=action)
ip = input('Введите IP: ')
login = input('Логин: ')
password = input('Пароль: ')


while True:
    print('Главное меню // Выберите функцию:\n\nИспользовать сценарий - 0\nРедактор сценариев - 1\nОбработчик команд - 2\nВыход - -1')
    func = input('\nВыберите функцию: ')
    if func == '0':
        scenarios_handler()
    elif func == '1':
        scenarios_editor()
    elif func == '2':
        commands_handler()
    elif func == '-1':
        break
