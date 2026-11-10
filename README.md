# Personal Expense Tracker 💰

A simple web-based application that helps users track daily expenses, monitor category-wise spending, and visualize spending patterns.

## Features

- Add expenses with a name, amount, and category.
- Automatically calculate total expenses.
- View category-wise spending summaries.
- Visualize spending using pie and bar charts.
- View complete expense history.
- Store expense records using an SQLite database.

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Chart.js

## Project Structure

```text
ExpenseTracker/
├── app.py
├── database.py
├── main.py
├── expense_list.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Installation and Setup

1. Clone this repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Enter the project folder:

```bash
cd ExpenseTracker
```

3. Create a virtual environment:

```bash
python3 -m venv .venv
```

4. Activate it:

```bash
source .venv/bin/activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
python app.py
```

7. Open http://127.0.0.1:5000 in your browser.

The SQLite database is created automatically when the application starts.

## Learning Outcomes

This project helped me gain practical experience with Python, Flask, SQLite database operations, HTML, CSS, and data visualization.

## Author

**Disha Reddy Bonthu**

[GitHub Profile](https://github.com/anonymouscodes-ai)