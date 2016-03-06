from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def template_test():
    #return render_template('img_template.html', my_string="Dieee!", my_list=[0,1,2,3,4,5])
    return render_template('img_template.html', my_string="T4!", my_list=[0,1,2,3,4,5])
    #return render_template('img_template.html')

if __name__ == '__main__':
    app.run(debug=True)