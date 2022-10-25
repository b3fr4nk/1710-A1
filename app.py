import random
from flask import Flask

#create flask server
app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/favorite_dessert/<user_query>')
def favorite_dessert(user_query):
    return f"How did you know I liked {user_query}"

@app.route('/madlib/<noun1>/<noun2>')
def madlib(noun1, noun2):
    return f"what did the {noun1} say to the {noun2}? I don't know you started the joke."

@app.route('/multiply/<num1>/<num2>')
def multiply2(num1, num2):
    if num1.isnumeric() and num2.isnumeric():
        num1 = int(num1)
     
        num2 = int(num2)

        return f"{num1 * num2}"

@app.route('/repeat/<word>/<times>')
def repeat_word(word, times):
    if times.isnumeric():
        times = int(times)

        word += " "
        return word * times

@app.route('/dicegame')
def dicegame():
    rand = random.randrange(1, 6)
    return f"{rand}p"
    
if __name__ == '__main__':
    app.run(debug=True)