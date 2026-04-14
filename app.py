from flask import Flask, render_template, request
import os 
from parser import extract_text, extract_email, extract_phone, extract_name, extract_education, extract_experience
from skills import extract_skills

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    return render_template('index.html', data=None)

@app.route('/upload', methods=['POST'])
def upload():

    if 'resume' not in request.files:
        return "No file part"
    
    file = request.files['resume']

    if file.filename == '':
        return "No file selected"
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
    file.save(filepath)

    text = extract_text(filepath)

    if text.strip() == "":
        return "Could not extract text from file"
    
    data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "skills": extract_phone(text),
        "education": extract_education(text),
        "experience": extract_experience(text)
    }

    return render_template('index.html', data=data)

if __name__ == '__main__':
     app.run(debug=True)