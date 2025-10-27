from flask import Flask, render_template
from database import engine
from sqlalchemy import text

app = Flask(__name__)


@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM sample"))
    jobs = []
    for row in result.mappings().all():
      jobs.append(dict(row))
      return jobs


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
