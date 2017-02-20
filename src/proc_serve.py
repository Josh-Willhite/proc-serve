from flask import Flask, jsonify

app = Flask(__name__)


def proc_to_dict(info):
    parsed = {}
    for line in info:
        parsed_line = line.split(':')
        key = parsed_line[0].strip()
        if len(parsed_line) > 1:
            value = parsed_line[1].strip()
        else:
            value = ''
        parsed[key] = value
    return parsed


def get_info(proc_file):
    with open('/proc/{}'.format(proc_file), 'r') as f:
        info = f.read().splitlines()
    return [line for line in info if line]


@app.route('/cpuinfo')
def cpu_info():
    info = get_info('cpuinfo')
    return jsonify(proc_to_dict(info))


@app.route('/meminfo')
def mem_info():
    info = get_info('meminfo')
    return jsonify(proc_to_dict(info))


@app.route('/uptime')
def uptime():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1404)
