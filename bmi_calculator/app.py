from flask import Flask, render_template, request
import webbrowser
import threading

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi():
    bmi_result = ""
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"

            bmi_result = f"Your BMI is {bmi:.2f} — {category}"
        except:
            bmi_result = "Please enter valid numbers."
    return render_template("index.html", result=bmi_result)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    # Open the browser in a new thread so it doesn’t block Flask
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True)
