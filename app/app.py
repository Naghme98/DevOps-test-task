from flask import Flask
from pytz import timezone
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_geek():
    format = "%Y-%m-%d %H:%M:%S %Z%z"
    date = datetime.now()
    now_utc = date.now(timezone('UTC'))
    now_moscow = now_utc.astimezone(timezone('Europe/Moscow'))
    return "<body style='text-align:center;margin-top:10%'>\
            <h1> Hello My Friends!</h1>\
            <h3> The exact time is:   </h3> \
            <h4>" + now_moscow.strftime(format) + "</h4>    \
        </body>"


if __name__ == "__main__":
    app.run(debug=True)