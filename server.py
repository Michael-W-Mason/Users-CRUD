from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)
app.secret_key = "as;diujasdnbvpiausdfhva"

@app.route("/")
def main():
    users = User.get_all()
    return render_template("read.html", users=users)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    new_user_data = {
        "first_name" : request.form["firstname"],
        "last_name" : request.form["lastname"],
        "email" : request.form["email"]
    }
    User.create_new(new_user_data)
    user = User.get_last_one()
    user_id = user["id"]
    return redirect(f"/read_one/{ user_id }")

@app.route("/read_one/<int:id>")
def read_one(id):
    user = User.get_one(id)
    print(user)
    return render_template("read(one).html", user=user)

@app.route("/edit/<int:id>")
def edit_one(id):
    user = User.get_one(id)
    return render_template("edit.html", user=user)

@app.route("/edit_complete/<int:id>", methods=["POST"])
def edit_complete(id):
    new_user_data = {
        "first_name" : request.form["firstname"],
        "last_name" : request.form["lastname"],
        "email" : request.form["email"],
        "id" : id
    }
    User.edit_one(new_user_data)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    User.delete_one(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)