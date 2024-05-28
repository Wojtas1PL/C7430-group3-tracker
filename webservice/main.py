from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary to store data for multiple users
user_data = {}

@app.route('/')
def root():
    return render_template('base.html')

@app.route('/data', methods=["GET", "POST"])
def updater():
    if request.method == "GET":
        # Retrieve data for the current user based on session ID or user ID
        session_id = request.cookies.get('session_id')
        data = user_data.get(session_id, {'X': 0.0, 'Y': 0.0})
        return jsonify(data)
    elif request.method == "POST":
        try:
            session_id = request.cookies.get('session_id')
            x = float(request.form.get('X'))
            y = float(request.form.get('Y'))
            # Update data for the current user
            user_data[session_id] = {'X': x, 'Y': y}
            return 'OK'
        except (TypeError, ValueError):
            return 'Invalid input', 400

    return "you shouldn't be here!"

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8000, debug=True, ssl_context=('cert.pem', 'key.pem'))
