from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'


@app.route('/about')
def about():
    return 'About page'


@app.route('/blog')
def blog():
    posts = [{'title': 'tech', 'author': 'jb'}, {
        'title': 'philosophy', 'author': 'gaby'}]
    return render_template('blog.html', author="bob", sunny=True, posts=posts)


@app.route('/blog/<blog_id>')
def blogpost(blog_id):
    return 'This is blog post number ' + str(blog_id)


if __name__ == '__main__':
    app.run()
