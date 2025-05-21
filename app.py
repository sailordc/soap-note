from flask import Flask, render_template, request

app = Flask(__name__)
import json

@app.route('/', methods=['GET', 'POST'])
def index():
    note = ""
    with open('macros.json') as f:
        macros = json.load(f)

    if request.method == 'POST':
        body_area = request.form.get('body_area', '')
        subjective = request.form.get('subjective', '')
        objective = request.form.get('objective', '')
        assessment = request.form.get('assessment', '')
        plan = request.form.get('plan', '')
        shockwave = request.form.get('shockwave', '')

        note = f"""
        **SOAP Note**

        **Body Area:** {body_area}

        **Subjective:** {subjective}

        **Objective:** {objective}

        **Assessment:** {assessment}

        **Plan:** {plan}

        **Shockwave Parameters:** {shockwave}
        """

    return render_template('form.html', note=note, macros=macros)
