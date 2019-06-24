from flask import Flask, request, render_template, redirect
app = Flask(__name__)

uname = ''
email = ''

@app.route("/", methods=['GET', "POST"])
def index():
    global uname
    global email
    user_name = uname
    un_error = request.args.get('un_error')
    pword_error = request.args.get('pword_error')
    pmatch_error = request.args.get('pmatch_error')
    user_email = email
    mail_error = request.args.get('mail_error')
    return render_template('index.html', user_name = user_name,
                                user_email = user_email,
                                username_error=un_error,
                                password_error=pword_error,
                                pass_match_error=pmatch_error,
                                user_email_error=mail_error)

@app.route("/auth", methods=["POST", "GET"])
def auth():
    rdr_string = '/?'
    global uname
    global email
    uname = request.form['user_name']
    pword = request.form['password']
    pword_match = request.form['pass_match']
    email = request.form['user_email']
    if len(uname) < 3:
        rdr_string = rdr_string + "un_error=yes&"
    if len(pword) < 3 or len(pword)>20:
        rdr_string = rdr_string + "pword_error=yes&"
    if pword != pword_match:
        rdr_string = rdr_string + "pmatch_error=yes&"
    if email != "":
        if ('@' in email) and ('.' in email):
                rdr_string = rdr_string
        else:
            rdr_string = rdr_string + "mail_error=yes&"
    if len(rdr_string) > 2:
        return redirect(rdr_string)
    else:
        return render_template('welcome.html', user_name=uname)


if __name__ == "__main__":
    app.run(debug=True)