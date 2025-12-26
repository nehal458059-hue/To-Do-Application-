app = Flask(
__ 
name
__ )
def get_db_connection():
return sqlite3.connect('students.db')
@app . route('/')
def index():
conn = get
_db_
connection()
students = conn . execute('SELECT * FROM
students') .fetchall()
conn.close()
return render
_
template('index.html',
students=students)
@app . route('/add', methods=['POST'])
def add_student():
data = (
request.form['name'],
request.form['roll'],
request.form['department'],
request.form['email'],
request.form['phone']
)
conn = get
_db_
connection()
conn.execute(
