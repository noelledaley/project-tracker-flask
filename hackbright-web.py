from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student")
def get_student():
    """Show information about a student."""

    # args.get gets value of key 'github', and if the key doesn't exist, returns 'jhacks'.
    student_github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(student_github)
    html = render_template("student_info.html", github=github, first=first, last=last)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")



@app.route("/add-new-student")
def add_new_student():
    """A form for adding new students to database."""
    


    return render_template("new_student.html")





if __name__ == "__main__":
    app.run(debug=True)