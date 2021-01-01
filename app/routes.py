from flask import render_template, redirect, request, url_for
from app import flask_app
from app.forms import LoginForm
from collections import OrderedDict
import pronouncing
from collections import OrderedDict

@flask_app.route('/', methods=['GET','POST'])
@flask_app.route('/index', methods=['GET','POST'])
def index():
    form = LoginForm()

    if form.validate_on_submit():
        input = request.form['word']
        #Assign None and not an empty string  to filter_len and #filter_alpha if request.form
        filter_len = None if not request.form['length'] else  request.form['length']
        filter_alpha = None if not request.form['alphabet'] else request.form['alphabet']
        return redirect(url_for('rhymes', input_word=input, input_len=filter_len, input_alpha=filter_alpha))

    return render_template('form.html', title="Generate rhyming words", form=form)


@flask_app.route('/rhymes/<string:input_word>', defaults={'input_len': None, 'input_alpha': None}, methods=['GET'])
@flask_app.route('/rhymes/<string:input_word>/<int:input_len>/', defaults={'input_alpha': None}, methods=['GET'])
@flask_app.route('/rhymes/<string:input_word>/<input_len>/<string:input_alpha>', defaults={'input_len': None}, methods=['GET'])
@flask_app.route('/rhymes/<string:input_word>/<int:input_len>/<string:input_alpha>', methods=['GET'])
def rhymes(input_word, input_len, input_alpha):
    result = GetRhymes.generate_rhymes(input_word)
    #Filter words according to their length
    if input_len is not None:
        result = [word for word in result if len(word) == input_len]
    #Filter words according to their starting alphabet
    if input_alpha is not None:
        result = [word for word in result if word[0] == input_alpha]

    return render_template('result.html', result=', '.join(result))

class GetRhymes():
    @staticmethod
    def generate_rhymes(word):
        if word is None :
            return ''

        #result is now a list of words
        result = list(OrderedDict.fromkeys(pronouncing.rhymes(word)))
        #if empty list returned, return a message
        if not result:
            return ' No words '

        return result
