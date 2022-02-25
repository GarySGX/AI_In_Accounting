from flask import Flask
from flask import request, render_template
from keras.models import load_model
import joblib


app = Flask(__name__)


# @app.route("/", methods = ['GET',"POST"])
# def index():
#     if request.method == "POST":
#         return(render_template("index.html",result = "1"))
#     else:
#         return(render_template("index_html",result = "2"))

# if __name__ == "__main__":
#     app.run()

@app.route("/", methods = ["GET", "POST"])

def init():
	if request.method == "POST":
		income = request.form.get("income")
		age = request.form.get("age")
		loan = request.form.get("loan")
		print(income, age, loan)
		model = load_model("model_file")
		transformer = joblib.load('MinMaxScaler')
		pred = model.predict(transformer.transform([[float(income),float(age), float(loan)]]))
		print(pred)
		pred = pred[0][0]
		s = "Predicted Default is " + str(pred)
		return(render_template("index.html", result = s))
	else:
		return(render_template("index.html", result = "Predict Default"))
if __name__ == "__main__":
	app.run()





