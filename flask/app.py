from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    with open('file.txt','r') as file:
        content = file.read()
    return content

if __name__ == "__main__":
    app.run()