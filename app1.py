from flask import Flask, jsonify, render_template, request, redirect, url_for, session 

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for sessions

# Simulated database
users_db = {}

# 1. Start by showing Registration page
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if not full_name or not username or not email or not password:
            return "All fields are required."

        if username in users_db:
            return "Username already exists. Please try another."

        users_db[username] = {'full_name': full_name, 'email': email, 'password': password}
        
        # Redirect to login page after successful registration
        return redirect(url_for('login'))  # Redirect to login after registration

    return render_template('registration.html')  # Show registration page


# 2. After Registration → Go to Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = users_db.get(username)

        if user and user['password'] == password:
            session['username'] = username
            return redirect(url_for('home'))  # Login successful → Go to Home
        else:
            return "Wrong username or password."  # Error handling for invalid login.

    return render_template('login.html')  # Show login page


# 3. After Login → Show Home Page
@app.route('/home')
def home():
    if 'username' in session:
        return render_template('index.html')  # Show home page if logged in
    else:
        return redirect(url_for('login'))  # Redirect to login page if not logged in


@app.route('/about1.html')
def about():
    return render_template('about1.html')

# Menu page
@app.route('/menu2.html')
def menu():
    return render_template('menu2.html')

# Product page
@app.route('/coffeemenu.html')
def product():
    return render_template('coffeemenu.html')

# Review page
@app.route('/review.html')
def review():
    return render_template('review.html')

# Contact page (Save data)
@app.route('/contact2.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        print(f"New contact: {name}, {email}, {message}")

        return jsonify({"status": "success", "message": "Thank you for contacting us!"})
    return render_template('contact2.html')

# More page
@app.route('/more.html')
def more():
    return render_template('more.html')

# Order page
@app.route('/ordernow.html', methods=['GET', 'POST'])
def order():
    # If it's a GET request, just render the order page
    if request.method == 'GET':
        return render_template('ordernow.html')

    # If it's a POST request, handle placing the order
    if request.method == 'POST':
        # Example: You can retrieve the order data here (could be passed via form data or JSON)
        order_items = request.form.getlist('items')  # Or you could pass this as a JSON object
        
        if order_items:
            # Process the order (e.g., save it to a database, send a confirmation email, etc.)
            return jsonify({"status": "success", "message": "Your order has been placed!"})
        else:
            return jsonify({"status": "error", "message": "No items selected. Please add items to your order."})
if __name__ == "__main__":
    app.run(debug=True)

