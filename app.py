
from flask import Flask, render_template, request, redirect, url_for

from database import add_expense, view_expenses

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        amount = float(request.form["amount"])
        category = request.form["category"]

        add_expense(name, amount, category)

        return redirect(url_for("home"))

    saved_expenses = view_expenses()

    total = sum(expense[2] for expense in saved_expenses)

    category_totals = {}

    for expense in saved_expenses:
        category = expense[3]
        amount = expense[2]

        category_totals[category] = category_totals.get(category, 0) + amount

    return render_template(
        "index.html",
        expenses=saved_expenses,
        total=total,
        category_totals=category_totals
    )


if __name__ == "__main__":
    app.run(debug=True)
