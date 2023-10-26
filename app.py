from flask import Flask,render_template,request,redirect,url_for,flash
from database import db, Data



app = Flask(__name__)


app.secret_key= "asasasasa"

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///CRUD-operations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_request
def create_table():
    db.create_all()



@app.route('/')
def index():
    all_data=Data.query.all()
    return render_template("index.html", employees=all_data)
@app.route('/insert', methods=['POST'])
def insert():  # put application's code here

    if request.method == 'POST':

        name=request.form['name']

        email=request.form['email']
        phone = request.form['phone']

        my_data=Data(name,email,phone)

        db.session.add(my_data)

        db.session.commit()
        flash("Employee inserted successfully ")
        return redirect(url_for('index'))


@app.route('/update', methods=['GET','POST'])
def update():

    if request.method == 'POST':
        my_data=Data.query.get(request.form.get('id'))


        my_data.name=request.form['name']

        my_data.email=request.form['email']
        my_data.phone=request.form['phone']



        db.session.commit()

        flash("Employee updated Successfully")
        return redirect('/')





@app.route('/delete/<id>', methods=['GET', "POST"])
def delete ( id ) :
    my_data=Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully" )
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

