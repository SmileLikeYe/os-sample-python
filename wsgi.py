from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    print 'hello before'
    return "Hello World!"

if __name__ == "__main__":
    print '1'
    application.run()
    print '2'
