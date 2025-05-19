# flask for blog
from flask import Flask, render_template, request, redirect, url_for
import fileManager
import uuid

app = Flask(__name__)

# Define the route for the home page
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you would typically check the username and password against a database
        if username == 'adit' and password == '123':
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/logout')
def logout():
    return redirect(url_for('home'))


# Route for creating new articles in admin section
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        article = {
            "id": fileManager.generate_id(),
            "title": title,
            "content": content
        }
        fileManager.save_article_json(article)
        return redirect(url_for('admin'))
    else:
        return render_template('add.html')
    

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        article_id = request.form['article_id']
        title = request.form['title']
        content = request.form['content']
        article = {
            "id": int(article_id),
            "title": title,
            "content": content
        }
        fileManager.save_article_json(article)
        return redirect(url_for('admin'))
    else:
        article_id = request.args.get('article_id')
        articles = fileManager.load_all_articles()
        for article in articles:
            if str(article['id']) == str(article_id):
                return render_template('edit.html', article=article)
    return render_template('edit.html', article=article)


@app.route('/delete', methods=['POST'])
def delete():
    article_id = request.form['article_id']
    fileManager.delete_article(article_id)
    return redirect(url_for('admin'))

@app.route('/admin/view/article/<int:article_id>', methods=['GET'])
def view(article_id):
    articles = fileManager.load_all_articles()  
    for article in articles:
        if article['id'] == int(article_id):
            return render_template('view.html', article=article)
    return redirect(url_for('admin'))

@app.route('/admin')
def admin():    
    articles = fileManager.load_all_articles()
    return render_template('admin.html', articles=articles)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)