from itertools import chain
from flask import Flask,render_template,request
import os
import block
found=False
global b
b={}

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
    global b
    if request.method=="POST":
        id=request.form.get('id')
        chain=block.block_chain_file()
        for i in chain["blockchain"]:
            if int(id)==i["index"]:
                b=i
                print(b)
                found=True
                break
    return render_template('index.html')

@app.route("/blockdisplay")
def check():
    list = [(k, v) for k, v in b.items()]
    return render_template('index.html',blockdisplay=list)

@app.route("/Create_block",methods=['POST','GET'])
def creation():
    if request.method=="POST":
        LastName=request.form.get('Last Name')
        FirstName=request.form.get('First Name')
        University=request.form.get('University')
        Degree=request.form.get('Degree')
        Date=request.form.get('Date')
        block.create_block(LastName,FirstName,University,Degree,Date,1,'')
        block.mine()
    return render_template("create_degree.html")



os.environ.setdefault('FLASK_ENV', 'development')
app.run(host='127.0.0.1', port=5000)




