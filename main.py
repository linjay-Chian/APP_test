import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Basic HTML template as a string for a single-file example
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud Run Test</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
        .container { border: 2px solid #4285F4; display: inline-block; padding: 20px; border-radius: 10px; background: white; }
        h1 { color: #4285F4; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Deployment Successful!</h1>
        <p>Your Python & HTML app is running on <strong>Google Cloud Run</strong>.</p>
        <p>Status: <span style="color: green;">Online</span></p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Serves the main HTML page."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health_check():
    """A simple endpoint to verify the service is responding."""
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    # Cloud Run passes the port via environment variable. 
    # Defaulting to 8080 is critical for compatibility.
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)