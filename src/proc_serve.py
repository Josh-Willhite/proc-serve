from flask import Flask

app = Flask(__name__)


@app.route('/cpuinfo')
def cpu_info():
    pass


@app.route('/meminfo')
def mem_info():
    pass


@app.route('/uptime')
def uptime():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1404)
