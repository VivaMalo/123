from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

# Глобальный список истории
calc_history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user_id' not in session:
        return redirect('/login')
    
    result = None
    if request.method == 'POST':
        try:
            n1 = float(request.form.get('n1'))
            n2 = float(request.form.get('n2'))
            op = request.form.get('op')
            
            if op == '+': result = n1 + n2
            elif op == '-': result = n1 - n2
            elif op == '*': result = n1 * n2
            elif op == '/': result = n1 / n2 if n2 != 0 else "Ошибка (на 0 нельзя)"
            
            if isinstance(result, (int, float)):
                entry = f"{session['username']}: {n1} {op} {n2} = {result}"
                calc_history.insert(0, entry)
        except:
            result = "Ошибка ввода"
            
    return render_template('index.html', result=result, history=calc_history, username=session['username'])

@app.route('/clear')
def clear_history():
    calc_history.clear()
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_pw = generate_password_hash(password)
        try:
            new_user = User(username=username, password=hashed_pw)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        except:
            return "Пользователь уже существует! <a href='/register'>Назад</a>"
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user and check_password_hash(user.password, request.form.get('password')):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect('/')
        return "Неверные данные! <a href='/login'>Назад</a>"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
