from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <h1>Home</h1>
    <a href='/search'>Search</a><br>
    <a href='/hello'>Hello</a><br>
    <a href='/bye'>Bye</a><br>
    <a href='/add'>Go to the Add Comments Page</a><br>
    <a href='/show'>Go to the Show Comments Page</a>

    """
    return html
    # return "Home"

@app.route('/hello')
def hello_page():
    html = """
    <h1>Hello</h1>
    <a href='/'>Home</a><br>
    <a href='/bye'>Bye</a>
    """
    return html
    # return "Hello"

@app.route('/bye')
def bye_page():
    html = """
    <h1>Bye</h1>
    <a href='/'>Home</a><br>
    <a href='/hello'>Hello</a>
    """
    return html
    # return "Bye"

@app.route('/search')
def search_page():
    # html = """
    # <h1>Search</h1>
    # <a href='/'>Home</a><br>
    # <p>f"{request.args}"</p>
    # """
    # return_string = " " #"<h1>Search</h1><br>" + f"{request.args['sort']} {request.args['term']}" + "<br><br><a href='/'>Home</a>"
    return_string = "<h1>Search</h1><br>" + "<br><br><a href='/'>Home</a>"
    # return_html = """
    #
    # f"<h1>{request.args['term']}</h1>"
    # f"<h1>{request.args}</h1>"
    # """

    return return_string
    # return f"<h1>{request.args}</h1>"


@app.route('/add')
def add_comment_form():
    return """
        <html>
            <body>
            <h1>Add a comment</h1>
            <form method="POST">
                <input type="text" placeholder='your comment' name='comment'/>
                <button>Submit</button>
            </form>
                <br><a href='/'>Go to the Home Page</a><br>
                <a href='/hello'>Go to the Hello Page</a><br>
                <a href='/bye'>Go to the Bye Page</a>
            <body>
        </html>

    """

@app.route('/add', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    return f"""
        <html>
            <body>
                <h1>Saved the comment: {comment}</h1>
                <a href='/'>Go to the Home Page</a><br>
                <a href='/hello'>Go to the Hello Page</a><br>
                <a href='/bye'>Go to the Bye Page</a><br>
                <a href='/add'>Go to the Comments Page</a>
            <body>
        </html>

    """

COMMENTS = {
    1: "just an initial comment",
    2: "getting the conversation started",
    3: "everyone can join in"
}


@app.route('/show')
def show_comment_form():
    return """
        <html>
            <body>
            <h1>Show a comment</h1>
            <form method="POST">
                <input type="text" placeholder='comment number' name='id'/>
                <button>Submit</button>
            </form>
                <br><a href='/'>Go to the Home Page</a><br>
            <body>
        </html>

    """


# @app.route('/show/<int:id>')
@app.route('/show', methods=["POST"])
# def find_comment(id):
def find_comment():
    # comment = COMMENTS.get(id, "no comment found for that number")
    id = int(request.form["id"]) # will need a try block to handle incorrect input type error
    comment = COMMENTS.get(id, "no comment found for that number")
    return f"""
    <html>
        <body>
            <h1>Here's the comment: {comment}</h1>
            <a href='/'>Go to the Home Page</a><br>
            <a href='/show'>Go to the Show Comments Page</a>
        <body>
    </html>

    """
