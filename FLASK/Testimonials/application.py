from  flask import Flask
# brings flask class from flask module
app= Flask(__name__)

# create a new flask object
#

@app.route("/")
def index():
    return "hello"




@app.route('/api/testimonials')

def testimonials():
    return {'testimonials':['great', 'tis ok', 'fantastic']}



