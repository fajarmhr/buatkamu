from flask import Flask,render_template,request,redirect
from models import SurveyModel, db
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sepikan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('index.html')
 
    if request.method == 'POST':
        nick = request.form['nick']
        name = request.form['namalengkap']
        syg = request.form['syg']
        survey = SurveyModel(name=name, nick=nick, syg=syg)
        db.session.add(survey)
        db.session.commit()
        return ('', 204)
        # return redirect("/bukawa")


# @app.route('/iniadmin')
# def adminGG():
#     sepikannlist = SurveyModel.query.all()
#     return render_template('iniadmin.html', sepikannlist = sepikannlist)


@app.route('/viewhaha')
def RetrieveList():
    sepikannlist = SurveyModel.query.all()
    return render_template('datalist.html', sepikannlist = sepikannlist) 


# @app.route("/update", methods=["POST"])
# def update():
#     id = request.form.get("id")
#     newname = request.form.get("newname")
#     newnick = request.form.get("newnick")
#     sepikann = SurveyModel.query.filter_by(id=id).first()
#     sepikann.name = newname
#     sepikann.nick = newnick
#     db.session.commit()
#     return redirect("/iniadmin")


# @app.route("/delete", methods=["POST"])
# def delete():
#     id = request.form.get("id")
#     sepikann = SurveyModel.query.filter_by(id=id).first()
#     db.session.delete(sepikann)
#     db.session.commit()
#     return redirect("/iniadmin")


# @app.route("/bukawa") 
# def bukaWa(): 
#     return redirect("https://api.whatsapp.com/send?phone=&text=Hai,%20aku%20udah%20bacain%20semuanya")


app.run(host='localhost', port=5000)