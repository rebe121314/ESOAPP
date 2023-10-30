from flask import Flask, render_template, request
from models import db, Scholarship
from flask import jsonify
import requests
from bs4 import BeautifulSoup
import openai
from flask_caching import Cache


app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    scholarship_name = request.form.get('scholarship_name')
    relevance = request.form.get('relevance')
    # Store this feedback, perhaps in a separate table or logging system
    # This data can be analyzed later to refine the search and extraction process
    return redirect('/')


cache = Cache(app, config={'CACHE_TYPE': 'simple'})
openai.api_key = 'YOUR_OPENAI_API_KEY'
GOOGLE_API_KEY = 'YOUR_GOOGLE_API_KEY'
GOOGLE_SEARCH_ENGINE_ID = 'YOUR_SEARCH_ENGINE_ID'
BING_API_KEY = 'YOUR_BING_API_KEY'

@cache.memoize(timeout=3600) 
def search_bing(query):
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    endpoint = "https://api.bing.microsoft.com/v7.0/search"
    response = requests.get(endpoint, headers=headers, params={"q": query, "count": 10, "responseFilter": "Webpages"})
    return response.json().get('webPages', {}).get('value', [])

@app.route('/search', methods=['POST'])
def search():
    keywords = request.form.get('keywords')
    min_amount = request.form.get('min_amount')
    max_amount = request.form.get('max_amount')
    deadline = request.form.get('deadline')
    citizenships = request.form.get('citizenships')
    
    # Formulate the search query
    query = f"{keywords} scholarship undergraduate -university-specific"
    google_url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={GOOGLE_SEARCH_ENGINE_ID}"
    response = requests.get(google_url)
    bing_results = search_bing(query)
    # Extract relevant information from the search results
    results = response.json().get('items', [])
    scholarships = []
    for item in results:
        soup = BeautifulSoup(item['htmlSnippet'], 'html.parser')
        snippet = soup.get_text()
        
        # Use OpenAI to extract details
        prompt = f"Extract scholarship details from: {snippet}"
        response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=100)
        details = response.choices[0].text.strip()

        # Assuming GPT-3.5 provides details in a structured format, extract and add to scholarships list
        # ... Parsing logic based on GPT-3.5 output ...

        scholarships.append({
            'name': item['title'],
            'link': item['link'],
            # ... additional fields based on GPT-3.5 output ...
        })
    
    # Store the extracted data in the database
    for scholarship in scholarships:
        new_scholarship = Scholarship(name=scholarship['name'], apply_link=scholarship['link'])
        db.session.add(new_scholarship)
    db.session.commit()

    return render_template('index.html', scholarships=scholarships)
