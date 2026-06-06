from flask import Flask, render_template_string, request
from groq import Groq

app = Flask(__name__)
client = Groq(api_key="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")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Job Posting Generator</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px; background: #f5f5f5; }
        .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        input, textarea, select { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }
        button { background: #4CAF50; color: white; padding: 15px 30px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        button:hover { background: #45a049; }
        .result { margin-top: 30px; padding: 20px; background: #f9f9f9; border-radius: 5px; white-space: pre-wrap; }
        h1 { color: #333; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 AI Job Posting Generator</h1>
        <form method="POST">
            <input type="text" name="job" placeholder="Job Title" required>
            <input type="text" name="company" placeholder="Company Name" required>
            <select name="level">
                <option>Entry Level</option>
                <option>Mid Level</option>
                <option>Senior</option>
                <option>Lead</option>
            </select>
            <textarea name="desc" placeholder="Company Description" rows="3" required></textarea>
            <button type="submit">Generate Job Posting</button>
        </form>
        {% if result %}
            <div class="result">{{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        job = request.form['job']
        company = request.form['company']
        level = request.form['level']
        desc = request.form['desc']
        
        prompt = f"Write job posting for {job} at {company}. Level: {level}. Description: {desc}"
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content
    
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True)
