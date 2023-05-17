from flask import Flask, jsonify,render_template,request

app = Flask(__name__)

@app.route("/calculate")
def calculate():
    input =request.args.get('input')
    try:
        return jsonify({'res':eval(input),'status':'good'})
    except SyntaxError:
        return jsonify({'status':'bad'})

@app.route('/')
def mainPage():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()