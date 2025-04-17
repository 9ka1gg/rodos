import requests


def command(ip, action, relay):
    response = requests.get(f'http://{ip}/protect/rb{relay}{action}.cgi')
    print(f'отправлен запрос по адресу: http://{ip}/protect/rb{relay}{action}.cgi')

ip = 'localhost'
# ip = input('Введите IP: ')
# login = input('Логин: ')
# password = input('Пароль: ')
while True:
    relay = input('Выберите реле: ')
    action = input('Выберите действие (n/f/s): ')
    command(ip, action, relay)