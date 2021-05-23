from flask import Flask,render_template
app = Flask(__name__)
@app.route('/get_toggled_status')
def toggled_status():
  current_status = flask.request.args.get('status')
  return 'Toggled' if current_status == 'Untoggled' else 'Untoggled'
app.run(debug=False)