from flask import Flask,render_template;
app=Flask(__name__)

posts=[
    {
        'title':'good comes to u',
        'author':'Johny',
        'dates_on':'5th feb'
        
    },
    {
        'title':'hope feel good',
        'author':'kama',
        'dates_on':'6th feb'
    }
    
]

@app.route('/')
def hello():
    return "hi shruu";
@app.route('/home')
def home():
    return render_template("home.html",posts=posts)
@app.route('/about')
def about():
    return render_template("about.html")
if __name__=='__main__':
    app.run(debug=True);   