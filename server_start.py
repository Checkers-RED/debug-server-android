from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/")
def hello():
    hello_text = "<h1 style = 'color:green'>Default route</h1>"
    hello_text += "Routes: <br>"
    hello_text += "<li>[post] /queue, requested: session </li>"
    hello_text += "<li>[get] /queue, requested: session </li>"
    return make_response(hello_text, 200)


# post /queue
@app.route("/queue", methods=["POST"])
def start_queue():
    try:
        current_session = request.json["session"]
    except Exception:
        return make_response("text", 400)

    # Какой-либо код обработки начала очереди
    return make_response("text", 200)


# get /queue
@app.route("/queue", methods=["GET"])
def check_queue():
    try:
        current_session = request.json["session"]
    except Exception:
        return make_response("text", 400)

    # Какой-либо код, обрабатывающий проверку статуса присутствия в очереди
    return make_response("Number in queue", 200)


# -----------------------------------------------------------------


if __name__ == "__main__":
    app.run(host="0.0.0.0")
