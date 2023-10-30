
# Scholarship Search Web Application

A web application that allows users to search for scholarships based on specific parameters. The application scrapes search results from multiple search engines, processes the data, and presents relevant scholarship opportunities to the user.

## Features:

1. **Keyword-based Search**: Users can input specific keywords to find relevant scholarships.
2. **Advanced Filters**: Users can filter scholarships based on the amount, deadline, and eligible citizenships.
3. **Feedback System**: Users can provide feedback on the relevance of the search results, helping to refine the search process.
4. **Caching**: Common queries are cached to improve response times and reduce the number of API calls.
5. **Database Storage**: Extracted scholarship data is stored in a SQLite database for easy access and retrieval.

## Setup & Installation:

### 1. Clone the Repository:

```bash
git clone [repository_url]
cd [repository_directory]
```

### 2. Set Up Virtual Environment:

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configuration:

- Update `config.py` with the necessary configurations, including API keys for search engines.
- Ensure Flask is set to run in production mode:

```bash
export FLASK_ENV=production
```

### 4. Initialize Database:

```bash
flask db init
flask db migrate
flask db upgrade
```

### 5. Run the Application:

Using Flask's development server:

```bash
flask run
```

For a more production-like setup on your local machine, use Gunicorn:

```bash
pip install gunicorn
gunicorn run:app
```

Visit `http://127.0.0.1:5000` on your browser to access the application.

## Usage:

1. Navigate to the homepage.
2. Enter your search parameters (keywords, amount range, deadline, citizenships).
3. Click "Search" to view relevant scholarship opportunities.
4. Provide feedback on the relevance of search results if desired.

## Future Improvements:

1. Integrate more search engines for comprehensive results.
2. Implement machine learning-based result ranking for better relevance.
3. Introduce user accounts for personalized search and saved results.

## Contributions:

Contributions are welcome! Please create an issue or submit a pull request.
