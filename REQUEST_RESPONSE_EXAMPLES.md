# Request/Response Examples

## Resume Analysis Endpoint

### Request
```bash
POST /analyze
Content-Type: multipart/form-data

file: resume.pdf
job_description: "Senior Python Developer..."
```

### Response
```json
{
  "status": "success",
  "request_id": "req_abc123xyz",
  "data": {
    "match_score": 0.85,
    "skills": {
      "matched": ["Python", "Flask", "PostgreSQL"],
      "missing": ["Go", "Rust"],
      "technical_score": 0.9
    },
    "experience": {
      "years": 5,
      "relevant_years": 4,
      "alignment": "high"
    },
    "recommendations": [
      "Add more cloud platform experience",
      "Include containerization skills"
    ]
  },
  "metadata": {
    "processing_time_ms": 245,
    "version": "v2"
  }
}
```

## Health Check Endpoint

### Request
```bash
GET /health
```

### Response
```json
{
  "status": "healthy",
  "timestamp": "2026-02-02T10:30:00Z",
  "components": {
    "database": "ok",
    "cache": "ok",
    "storage": "ok"
  },
  "metrics": {
    "uptime_seconds": 86400,
    "requests_total": 10000,
    "errors_total": 12
  }
}
```

## Batch Processing Endpoint

### Request
```bash
POST /batch/analyze
Content-Type: application/json

{
  "resumes": [
    {"id": 1, "file": "resume1.pdf"},
    {"id": 2, "file": "resume2.pdf"}
  ],
  "job_description": "Job details...",
  "callback_url": "https://example.com/callback"
}
```

### Response
```json
{
  "status": "processing",
  "batch_id": "batch_def456",
  "total_items": 2,
  "estimated_time_seconds": 30,
  "status_url": "/batch/status/batch_def456"
}
```

## Error Response

### Response
```json
{
  "status": "error",
  "error_code": "INVALID_FILE",
  "message": "Uploaded file is not a valid PDF",
  "request_id": "req_xyz789",
  "timestamp": "2026-02-02T10:30:00Z"
}
```

## Pagination Example

### Request
```bash
GET /analyses?page=2&per_page=20&sort=created_at&order=desc
```

### Response
```json
{
  "status": "success",
  "data": [
    {
      "id": "analysis_001",
      "resume_name": "john_doe.pdf",
      "job_title": "Senior Developer",
      "match_score": 0.88,
      "created_at": "2026-02-01T15:30:00Z"
    }
  ],
  "pagination": {
    "page": 2,
    "per_page": 20,
    "total": 152,
    "total_pages": 8,
    "has_next": true,
    "has_prev": true
  }
}
```
