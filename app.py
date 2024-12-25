from flask import Flask, request, jsonify, render_template_string
import subprocess

app = Flask(__name__)

# HTML-шаблон с улучшенным дизайном
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Compiler</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: white;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 80%;
            max-width: 800px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        textarea {
            width: 100%;
            height: 150px;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
            font-size: 16px;
            font-family: monospace;
            margin-bottom: 20px;
            resize: vertical;
        }
        button {
            display: block;
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .output {
            margin-top: 20px;
            padding: 15px;
            border-radius: 5px;
            background-color: #f1f1f1;
            border: 1px solid #ddd;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        .error {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Python Compiler</h1>
        <form action="/run" method="post">
            <textarea name="code" placeholder="Enter your Python code here..."></textarea>
            <button type="submit">Run Code</button>
        </form>
        {% if result is not none %}
            <div class="output">
                <h3>Output:</h3>
                <pre>{{ result['stdout'] }}</pre>
                {% if result['stderr'] %}
                    <div class="error">
                        <h3>Error:</h3>
                        <pre>{{ result['stderr'] }}</pre>
                    </div>
                {% endif %}
            </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_template, result=None)

@app.route('/run', methods=['POST'])
def run_code():
    code = request.form.get('code')
    try:
        result = subprocess.run(
            ['python3', '-c', code],
            capture_output=True,
            text=True,
            timeout=5
        )
        return render_template_string(html_template, result={
            'stdout': result.stdout,
            'stderr': result.stderr
        })
    except subprocess.TimeoutExpired:
        return render_template_string(html_template, result={
            'stdout': '',
            'stderr': 'Error: Code execution timed out.'
        })
    except Exception as e:
        return render_template_string(html_template, result={
            'stdout': '',
            'stderr': f'Error: {str(e)}'
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
