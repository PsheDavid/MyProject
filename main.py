
---

# main.py

```python
from flask import Flask, render_template, jsonify, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    # Render the main page
    return render_template('index.html')

@app.route('/about')
def about():
    """
    Новая функция: возвращает информацию о приложении.
    """
    info = {
        'name': 'Simple Flask Web Project',
        'version': '1.0.0',
        'description': 'This endpoint provides project metadata.'
    }
    return jsonify(info)

@app.route('/api/echo', methods=['POST'])
def echo():
    """
    Новая функция: эхо-эндпоинт, возвращает полученные JSON-данные.
    """
    data = request.get_json()
    return jsonify({
        'received': data
    })

if __name__ == '__main__':
    app.run(debug=True)
```python
from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    # Render the main page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)