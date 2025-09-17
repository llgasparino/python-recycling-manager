from flask import Flask, render_template
import os

# Ajusta os caminhos para templates e static
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '../recycling_manager/templates')
STATIC_DIR = os.path.join(BASE_DIR, '../recycling_manager/static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route("/")
def home():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("page_not_found.html"), 404

# Outras rotas podem ser adicionadas aqui

# Vercel espera a variável 'app' para exportar
