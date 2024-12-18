from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# JDoodle API credentials
CLIENT_ID = "ed53ccfb58f971016c5400e717529ba7"
CLIENT_SECRET = "cc6cde90c58d81626e26471533b5a95860d354589e0287dee10babf24e3ef401"
JDoodle_URL = "https://api.jdoodle.com/v1/execute"

@app.route('/execute', methods=['POST'])
def execute_code():
    try:
        # Получаем данные из запроса
        data = request.json
        code = data.get("code", "")
        language = "python3"
        version_index = "3"

        # Формируем тело запроса к JDoodle API
        jdoodle_payload = {
            "clientId": CLIENT_ID,
            "clientSecret": CLIENT_SECRET,
            "script": code,
            "language": language,
            "versionIndex": version_index
        }

        # Отправляем запрос на JDoodle API
        response = requests.post(JDoodle_URL, json=jdoodle_payload)
        return jsonify(response.json())  # Возвращаем результат
    except Exception as e:
        return jsonify({"error": str(e)})  # Возвращаем ошибку, если она есть

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Запуск сервера