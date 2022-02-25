from flask import Flask
from flask import request, render_template
from keras.models import load_model



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
		NP_TA = request.form.get("NP_TA")
		TL_TA = request.form.get("TL_TA")
		WC_TA = request.form.get("WC_TA")
		print(NP_TA, TL_TA, WC_TA)
		model = load_model("bm")
		pred = model.predict([[float(NP_TA), float(TL_TA), float(WC_TA)]])
		print(pred)
		pred = pred[0][0]
		s = "Predicted Bankruptcy Score is " + str(pred)
		return(render_template("main.html", result = s))
	else:
		return(render_template("main.html", result = "Predict Bankruptcy"))

	app.run()





