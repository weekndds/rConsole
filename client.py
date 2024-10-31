from flask import Flask, request, jsonify
import threading
import logging
import os, re

app = Flask(__name__)

colorCodes = {
    "BLACK": "\033[30m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",
    "LIGHT_GRAY": "\033[37m",
    "DARK_GRAY": "\033[90m",
    "LIGHT_RED": "\033[91m",
    "LIGHT_GREEN": "\033[92m",
    "LIGHT_YELLOW": "\033[93m",
    "LIGHT_BLUE": "\033[94m",
    "LIGHT_MAGENTA": "\033[95m",
    "LIGHT_CYAN": "\033[96m",
    "RESET": "\033[0m"
}

def parseMessage(message):
    colorMatch = re.search(r"@@(\w+)@@", message)
    if colorMatch:
        color = colorMatch.group(1).upper()
        colorCode = colorCodes.get(color, colorCodes["WHITE"])
        message = message.replace(f"@@{color}@@", "")
        return f"{colorCode}{message}{colorCodes['RESET']}"
    return message

@app.route('/rconsoleprint', methods=['POST'])
def rconsolePrint():
    message = request.json.get('message', '')
    print(parseMessage(message))
    return jsonify(success=True)

@app.route('/rconsoleclear', methods=['POST'])
def rconsoleClear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return jsonify(success=True)

@app.route('/rconsolename', methods=['POST'])
def rconsoleName():
    title = request.json.get('title', 'Console')
    os.system(f'title {title}' if os.name == 'nt' else f'echo -ne "\033]0;{title}\007"')
    return jsonify(success=True)

@app.route('/rconsoleinfo', methods=['POST'])
def rconsoleInfo():
    message = request.json.get('message', '')
    print(parseMessage(f"@@CYAN@@[INFO] {message}"))
    return jsonify(success=True)

@app.route('/rconsolewarn', methods=['POST'])
def rconsoleWarn():
    message = request.json.get('message', '')
    print(parseMessage(f"@@YELLOW@@[WARN] {message}"))
    return jsonify(success=True)

@app.route('/rconsoleerr', methods=['POST'])
def rconsoleErr():
    message = request.json.get('message', '')
    print(parseMessage(f"@@RED@@[ERROR] {message}"))
    return jsonify(success=True)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def runFlask():
    app.run(port=5000)

if __name__ == '__main__':
    threading.Thread(target=runFlask).start()
    os.system('cls'); os.system('title Console')
