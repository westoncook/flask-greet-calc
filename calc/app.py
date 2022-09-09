from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)




@app.route('/add')
def add_queries():
 return str(add(int(request.args['a']), int(request.args['b'])))

@app.route('/sub')
def sub_queries():
 return str(sub(int(request.args['a']), int(request.args['b'])))

@app.route('/mult')
def mult_queries():
 return str(mult(int(request.args['a']), int(request.args['b'])))

@app.route('/div')
def div_queries():
 return str(div(int(request.args['a']), int(request.args['b'])))

@app.route('/math/<op>')
def perform_op(op):
    return str(ops[op]())


ops = {
    "add" : add_queries,
    "sub": sub_queries,
    "mult": mult_queries,
    "div": div_queries
}
