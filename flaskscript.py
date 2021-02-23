from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

posts = [
	{
		"author" : "Conroy Ricketts",
		"title" : "My first blog post!",
		"date" : "02/23/2021",
		"content" : "This is my first blog post. Take it for what it is."
	},
	{
		"author" : "John Smith",
		"title" : "Aliens are real.",
		"date" : "01/15/2021",
		"content" : "I couldn't believe what I saw! 2 aliens were on my front porch this morning."
	},
	{
		"author" : "Evan Roberts",
		"title" : "Why you should go to a jazz concert.",
		"date" : "02/20/2021",
		"content" : "You all should go to a jazz concert because they are cool."
	}
]

@app.route('/')
@app.route('/home/')
def home():
	return render_template('home.html', posts = posts, title = "Home")

@app.route('/about/')
def about():
	return render_template('about.html', title = "About")

@app.route('/about_conroy/')
def about_conroy():
	return redirect(url_for('about'))

if __name__ == '__main__':
	app.run(debug = True)
	