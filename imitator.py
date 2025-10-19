from flask import Flask, abort
from datetime import datetime
import threading
import time

app = Flask(__name__)

# Храним состояние реле (0 - выкл, 1 - вкл)
relay_states = {i: 0 for i in range(16)}


def reset_relay_after_delay(relay, delay=2):
    """Сбрасывает реле через указанное время"""
    time.sleep(delay)
    relay_states[relay] = 0
    print(f'[{datetime.now().strftime("%H:%M:%S")}] Реле {relay}: автосброс после импульса')


@app.route('/protect/rb<int:relay><action>.cgi')
def handle_request(relay, action):
    if relay < 0 or relay > 15:
        abort(400)

    if action not in ['n', 'f', 's']:
        abort(400)

    # Обновляем состояние реле
    if action == 'n':  # Включить
        relay_states[relay] = 1
    elif action == 'f':  # Выключить
        relay_states[relay] = 0
    elif action == 's':  # Импульс (включаем на 2 секунды)
        relay_states[relay] = 1
        # Запускаем поток для автоматического выключения через 2 секунды
        thread = threading.Thread(target=reset_relay_after_delay, args=(relay, 2))
        thread.daemon = True
        thread.start()

    action_text = action.replace("n", "включить (ON)").replace("f", "выключить (OFF)").replace("s", "импульс (IMPULSE)")
    print(f'[{datetime.now().strftime("%H:%M:%S")}] Реле {relay}: {action_text} -> состояние: {relay_states[relay]}')

    return f'ОК: Реле {relay}, действие {action_text}'


@app.route('/pstat.xml')
def get_relay_status():
    """Возвращает статус всех реле в XML формате"""
    xml_content = '<response>'
    for i in range(16):
        xml_content += f'<rl{i}string>{relay_states[i]}</rl{i}string>'
    xml_content += '</response>'

    return xml_content, 200, {'Content-Type': 'application/xml'}


@app.route('/')
def index():
    """Простая страница для проверки работы сервера"""
    status = "<br>".join([f"Реле {i}: {'ВКЛ (1)' if relay_states[i] else 'ВЫКЛ (0)'}" for i in range(16)])
    return f"""
    <h1>Имитатор сервера реле</h1>
    <p>Состояние реле:</p>
    <p>{status}</p>
    <p><a href="/pstat.xml">Просмотреть статус в XML</a></p>
    <p><em>Импульсные реле автоматически сбрасываются через 2 секунды</em></p>
    """


if __name__ == '__main__':
    print("Сервер запущен! Доступные endpoints:")
    print("- http://localhost/pstat.xml - статус реле в XML")
    print("- http://localhost/protect/rb0n.cgi - управление реле")
    print("- http://localhost/ - веб-интерфейс")
    print("- Импульсные реле (s) автоматически сбрасываются через 2 секунды")
    app.run(host='0.0.0.0', port=80)