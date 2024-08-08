from flask import Flask
from flask import jsonify
import os
app=Flask(__name__)

@app.route('/')
def hello():
    """Return a frinedly HTTP greeting."""
    print("I am inside hello world")
    return "Hello world"

@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val={"new-name":name}
    return jsonify(val)

if __name__=='__main__':
    #app.run(host='127.0.0.1',port=8080,debug=True)
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))