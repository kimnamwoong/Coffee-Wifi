from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)



class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location link(URL)',validators=[DataRequired(),URL()])
    open_time = StringField('Open Time(ex:9:00 AM)',validators=[DataRequired()])
    close_time = StringField('Close Time(ex:9:00 PM)', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee rating',choices=["☕","☕☕","☕☕☕","☕☕☕☕","☕☕☕☕☕"], validators=[DataRequired()])
    wifi = SelectField('Wifi strength',choices=["✘","💪","💪💪","💪💪💪","💪💪💪💪","💪💪💪💪💪"], validators=[DataRequired()])
    power = SelectField('Power availability',choices=["✘","🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌🔌","🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        csv_data = [form.cafe.data,form.location.data,form.open_time.data,form.close_time.data,form.coffee_rating.data,form.wifi.data,form.power.data]
        with open('cafe-data.csv','a',encoding='utf-8') as csv_file:
            writer_object = csv.writer(csv_file)
            writer_object.writerow(csv_data)
            csv_file.close()
            return redirect(url_for('add_cafe'))

            # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='',encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
