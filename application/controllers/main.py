from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@main_bp.route('/calculate', methods=['POST'])
@login_required
def calculate():
    from flask import jsonify, request
    try:
        expression = request.json.get('expression')
        result = str(eval(expression))  
        return jsonify({'result': result})
    except:
        return jsonify({'error': 'Invalid expression'}), 400