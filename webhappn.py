from flask import Flask, render_template, request, jsonify,url_for,redirect,session
import happncontroller
app = Flask(__name__)

@app.route("/recommendations")
def recommendations():
    recs = happncontroller.getRecommendations()
    return render_template("profiles.html", recs=recs)

@app.route("/matches")
def matches():
    return render_template("matches.html")

@app.route("/decline/<string:id>/")
def decline(id):
    happncontroller.declineUser(id)
    return redirect(url_for('recommendations'))

@app.route("/like/<string:id>/")
def like(id):
    happncontroller.likeUser(id)
    return redirect(url_for('recommendations'))

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)