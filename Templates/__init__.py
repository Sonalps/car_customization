from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='.')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sonal123$'
app.config['MYSQL_DB'] = 'car_customization'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
abc={}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    cursor = mysql.connection.cursor()
    try:
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(query, (name, email))
        mysql.connection.commit()
        return 'Data submitted successfully!'
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()

@app.route('/dashboard')
def dashboard():
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT * FROM customer")
        row_headers = [x[0] for x in cursor.description]
        data = cursor.fetchall()
        json_data = []
        for result in data:
            json_data.append(dict(zip(row_headers, result)))

        return render_template('dashboard.html', data=json_data)
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    name = request.form['name']
    cursor = mysql.connection.cursor()
    try:
        query = "SELECT * FROM users WHERE email = %s AND name = %s"
        cursor.execute(query, (email, name))
        user = cursor.fetchone()
        if user:
            return 'Login successful!'
        else:
            return 'Invalid email or name'
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(debug=True)
