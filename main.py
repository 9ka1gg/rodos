import requests
import os


def command(ip, relay, action):
    address = f'http://{login}:{password}@{ip}/protect/rb{relay}{action}.cgi'
    print(f'Отправляется запрос по адресу {address} ... ', end='')
    response = requests.get(address)
    print('Успешно. \n')


ip = input('Введите IP: ')
login = input('Логин: ')
password = input('Пароль: ')


use_scenario = input('Использовать сценарий? (y/n): ')
if use_scenario == 'y':
    print('Выберите сценарий:\n\n', end='')
    for scenario_file in os.listdir('scenarios'):
        if '.dll' in scenario_file:
            print(scenario_file.replace('.dll', ''), end=' ')
    selected_scenario = input('\n\nЗагрузить сценарий: ')
    with open(f'scenarios/{selected_scenario}.dll') as scenario:
        for line in scenario.readlines():
            command(ip=ip, relay=line[0], action=line[1])
while True:
    relay = input('Выберите реле: ')
    action = input('Выберите действие (n/f/s): ')
    command(ip=ip, relay=relay, action=action)