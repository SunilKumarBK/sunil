from flask import Flask,render_template,redirect
from read import read


app = Flask(__name__)

app.register_blueprint(read)


@app.route("/")
def home():
    # return "kiijhihihi"
    return redirect('/read')
 

if __name__=="__main__":
    app.run(debug=True)
