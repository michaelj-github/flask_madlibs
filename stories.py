"""Madlibs Stories."""
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.config['SECRET_KEY'] = "mjm34442"
debug = DebugToolbarExtension(app)
storytype = ''

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "adjective", "noun", "verb", "plural-noun"],
    """Once upon a time in {place}, there lived a
       {adjective} {noun}. It loved to {verb} {plural-noun}."""
)

shortstory = Story(
    ["subject", "verb", "object"],
    """{subject} {verb} {object}."""
)

longstory = Story(
    ["adjective", "subject", "verb", "another-adjective", "object"],
    """The {adjective} {subject} {verb} the {another-adjective} {object}."""
)

@app.route('/')
def index():
    """Home Page"""
    return render_template("home.html")

@app.route('/form')
def display_form():
    global storytype
    storytype = request.args["astory"]
    if storytype == "short story":
        thestory = shortstory
    elif storytype == "long story":
        thestory = longstory
    else:
        thestory = story
    return render_template("form.html", thestory = thestory)


@app.route('/result')
def display_result():
    global storytype
    if storytype == "short story":
        thestory = shortstory.generate(request.args)
    elif storytype == "long story":
        thestory = longstory.generate(request.args)
    else:
        thestory = story.generate(request.args)
    return render_template("result.html", thestory = thestory)
