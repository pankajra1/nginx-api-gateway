from flask import Flask, render_template_string, jsonify, request

app = Flask(__name__)

# HTML template with embedded CSS
template = """
<!DOCTYPE html>
<html>
<head>
    <title>API 1 Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
            color: #ff00ff;
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            background: rgba(100, 100, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            background: linear-gradient(90deg, #00ff88, #00ffcc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .status-card {
            background: rgba(0, 0, 255, 0.05);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
        }

        .status {
            display: inline-block;
            padding: 8px 15px;
            background: #00ff88;
            color: #1a1a1a;
            border-radius: 20px;
            font-weight: bold;
            margin-top: 10px;
        }

        .endpoints {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }

        .endpoint-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .endpoint-card h3 {
            color: #00ff88;
            margin-bottom: 10px;
        }

        .method {
            display: inline-block;
            padding: 5px 10px;
            background: #2196F3;
            border-radius: 5px;
            font-size: 0.9em;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>API 1 Dashboard</h1>
            <p>Welcome to the next generation API interface</p>
        </div>

        <div class="status-card">
            <h2>API Status</h2>
            <div class="status">ONLINE</div>
        </div>

        <div class="endpoints">
            <div class="endpoint-card">
                <span class="method">GET</span>
                <h3>Root Endpoint</h3>
                <p>Base URL: /</p>
                <p>Returns welcome message</p>
            </div>
            
            <div class="endpoint-card">
                <span class="method">GET</span>
                <h3>Health Check</h3>
                <p>Base URL: /health</p>
                <p>Returns API health status</p>
            </div>

            <div class="endpoint-card">
                <span class="method">GET</span>
                <h3>Documentation</h3>
                <p>Base URL: /docs</p>
                <p>API documentation and usage guide</p>
            </div>

            <div class="endpoint-card">
                <span class="method">GET</span>
                <h3>Products API</h3>
                <p>Base URL: /api/products</p>
                <p>Returns a sample product</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(template)

@app.route('/health')
def health():
    return {"status": "healthy", "version": "2.0"}

@app.route('/docs')
def docs():
    return render_template_string(template)

# ✅ ADDED: Handle JSON or HTML response for /api/products
@app.route('/api/sales')
def products():
    if "application/json" in request.headers.get("Accept", ""):
        return jsonify({"name": "Sale 1", "description": "Detail about product 1"})
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)
