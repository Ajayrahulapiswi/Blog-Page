
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def initial():
  app.logger.debug("Loading initial route")
  return render_template("index.html")



# run the Flask application
if __name__ == "__main__":



  app.run(
    host='0.0.0.0',
    port=9001,
    debug=True)
