from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/home")
def homepage():
    # Read facts from temp.txt using UTF-8 encoding and store them in a list
    with open("temp.txt", 'r', encoding='utf-8') as f:
        facts = [line.strip() for line in f.readlines() if line.strip()]
    
    # Select one random fact from the list
    random_fact = random.choice(facts) if facts else "No facts available."
    
    # Pass the random fact to the index.html template
    return render_template('index.html', fact=random_fact)

if __name__ == "__main__":
    app.run(debug=True)
