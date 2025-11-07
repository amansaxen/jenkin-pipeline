from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            text-align: center;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        h1 { font-size: 3rem; margin: 0; }
        p { font-size: 1.2rem; margin-top: 1rem; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello World! 🌍</h1>
        <p>Deployed via Jenkins Pipeline</p>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
