from flask import Flask,jsonify,request
from website.chat import agent

app = Flask(__name__)

@app.route('/bot',methods = ['POST', 'GET'])
def cryptobot():    

    question = request.args.get("question")
    answer = (agent.run(question))
    return jsonify( answer )


@app.route('/')
def  home():
    return "nIKHIL"



if __name__ == '__main__':

    app.run(debug=True)

