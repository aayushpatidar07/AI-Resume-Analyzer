# AI Resume Analyzer & Job Matcher - Copilot Instructions

## Project Overview
A Flask web application that analyzes PDF resumes and matches them against job descriptions using keyword-based NLP skill extraction. Three-layer architecture: presentation (HTML/CSS/JS) → Flask application → business logic utilities.

## Architecture & Data Flow

**Core Pipeline:**
1. User uploads PDF resume + job description via frontend form
2. `app.py` validates inputs and calls processing utilities
3. `resume_parser.py` extracts & cleans PDF text
4. `skill_extractor.py` identifies skills from both documents (shared TECHNICAL_SKILLS database)
5. `matcher.py` calculates match percentage and identifies gaps
6. Results returned as JSON, displayed in real-time UI

**File Organization:**
- **`app.py`** (237 lines): Flask app, routes (`/`, `/analyze`, `/api/sample-data`), error handlers, file handling
- **`config.py`** (316 lines): Centralized settings (Flask config, file limits, skill extraction tuning, matching thresholds)
- **`utils/`**: Core business logic - keep stateless, focused responsibilities
  - `resume_parser.py`: PDF text extraction + text normalization (regex-based cleaning)
  - `skill_extractor.py`: Keyword matching against TECHNICAL_SKILLS set (150+ skills across 13 categories)
  - `matcher.py`: Set operations for skill comparison, match percentage calculation
- **`templates/index.html`**: Single-page form + results display (Bootstrap 5)
- **`static/script.js`**: API calls via `fetch()`, DOM manipulation, error handling

## Key Patterns & Conventions

### Error Handling
- **Validation-first approach**: Check inputs before processing (in app.py routes)
- **Structured JSON responses**: `{"success": bool, "error": str|null, ...}`
- **Exception catching in utilities**: Raise descriptive exceptions from utils; app.py handles logging
- **Common validations**: File type (PDF only), size (16MB max), text length (10+ chars for job desc)

### Text Processing Pipeline
1. **extraction** → raw text from PyPDF2
2. **cleaning** → lowercase, remove special chars, normalize whitespace (see `resume_parser.clean_text()`)
3. **skill extraction** → case-insensitive keyword matching against config database
4. **comparison** → set intersection/difference for matching logic

### Configuration Management
- All settings in `config.py` - no hardcoded values in business logic
- Key tuning knobs:
  - `MAX_SKILLS_TO_RETURN`: Limit results (None = no limit)
  - `MATCH_LEVEL_THRESHOLDS`: Dictionary mapping label to percentage (e.g., "Excellent Match" → 80%)
  - `PDF_EXTRACTION_METHOD`: Currently 'text' (future: 'ocr')
- Skills database is class variable `SkillExtractor.TECHNICAL_SKILLS` (set, not list)

### Type Hints
- All utility functions use type hints (e.g., `extract_keywords(text: str) -> Set[str]`)
- Keep Dict/List/Set types explicit for clarity

### Logging
- Use Python `logging` module (not print statements)
- Configured in app.py: `logging.basicConfig()` + logger per module
- LOG_LEVEL and LOG_FILE in config.py

## Development Workflows

### Running Locally
```bash
# Windows PowerShell (recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py  # Runs on http://127.0.0.1:5000
```

### Adding New Skills
- Edit `SkillExtractor.TECHNICAL_SKILLS` set in `utils/skill_extractor.py`
- Format: single quotes, lowercase, comma-separated
- Grouped by category (Programming Languages, Web Dev, Databases, etc.)

### Modifying Matching Logic
- Match percentage: `matcher.py` → `calculate_match_percentage()`
- Match level labels: `config.py` → `MATCH_LEVEL_THRESHOLDS`
- If changing algorithm: update docstrings explaining the calculation method

### Testing
- See `TESTING_GUIDE.md` for manual test procedures
- Tests folder exists but minimal (future expansion area)
- Key test scenarios: invalid PDF, empty job desc, no matching skills, 100% match

## External Dependencies
- **Flask 3.0.0**: Web framework, routing, file handling
- **PyPDF2 3.0.1**: PDF text extraction (used in resume_parser)
- **Werkzeug 3.0.1**: WSGI utilities, secure_filename()
- **python-dotenv 1.0.0**: Environment variable loading (if .env exists)

## Common Pitfalls to Avoid
1. **Modifying skill extraction within app.py** - Keep logic in `SkillExtractor` class for reusability
2. **Hardcoding file paths** - Use `config.UPLOAD_FOLDER` and `os.path.join()`
3. **Forgetting secure_filename()** - Always use for user uploads to prevent path traversal
4. **Case sensitivity** - Skills are matched lowercase; ensure cleaning step is applied consistently
5. **Unbounded skill results** - Use `MAX_SKILLS_TO_RETURN` config to prevent performance issues

## File Upload Handling
- Max size enforced via `app.config['MAX_CONTENT_LENGTH'] = 16MB`
- Temporary files stored in `uploads/` folder (auto-created if missing)
- Filename format: `{timestamp}_{original_name}.pdf` (prevents collisions)
- Auto-delete enabled via `AUTO_DELETE_UPLOADS` config (production security)
- Only `.pdf` extension allowed; validation with `allowed_file()` + MIME type checking recommended

## When Adding Features
- **New endpoints**: Add to app.py with clear docstrings, validate inputs first
- **New utils**: Create stateless class methods (no instance state); use type hints
- **UI changes**: Modify templates/index.html and static/script.js; test responsive design (Bootstrap classes)
- **Config additions**: Always add to config.py with comments explaining purpose
