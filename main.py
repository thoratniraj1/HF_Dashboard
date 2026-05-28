from flask import Flask, jsonify, request
from models import User
from db_connection import SessionLocal

# Create Flask app instance
app = Flask(__name__)

# Define route
@app.route('/')
def home():
    return "Hello, World! Welcome to Flask."

@app.route('/homepage')
def homepage():
    return "Welcome to homepage."

@app.route('/patents')
def patents():
    return {'message':"patents retrived successfully."}

# Add User API
@app.route('/add-user', methods=['POST'])
def add_user():

    db = SessionLocal()

    try:
        # Get JSON data from request
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        # Basic validation
        if not all([name, email, password]):
            return jsonify({
                "error": "Name, email and password required"
            }), 400

        # Check if user already exists
        existing_user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if existing_user:
            return jsonify({
                "error": "Email already exists"
            }), 409

        # Create user object
        new_user = User(
            name=name,
            email=email,
            password=password
        )

        # Add to DB
        db.add(new_user)

        # Commit transaction
        db.commit()

        # Refresh object to get generated ID
        db.refresh(new_user)

        return jsonify({
            "message": "User added successfully",
            "user_id": new_user.id
        }), 201

    except Exception as e:

        db.rollback()

        return jsonify({
            "error": str(e)
        }), 500

    finally:
        db.close()

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):

    db = SessionLocal()

    try:

        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            return jsonify({
                "error": "User not found"
            }), 404

        db.delete(user)
        db.commit()

        return jsonify({
            "message": "User deleted"
        })

    except Exception as e:

        db.rollback()

        return jsonify({
            "error": str(e)
        }), 500

    finally:
        db.close()

# Run application
if __name__ == '__main__':
    app.run(debug=True)