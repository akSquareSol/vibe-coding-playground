import sys
import os

os.chdir(r'C:\Users\anuna\Downloads\Project\vibe-coding-playground\python-flask')

try:
    print("Step 1: Importing Flask...")
    from flask import Flask, jsonify, request, render_template
    print("✓ Flask imported")
    
    print("Step 2: Importing CORS...")
    from flask_cors import CORS
    print("✓ CORS imported")
    
    print("Step 3: Importing random...")
    import random
    print("✓ random imported")
    
    print("Step 4: Creating Flask app...")
    app = Flask(__name__)
    CORS(app)
    print("✓ App created")
    
    print("Step 5: Defining routes...")
    
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/api/hello')
    def hello():
        return jsonify({'message': 'Hello from Flask! 🐍', 'status': 'success'})
    
    print("✓ Routes defined")
    
    print("\n" + "="*50)
    print("All checks passed! The Flask app should work.")
    print("="*50)
    print("\nTo run the Flask app:")
    print("  cd python-flask")
    print("  python app.py")
    print("\nOr from the root directory:")
    print("  python python-flask/app.py")
    
except Exception as e:
    print(f"\n✗ Error at current step: {e}")
    import traceback
    traceback.print_exc()

