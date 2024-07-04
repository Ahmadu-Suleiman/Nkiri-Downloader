import asyncio
import socket
import webbrowser

from flask import Flask, request, render_template, redirect
from waitress import serve

from src.download import start_downloads

app = Flask(__name__)


@app.route('/')
def index():
    return redirect("/form")


@app.route('/form', methods=['GET'])
def show_form():
    return render_template('form.html')


@app.route('/process', methods=['POST'])
def process_form():
    link = request.form.get('link')

    asyncio.run(start_downloads(link))
    return render_template('download.html')


if __name__ == '__main__':
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    port = 8080
    url = f'http://{local_ip}:{port}/'

    webbrowser.open_new(url)
    serve(app, host=local_ip, port=port)
