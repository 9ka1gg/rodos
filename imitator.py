from flask import Flask, abort

app = Flask(__name__)

@app.route('/protect/rb<int:relay><action>.cgi')
def handle_request(relay, action):
    if relay < 0 or relay > 15:
        abort(404)

    if action not in ['n', 'f', 's']:
        abort(404)

    print(f'Реле {relay}: действие {action}')
    return f'ОК: Реле {relay}, действие {action}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
