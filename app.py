from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

PRESSURES = ["1.5", "2.0", "2.5", "3.0"]
FREQUENCIES = ["8", "10", "12", "15"]
SHOCK_COUNTS = ["1500", "2000", "2500", "3000"]
TREATMENT_FREQS = ["1x/week", "2x/week", "3x/week", "Other"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        soap_note = f"""
        ----------------------------------------
        SOAP Note for: {data['patient_name']}
        Date: {data['date_of_visit'] or datetime.today().strftime('%Y-%m-%d')}
        ----------------------------------------
        S - Subjective:
        {data['subjective']}

        O - Objective:
        {data['objective']}

        A - Assessment:
        {data['assessment']}

        P - Plan:
        {data['plan']}
        """

        if data.get("include_shockwave") == "yes":
            soap_note += f"""
            Shockwave Therapy Treatment Plan:
            - Target Region: {data['region']}
            - Pressure: {data['pressure']} bar
            - Frequency: {data['frequency']} Hz
            - Number of Shocks: {data['shocks']}
            - Treatment Frequency: {data['treatment_freq']}
            - Duration: Typically 6-12 sessions based on patient response and severity
            - Goals: Reduce inflammation, break down adhesions, stimulate tissue healing.
            """

        soap_note += "\n----------------------------------------"
        return f"<pre>{soap_note}</pre>"

    return render_template(
        'form.html',
        pressures=PRESSURES,
        frequencies=FREQUENCIES,
        shock_counts=SHOCK_COUNTS,
        treatment_freqs=TREATMENT_FREQS
    )

if __name__ == '__main__':
    app.run(debug=True)
