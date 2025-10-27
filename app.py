from flask import Flask, render_template
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_spends_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM spendings"))
    spendings = result.mappings().all()
  return spendings
      
@app.route('/')
def hello_world():
  spendings = load_spends_from_db()
  return render_template('home.html', spendings=spendings)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)