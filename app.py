from flask import Flask, render_template, request
from summarizer import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    raw_text = request.form['text']
    summary, _, original_length, summary_length = summarizer(raw_text)
    return render_template('result.html', summary=summary, original_length=original_length, summary_length=summary_length)

if __name__ == '__main__':
    app.run(debug=True)