# app.py
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# 全局注入 current_data，给 footer 用
@app.context_processor
def inject_now():
    return { 'current_date': datetime.now().strftime('%Y-%m-%d')
            }

# Homepage
@app.route('/')
def home():
    return render_template('home.html', active='home')

# About Me (lynn.html)
@app.route('/about')
def about():
    return render_template('about.html', active='about')

# Research (projects)
@app.route('/research')
def research():
    return render_template('research.html', active='research')

# News
@app.route('/news')
def news():
    return render_template('news.html', active='news')

# Publications
@app.route('/publications')
def publications():
    return render_template('publication.html', active='publications')

# Contact
@app.route('/contact')
def contact():
    return render_template('contact.html', active='contact')

if __name__ == '__main__':
    # debug=True 开发时自动重载、输出调试信息
    app.run(host='127.0.0.1', port=5000, debug=True)