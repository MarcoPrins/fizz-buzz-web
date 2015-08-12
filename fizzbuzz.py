from flask import Flask, render_template
from flask_bootstrap import Bootstrap

class Entry():
  def __init__(self, number):
    self.number = number
    if (number%3 == 0):
      self.fizz = True
      if (number%5 == 0):
        self.buzz = True
        self.color = "green"
    elif (number%5 == 0):
      self.buzz = True

def create_application():
  application = Flask(__name__)
  Bootstrap(application)
  application.debug = True

  return application

app = create_application()

@app.route('/')
def index():
  entries = []
  for i in range(1, 101):
    entries.append(Entry(i))

  return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(host='0.0.0.0')