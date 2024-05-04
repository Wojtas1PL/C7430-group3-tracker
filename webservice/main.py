from flask import Flask, render_template, request, jsonify
app=Flask(__name__)

app.config['X'] = 0
app.config['Y'] = 0

@app.route('/')
def root():
   # markers=[
   # {
   # 'lat':0,
   # 'lon':0,
   # 'popup':'This is the middle of the map.'
   #  }
   # ]
   return render_template('base.html')


@app.route('/data', methods=["GET", "POST"])
def updater():
   if request.method == "GET":
      data = {
         'X': app.config['X'],
         'Y': app.config['Y']
      }
      return jsonify(data)
   elif request.method == "POST":
      app.config['X'] = request.form.get('X')
      app.config['Y'] = request.form.get('Y')
      return 'OK'

   return 'shouldnt be here'

if __name__ == '__main__':
   app.run(host="localhost", port=8080, debug=True)
