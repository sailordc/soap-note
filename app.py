from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    note = ""
    if request.method == 'POST':
        subjective = request.form['subjective']
        objective = request.form['objective']
        assessment = request.form['assessment']
        plan = request.form['plan']
        shockwave = request.form['shockwave']
        note = f"""
        **SOAP Note**

        **Subjective:** {subjective}

        **Objective:** {objective}

        **Assessment:** {assessment}

        **Plan:** {plan}

        **Shockwave Parameters:** {shockwave}
        """
    return render_template('form.html', note=note)

if __name__ == '__main__':
    app.run(debug=True)
