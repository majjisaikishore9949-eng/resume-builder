from flask import Flask, request, jsonify, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'  # Replace with a secure key

USERNAME = "user123"
PASSWORD = "pass123"

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("username") == USERNAME and request.form.get("password") == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            error = "Invalid username or password. Try again."
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

def render_resume_html(data):
    # Generate HTML for preview, used by generate_ai_resume route
    template = data.get('template', 'classic')
    name = data.get('name', '')
    email = data.get('email', '')
    phone = data.get('phone', '')
    address = data.get('address', '')
    linkedin = data.get('linkedin', '')
    website = data.get('website', '')
    objective = data.get('objective', '')
    education = data.get('education', '')
    certifications = data.get('certifications', '')
    skills = data.get('skills', '')
    experience = data.get('experience', '')
    languages = data.get('languages', '')
    hobbies = data.get('hobbies', '')
    references = data.get('references', '')

    if template == 'modern':
        html = f"""
        <div style='font-family:Arial,sans-serif;font-size:17px;'>
            <h2 style='color:#2255a4'>{name}</h2>
            <p><b>Email:</b> {email} | <b>Phone:</b> {phone} | <b>LinkedIn:</b> {linkedin}</p>
            <p><b>Address:</b> {address}</p>
            <hr />
            <h3>Objective</h3><p>{objective}</p>
            <h3>Education</h3><p>{education}</p>
            <h3>Certifications</h3><p>{certifications}</p>
            <h3>Skills</h3><p>{skills}</p>
            <h3>Experience</h3><p>{experience}</p>
            <h3>Languages</h3><p>{languages}</p>
            <h3>Hobbies / Interests</h3><p>{hobbies}</p>
            <h3>References</h3><p>{references}</p>
            <div>Portfolio: {website}</div>
        </div>
        """
    elif template == 'colorful':
        html = f"""
        <div style='font-family:"Segoe UI",sans-serif;font-size:17px;background:linear-gradient(135deg,#11cb77 0%,#ff3c61 100%);color:#fff;padding:25px;border-radius:18px;'>
            <h2 style='color:#fff;'>{name}</h2>
            <div><b>Email:</b> {email} <b>Phone:</b> {phone}</div>
            <div><b>LinkedIn:</b> {linkedin} | <b>Website:</b> {website}</div>
            <div><b>Address:</b> {address}</div>
            <hr style='border:1.5px solid #fff;' />
            <h3>Objective</h3><p>{objective}</p>
            <h3>Education</h3><p>{education}</p>
            <h3>Certifications</h3><p>{certifications}</p>
            <h3>Skills</h3><p>{skills}</p>
            <h3>Experience</h3><p>{experience}</p>
            <h3>Languages</h3><p>{languages}</p>
            <h3>Hobbies / Interests</h3><p>{hobbies}</p>
            <h3>References</h3><p>{references}</p>
        </div>
        """
    else:  # classic
        html = f"""
        <div style='font-family:serif;font-size:16px;padding:10px;'>
            <h2>{name}</h2>
            <p><b>Email:</b> {email}</p>
            <p><b>Phone:</b> {phone}</p>
            <p><b>LinkedIn:</b> {linkedin}</p>
            <p><b>Website:</b> {website}</p>
            <p><b>Address:</b> {address}</p>
            <hr />
            <h3>Objective</h3><p>{objective}</p>
            <h3>Education</h3><p>{education}</p>
            <h3>Certifications</h3><p>{certifications}</p>
            <h3>Skills</h3><p>{skills}</p>
            <h3>Experience</h3><p>{experience}</p>
            <h3>Languages</h3><p>{languages}</p>
            <h3>Hobbies / Interests</h3><p>{hobbies}</p>
            <h3>References</h3><p>{references}</p>
        </div>
        """
    return html

@app.route('/generate_ai_resume', methods=['POST'])
def generate_ai_resume():
    if not session.get('logged_in'):
        return jsonify({"resume": "<div>Please login first.</div>"})
    data = request.json
    html_content = render_resume_html(data)
    return jsonify({"resume": html_content})

if __name__ == "__main__":
    app.run(debug=True)
