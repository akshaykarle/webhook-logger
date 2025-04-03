from flask import Flask, request
import pprint

app = Flask(__name__)

@app.route('/', methods=['POST'])
def log_payload():
    payload = request.get_json()
    with open('payload_log.txt', 'a') as f:
        f.write(str(payload) + '\n')
    pprint.pprint('*** Payload received: ***')
    pprint.pprint(payload)
    pprint.pprint('*** End of Payload ***')
    return 'Payload received', 200

if __name__ == '__main__':
    app.run(port=8080)
