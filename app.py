from flask import Flask, render_template
import search_region_and_operator


from forms import LoginForm
app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        number_phone = form.username.raw_data[0]
        result_numb = search_region_and_operator.search_numb.search_region_and_operator(number_phone)
        print(result_numb)
        return str(result_numb)
    return render_template('login.html', title='number', form=form)


if __name__ == '__main__':
   app.run(debug = True)