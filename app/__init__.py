import flask,requests,json 
import jinja2
from authlib.flask.client import OAuth

app = flask.Flask(__name__)

@app.route("/")
def home_view():
    return flask.render_template("form.html",name="Abhi",bday="February 7, 2007")

@app.route("/formsubmit",methods=['POST'])
def infosubmit():
    if(requests.method=="POST"):
        print(request.form["fname"])
        return jsonify(
                message="thanks",
                category="success",
                status=200
            )
    else:
        return jsonify(
                message="invalid test",
                category="fail",
                data=data,
                status=500
            )

@app.route("/abc")
def abc():
    return jsonify(
                message="good test",
                category="success",
                data=data,
                status=200
            )
