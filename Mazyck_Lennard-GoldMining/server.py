import random
from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "Free Willy"

@app.route('/')
def index():
    if 'gold' not in session:
        session["gold"] = 0
    if 'activity' not in session:
        session['activity'] = ''
    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def process():
    if 'Farm' == request.form['Location']:
        mining_gold = random.randint(10,20)
        opt = ["gain", "Lost"]
        selection = random.choice(opt)
        if selection == "gain":
            session["gold"] =+ mining_gold
            session['activity'] += f"<p style='color: green'>You plowed {mining_gold} from a farm!</p>"
        if selection == "Lost":
            session["gold"] =- mining_gold
            session['activity'] += f"<p style='color: red'>You lost {mining_gold} while grazing at the farm!</p>"
        return redirect('/')

    if 'Cave' == request.form['Location']:
        mining_gold = random.randint(5,10)
        opt = ["gain", "Lost"]
        selection = random.choice(opt)
        if selection == "gain":
            session["gold"] =+ mining_gold
            session['activity'] += f"<p style='color: green'>You earned {mining_gold} from a Cave!</p>"
        if selection == "Lost":
            session["gold"] =- mining_gold
            session['activity'] += f"<p style='color: red'>You lost {mining_gold} while scotting a Cave!</p>"
        return redirect('/')

    if 'House' == request.form['Location']:
        mining_gold = random.randint(2,5)
        opt = ["gain", "Lost"]
        selection = random.choice(opt)
        if selection == "gain":
            session["gold"] =+ mining_gold
            session['activity'] += f"<p style='color: green'>You earned {mining_gold} from searching a House!</p>"
        if selection == "Lost":
            session["gold"] =- mining_gold
            session['activity'] += f"<p style='color: red'>You lost {mining_gold} while pillaging a Home!</p>"
        return redirect('/')

    if 'Casino' == request.form['Location']:
        mining_gold = random.randint(-50,50)
        opt = ["gain", "Lost"]
        selection = random.choice(opt)
        if selection == "gain":
            session["gold"] =+ mining_gold
            session['activity'] += f"<p style='color: green'>You won {mining_gold} while placing bets at the Casino!</p>"
        if selection == "Lost":
            session["gold"] =- mining_gold
            session['activity'] += f"<p style='color: red'>You were robbed {mining_gold} from the Casino!</p>"
        return redirect('/')

@app.route('/rest')
def destroy():
    session.clear()
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True)