import sys
import os

# Add the python-flask directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'python-flask'))

print("Testing Flask app...")
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")

try:
    from flask import Flask
    print("✓ Flask imported")
    from flask_cors import CORS
    print("✓ flask_cors imported")
    import random
    print("✓ random imported")
    
    # Now try to import the app
    os.chdir(os.path.join(os.path.dirname(__file__), 'python-flask'))
    print(f"Changed to: {os.getcwd()}")
    
    from app import app
    print("✓ App imported successfully")
    
    # Try to run the app
    print("\nStarting Flask server on http://localhost:5000")
    print("Press Ctrl+C to stop")
    app.run(debug=True, port=5000, host='0.0.0.0')
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()

