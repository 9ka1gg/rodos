import requests


def command(ip, action, relay):
    address = f'http://{login}:{password}@{ip}/protect/rb{relay}{action}.cgi'
    print('Отправляется запрос по адресу:', address)
    response = requests.get(address)
    print('Успешно отправлен запрос по адресу:', address)


ip = input('Введите IP: ')
login = input('Логин: ')
password = input('Пароль: ')
while True:
    relay = input('Выберите реле: ')
    action = input('Выберите действие (n/f/s): ')
    command(ip, action, relay)