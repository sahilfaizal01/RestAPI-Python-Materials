import flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello world!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sums = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sums += digit **order
        n = n//10
    
    if(sums == copy_n):
        print(f"{copy_n} is an armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": True
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": False
        }
    
    
    return jsonify(result)
    

if __name__ == "__main__":
    app.run(debug=True)

