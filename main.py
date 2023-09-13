from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def takeinput():
    return render_template('index.html')

@app.route('/Pass/<float:per>')
def Pass(per):
    res = 'Pass'
    return render_template('results.html', per=per, res=res)

@app.route('/Fail/<float:per>')
def Fail(per):
    res = 'Fail'
    return render_template('results.html', per=per, res=res)

@app.route('/submit', methods=['POST', 'GET'])
def postsubmit():
    res =""
    if request.method == 'POST':
        c = float(request.form['c-language'])
        datascience = float(request.form['data-science'])
        maths = float(request.form['maths'])
        per = (((c+datascience+maths)/300) * 100)
        if c < 35 or datascience < 35 or maths < 35:
            res = 'Fail'
            return redirect(url_for(res, per=per))
        else:
            res = 'Pass'
            return redirect(url_for(res, per=per))

if __name__ == '__main__':
    app.run(debug=True)



