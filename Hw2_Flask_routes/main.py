from flask import Flask, request
import utils

app = Flask(__name__)


@app.route("/requirements")
def requirements():
    return utils.requirements()


@app.route("/generate-users")
def generate_users():
    length = request.args.get('length', '100')
    if length.isdigit():
        length = int(length)
        max_length = 500
        if length > max_length:
            return f'Length should be less then {max_length}'
        return utils.generate_users(length)
    return f'Invalid length value: {length}'


@app.route("/space")
def space():
    return utils.space()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
