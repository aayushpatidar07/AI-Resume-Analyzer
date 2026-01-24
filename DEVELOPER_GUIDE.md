# Developer Guide

## Project Architecture

```
AI Resume Analyzer & Job Matcher
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── static/
│   ├── script.js         # Frontend JavaScript
│   └── style.css         # Frontend styling
├── templates/
│   └── index.html        # HTML template
├── uploads/              # Resume upload directory
├── routes/
│   └── api_v2.py         # API v2 endpoints
└── utils/
    ├── __init__.py
    ├── cache.py          # Caching utilities
    ├── config.py         # Configuration management
    ├── constants.py      # Application constants
    ├── database.py       # Database operations
    ├── decorators.py     # Utility decorators
    ├── exceptions.py     # Custom exceptions
    ├── helpers.py        # Helper functions
    ├── logger.py         # Logging setup
    ├── matcher.py        # Resume-job matching
    ├── models.py         # Data models
    ├── performance.py    # Performance monitoring
    ├── resume_parser.py  # PDF parsing
    ├── response.py       # API response formatting
    ├── security.py       # Security utilities
    ├── skill_extractor.py # Skill extraction
    ├── test_utils.py     # Testing utilities
    └── validation.py     # Input validation
```

## Development Setup

### Prerequisites
- Python 3.8+
- pip or poetry
- Git

### Initial Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aayushpatidar07/AI-Resume-Analyzer.git
   cd AI-Resume-Analyzer
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

Visit `http://127.0.0.1:5000`

## Module Guide

### Core Modules

#### `resume_parser.py`
Handles PDF resume parsing and text extraction.

**Key Methods:**
- `extract_text(file_path)` - Extract text from PDF
- `clean_text(text)` - Clean and normalize text
- `parse_resume(file_path)` - Full parsing workflow

#### `skill_extractor.py`
Extracts technical skills from text.

**Key Methods:**
- `extract_keywords(text)` - Find skills via keyword matching
- `extract_from_resume(text)` - Extract resume skills
- `extract_from_job_description(text)` - Extract job skills

#### `matcher.py`
Matches resume skills with job requirements.

**Key Methods:**
- `match_resume(resume_skills, job_skills)` - Complete matching
- `calculate_match_percentage()` - Calculate match %
- `get_matched_skills()` - Find common skills
- `get_missing_skills()` - Find missing skills

### Utility Modules

#### `logger.py`
Centralized logging configuration.

```python
from utils.logger import get_logger
logger = get_logger(__name__)
logger.info("Message")
```

#### `cache.py`
In-memory caching with TTL.

```python
from utils.cache import cache_result

@cache_result(ttl=300)
def expensive_function():
    return result
```

#### `security.py`
Security-related utilities.

```python
from utils.security import PasswordManager

hash, salt = PasswordManager.hash_password(password)
verified = PasswordManager.verify_password(password, hash, salt)
```

#### `performance.py`
Performance monitoring and profiling.

```python
from utils.performance import measure_performance

@measure_performance
def my_function():
    pass
```

## Testing

### Running Tests
```bash
pytest
```

### Writing Tests
```python
from utils.test_utils import TestDataGenerator

def test_skill_extraction():
    resume = TestDataGenerator.create_sample_resume_text()
    # Test your code
```

## Code Standards

### Style
- Follow PEP 8
- Use type hints
- Write docstrings

### Example:
```python
def extract_skills(text: str, min_length: int = 2) -> List[str]:
    """
    Extract skills from text.
    
    Args:
        text: Input text
        min_length: Minimum skill name length
        
    Returns:
        List of extracted skills
    """
    # Implementation
    pass
```

### Commits
```
feat: add new feature
fix: fix bug
docs: update documentation
test: add tests
refactor: refactor code
```

## API Endpoints

### v1 (Current)
- `GET /` - Home page
- `POST /analyze` - Analyze resume
- `GET /api/sample-data` - Get sample data

### v2 (Development)
- `GET /api/v2/health` - Health check
- `GET /api/v2/stats` - Application stats
- `POST /api/v2/batch-analyze` - Batch analysis
- `POST /api/v2/skills/recommendations` - Skill recommendations
- `POST /api/v2/export` - Export results

## Deployment

### Local
```bash
python app.py
```

### Production
```bash
gunicorn app:app
```

### Docker (Planned)
```bash
docker build -t resume-analyzer .
docker run -p 5000:5000 resume-analyzer
```

## Troubleshooting

### Issue: Module not found
**Solution:** Ensure all dependencies are installed: `pip install -r requirements.txt`

### Issue: Port 5000 already in use
**Solution:** Change PORT in .env or use: `python app.py --port 5001`

### Issue: PDF parsing fails
**Solution:** Ensure PyPDF2 is installed: `pip install PyPDF2==3.0.1`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)
- [Python Logging](https://docs.python.org/3/library/logging.html)

---

**Last Updated:** 2026-01-24
