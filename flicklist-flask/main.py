from flask import Flask
import random
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    movie2 = get_random_movie()


    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    content += "<h1>Tomorrow's Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie2 + "</li>"
    content += "</ul>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movie_list = ["The Big Lebowski", "Shaun of the Dead", "The Princess Bride", "The Fifth Element", "Guardians of the Galaxy"]
    # TODO: randomly choose one of the movies, and return it
    return (random.choice(movie_list))


app.run()