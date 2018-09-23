import smartcar
from flask import Flask, request, jsonify
import json

with open("config.json", 'r') as f:
    config = json.load(f)

app = Flask(__name__)

client = smartcar.AuthClient(
    client_id=config['client_id'],
    client_secret=config['client_secret'],
    redirect_uri='http://localhost:8000/callback',
    scope=['read_vehicle_info', 'read_location', 'read_odometer'],
    test_mode=True
)


@app.route('/', methods=['GET'])
def index():
    auth_url = client.get_auth_url(force=True)
    return '''
        <h1>Hello, Hackbright!</h1>
        <a href=%s>
          <button>Connect Car</button>
        </a>
    ''' % auth_url


@app.route('/callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    access = client.exchange_code(code)

    print(access)

    return jsonify(access)


if __name__ == '__main__':
    app.run(port=8000)