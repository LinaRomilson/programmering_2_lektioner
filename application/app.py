from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def hello():
    dictionary = {
        "Landsdel": ["Götaland", "Götaland", "Götaland", "Svealand", "Svealand", "Norrland", "Norrland", "Norrland",
                     "Norrland", "Norrland"],
        "Landskap": ["Östergötland", "Östergötland", "Västergötland", "Södermanland", "Södermanland", "Norrbotten",
                     "Gästrikland", "Ångermanland", "Ångermanland", "Ångermanland"],
        "Stad": ["Linköping", "Motala", "Mjölby", "Mariefred", "Nyköping", "Piteå", "Sandviken", "Sollefteå",
                 "Kramfors", "Örnsköldsvik"]
        }
    df = pd.DataFrame(dictionary)
    html = df.to_html(classes="table table-striped", justify="left", index=False)
    return render_template('template.html', data=html)
