import sys
from flask import Flask, request

app = Flask(__name__)

@app.route("/performAction", methods=["POST", "GET"])
def performAction():
    data = request.json
    if data['data'] == 0:
        return "Turn Off Fan"
    else:
        return "Turn On Fan"


if __name__ == "__main__":
    port = sys.argv[1]
    app.run(port=port, host="0.0.0.0", use_reloader=False,debug=True)