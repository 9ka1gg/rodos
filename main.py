import os
import requests
from rich import print
from rich.prompt import Prompt, IntPrompt

class Logger:
    def __init__(self, enabled=False):
        self.enabled = enabled

    def debug(self, msg):
        if self.enabled:
            print(f"[yellow][DEBUG][/]: {msg}")
    def info(self, msg):
        if self.enabled: print(f"[cyan][INFO][/]: {msg}")
    def error(self, msg):
        print(f"[red][ERROR][/]: {msg}")

DEBUG_MODE = False
logger = Logger(DEBUG_MODE)

def parse_flags(raw_input):
    parts = raw_input.strip().split()
    flags = {
        "debug": False,
        "nologin": False,
        "log": "admin",
        "pass": "",
        "ip": "-1"
    }

    for part in parts:
        if part.startswith("-"):
            if part == "-debug":
                flags["debug"] = True
            elif part == "-nologin":
                flags["nologin"] = True
            elif part.startswith("-log="):
                flags["log"] = part.split("=", 1)[1]
            elif part.startswith("-pass="):
                flags["pass"] = part.split("=", 1)[1]
        else:
            flags["ip"] = part  # всё остальное считается IP

    return flags

def input_action():
    action = Prompt.ask("Действие [n/f/s/-1]", choices=["n", "f", "s", "-1"], default="-1")
    logger.debug(f"Введено действие: {action}")
    return action

def input_relay():
    try:
        relay = IntPrompt.ask("Реле (0-15, -1 для выхода)", default=-1)
        logger.debug(f"Введено реле: {relay}")
        return relay
    except Exception as e:
        logger.error(f"Ошибка ввода реле: {e}")
        return -1

def command(ip, relay, action):
    address = f"http://{login}:{password}@{ip}/protect/rb{relay}{action}.cgi"
    logger.info(f"Отправляется запрос: {address}")
    try:
        r = requests.get(address)
        r.raise_for_status()
        print("[green]Успешно[/]")
        logger.debug(f"Ответ сервера: {r.status_code}")
    except Exception as e:
        logger.error(f"Ошибка запроса: {e}")

def list_scenarios():
    scenarios = sorted(f.replace(".bat", "") for f in os.listdir("scenarios") if f.endswith(".bat"))
    logger.debug(f"Найденные сценарии: {scenarios}")
    return scenarios

def load_scenario():
    print("[bold]Сценарии:[/]")
    scenarios = list_scenarios()
    print(" ".join(scenarios))
    name = Prompt.ask("Имя сценария (-1 для выхода)")
    if name == "-1":
        return
    path = f"scenarios/{name}.bat"
    if not os.path.exists(path):
        logger.error("Сценарий не найден")
        return
    with open(path) as f:
        for line in f:
            if len(line) < 2: continue
            command(ip, relay=line[0], action=line[1])

def create_scenario():
    name = Prompt.ask("Название сценария (-1 для отмены)")
    if name == "-1": return
    path = f"scenarios/{name}.bat"
    if os.path.exists(path):
        if Prompt.ask("Файл существует. Перезаписать? [0/-1]", choices=["0", "-1"]) != "0":
            return
        os.remove(path)
    with open(path, 'w') as f:
        print("Добавление шагов. Введите -1 для выхода.")
        while True:
            relay = input_relay()
            if relay == -1: break
            action = input_action()
            if action == "-1": break
            f.write(f"{relay}{action}\n")

def edit_scenario():
    print("[bold]Сценарии:[/]")
    scenarios = list_scenarios()
    print(" ".join(scenarios))
    name = Prompt.ask("Редактируемый сценарий (-1 для выхода)")
    if name == "-1": return
    path = f"scenarios/{name}.bat"
    if not os.path.exists(path):
        logger.error("Сценарий не найден")
        return
    with open(path) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        print(f"{i}: Реле {line[0]}, Действие {line[1]}")
    idx = IntPrompt.ask("Номер команды для редактирования (-1 для выхода)", default=-1)
    if idx == -1 or not (0 <= idx < len(lines)):
        return
    relay = input_relay()
    action = input_action()
    if relay != -1 and action != "-1":
        lines[idx] = f"{relay}{action}\n"
        with open(path, "w") as f:
            f.writelines(lines)
        print("[green]Команда обновлена[/]")

def append_to_scenario():
    print("[bold]Сценарии:[/]")
    scenarios = list_scenarios()
    print(" ".join(scenarios))
    name = Prompt.ask("Добавить в сценарий (-1 для выхода)")
    if name == "-1": return
    path = f"scenarios/{name}.bat"
    if not os.path.exists(path):
        logger.error("Сценарий не найден")
        return
    with open(path, 'a') as f:
        print("Добавление шагов. Введите -1 для выхода.")
        while True:
            relay = input_relay()
            if relay == -1: break
            action = input_action()
            if action == "-1": break
            f.write(f"{relay}{action}\n")

def scenarios_editor():
    while True:
        print("\n[bold]Редактор сценариев:[/]")
        print("0: Создать | 1: Редактировать | 2: Дополнить | -1: Назад")
        mode = Prompt.ask("Выбор", choices=["0", "1", "2", "-1"])
        if mode == "0": create_scenario()
        elif mode == "1": edit_scenario()
        elif mode == "2": append_to_scenario()
        elif mode == "-1": return

def commands_handler():
    while True:
        relay = input_relay()
        if relay == -1: break
        action = input_action()
        if action == "-1": break
        command(ip, relay, action)

def main_menu():
    while True:
        print(f"\n[bold]Меню:[/] ({'не авторизован' if ip == '-1' else f'{login}@{ip}'})")
        if ip == "-1":
            print("1: Редактор сценариев | -1: Выход")
            choices = ["1", "-1"]
        else:
            print("0: Сценарий | 1: Редактор | 2: Команды | -1: Выход")
            choices = ["0", "1", "2", "-1"]
        choice = Prompt.ask("Выбор", choices=choices)
        if choice == "0": load_scenario()
        elif choice == "1": scenarios_editor()
        elif choice == "2": commands_handler()
        elif choice == "-1":
            logger.info("Выход из программы")
            break

# ========== ИНИЦИАЛИЗАЦИЯ ==========

raw_input = Prompt.ask("[bold]Вход[/] Введите IP и флаги (например: 192.168.0.12 -nologin)")

flags = parse_flags(raw_input)
DEBUG_MODE = flags["debug"]
logger.enabled = DEBUG_MODE
ip = flags["ip"]
login = flags["log"]
password = flags["pass"]

if DEBUG_MODE:
    logger.info("DEBUG_MODE включён")
if flags["nologin"]:
    ip = "-1"
    logger.info("Запуск без авторизации")

# Если не указано -nologin и IP задан, но логин или пароль не были переданы
if ip != "-1" and not flags["nologin"]:
    if flags["log"] == "admin":
        login = Prompt.ask("Введите логин (по умолчанию admin)", default="admin")
    if not flags["pass"]:
        password = Prompt.ask("Пароль", password=True)
