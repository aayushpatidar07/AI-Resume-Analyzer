# API Documentation

## Overview
The AI Resume Analyzer & Job Matcher is a Flask-based REST API that analyzes resumes and matches them with job descriptions to determine skill alignment.

## Base URL
```
http://127.0.0.1:5000
```

## Endpoints

### 1. Home Page
**GET** `/`

Returns the web interface for the application.

**Response:**
- Status: 200 OK
- Content-Type: text/html

---

### 2. Analyze Resume
**POST** `/analyze`

Analyzes a resume against a job description and returns skill matching results.

**Request Format:**
- Content-Type: multipart/form-data

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| resume | file | Yes | PDF file of the resume (max 16MB) |
| job_description | string | Yes | Job description text (min 10 characters) |

**Example cURL:**
```bash
curl -X POST http://127.0.0.1:5000/analyze \
  -F "resume=@resume.pdf" \
  -F "job_description=Senior Python Developer with 5+ years experience..."
```

**Success Response (200):**
```json
{
  "success": true,
  "match_percentage": 85.5,
  "match_level": "Excellent",
  "matched_skills": ["python", "flask", "sql", "docker"],
  "missing_skills": ["kubernetes", "aws"],
  "resume_skills_count": 12,
  "required_skills_count": 14,
  "matched_count": 12,
  "missing_count": 2
}
```

**Error Response (400/500):**
```json
{
  "success": false,
  "error": "Error message describing what went wrong"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 400 | Bad request (missing fields, invalid file type, etc.) |
| 413 | Payload too large (file exceeds 16MB) |
| 500 | Server error |

---

### 3. Sample Data
**GET** `/api/sample-data`

Returns sample job description for testing purposes.

**Response:**
```json
{
  "sample_job_description": "Senior Full Stack Developer...\n..."
}
```

---

## Match Levels

The match percentage is categorized into levels:

| Level | Range | Description |
|-------|-------|-------------|
| Excellent | 80-100% | Strong match, candidate well-qualified |
| Good | 60-79% | Good match, candidate qualified with some gaps |
| Fair | 40-59% | Moderate match, candidate may need upskilling |
| Poor | 0-39% | Poor match, significant skill gaps |

---

## Error Handling

All errors are returned with proper HTTP status codes and descriptive messages:

```json
{
  "success": false,
  "error": "No resume file provided"
}
```

Common errors:
- `No resume file provided` - Resume file is missing
- `No job description provided` - Job description is empty
- `Only PDF files are allowed` - File must be PDF format
- `File size exceeds maximum limit` - File is larger than 16MB
- `Failed to parse resume` - PDF could not be read
- `No recognized skills found` - No skills detected in input

---

## Rate Limiting (Planned)
API rate limiting to be implemented. Current limits:
- No rate limiting active

---

## Authentication (Planned)
Authentication support to be added in future versions.

---

## Examples

### Python Example
```python
import requests

url = 'http://127.0.0.1:5000/analyze'
files = {'resume': open('resume.pdf', 'rb')}
data = {'job_description': 'Senior Python Developer...'}

response = requests.post(url, files=files, data=data)
result = response.json()

print(f"Match: {result['match_percentage']}%")
print(f"Level: {result['match_level']}")
```

### JavaScript Example
```javascript
const formData = new FormData();
formData.append('resume', fileInput.files[0]);
formData.append('job_description', jobDescription);

fetch('/analyze', {
  method: 'POST',
  body: formData
})
.then(res => res.json())
.then(data => {
  console.log(`Match: ${data.match_percentage}%`);
  console.log(`Matched Skills: ${data.matched_skills.join(', ')}`);
});
```

---

## Version
API Version: 1.0.0

Last Updated: 2026-01-24
