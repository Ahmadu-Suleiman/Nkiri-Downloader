import asyncio
import socket
import webbrowser

from flask import Flask, request, render_template
from waitress import serve

import download

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def process_form():
    link = request.form.get('link')

    asyncio.run(download.start_downloads(link))
    return render_template('download.html')


if __name__ == '__main__':
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    port = 8080
    url = f'http://{local_ip}:{port}/'

    webbrowser.open_new(url)
    serve(app, host=local_ip, port=port)
