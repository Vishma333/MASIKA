from flask import Flask, render_template, request, send_from_directory
import pandas as pd
import os
from datetime import datetime

# Initialize the app
app = Flask(__name__)

# Name of the Excel file
EXCEL_FILE = 'masika_feedback.xlsx'

def save_to_excel(data):
    """
    Saves dictionary data to an Excel file.
    """
    # Create a DataFrame from the incoming data (wrapping in list)
    new_entry = pd.DataFrame([data])
    
    # Check if the file already exists
    if not os.path.exists(EXCEL_FILE):
        # Create new file with the data
        new_entry.to_excel(EXCEL_FILE, index=False, engine='openpyxl')
    else:
        # Load existing file
        existing_df = pd.read_excel(EXCEL_FILE)
        # Combine old data with new data
        updated_df = pd.concat([existing_df, new_entry], ignore_index=True)
        # Save back to Excel
        updated_df.to_excel(EXCEL_FILE, index=False, engine='openpyxl')

# Route for the Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route for Serving manifest.json (Added for PWA functionality)
@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory('static', 'manifest.json')

# Route for Coming Soon Page (Added for redirection)
@app.route('/comingsoon.html')
def coming_soon():
    return render_template('comingsoon.html')

# --- Routes for Team Member Pages ---
@app.route('/tapaswinipadhi.html')
def tapaswini():
    return render_template('tapaswinipadhi.html')

@app.route('/vishmapasayat.html')
def vishma():
    return render_template('vishmapasayat.html')

@app.route('/amritasaini.html')
def amrita():
    return render_template('amritasaini.html')

@app.route('/paramjeetsingh.html')
def paramjeet():
    return render_template('paramjeetsingh.html')

@app.route('/bikramadityadas.html')
def bikramaditya():
    return render_template('bikramadityadas.html')

@app.route('/sharmilapradhan.html')
def sharmila():
    return render_template('sharmilapradhan.html')

# Route for Handling the Form
@app.route('/contact', methods=['POST'])
def contact_submit():
    try:
        # 1. Get data from the HTML form based on the 'name' attributes
        identity = request.form.get('identity')  # Name
        email = request.form.get('email')        # Signal / Email
        frequency = request.form.get('frequency')# Contact Frequency
        transmission = request.form.get('message') # Transmission Data (Message)
        
        # 2. Prepare data dictionary with a timestamp
        data = {
            'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'Identity (Name)': identity,
            'Email/Signal': email,
            'Contact Frequency': frequency,
            'Transmission Data (Message)': transmission
        }
        
        # 3. Save to Excel
        save_to_excel(data)
        
        print("✅ Data successfully saved to Excel.")
        
        # 4. Render template with a success flag
        return render_template('index.html', success=True)
        
    except PermissionError:
        # This happens if the Excel file is currently OPEN on your computer
        return "Error: Please close 'masika_feedback.xlsx' and try again."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)