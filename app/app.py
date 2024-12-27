from flask import Flask

app = Flask(__name__)

@app.route('/')  # Ruta de ejemplo
def home():
    return "¡Hola, mundo!"

if __name__ == '__main__':
    app.run()
