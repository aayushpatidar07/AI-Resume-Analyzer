# TESTING GUIDE

## Comprehensive Testing for AI Resume Analyzer & Job Matcher

This guide covers all testing scenarios and validation procedures.

---

## 🧪 Unit Testing

### Test Module 1: Resume Parser (`utils/resume_parser.py`)

#### Test 1.1: PDF Text Extraction
```python
# Create test_resume_parser.py
from utils.resume_parser import ResumeParser

def test_extract_text_from_pdf():
    """Test PDF text extraction"""
    result = ResumeParser.extract_text('path/to/test.pdf')
    assert isinstance(result, str)
    assert len(result) > 0
    print("✓ PDF text extraction works")

def test_clean_text():
    """Test text cleaning"""
    dirty_text = "  Python   Java\n\nSQL  ..."
    clean = ResumeParser.clean_text(dirty_text)
    assert '  ' not in clean  # No double spaces
    assert clean == clean.lower()  # Lowercase
    print("✓ Text cleaning works")

def test_parse_resume():
    """Test complete parsing pipeline"""
    result = ResumeParser.parse_resume('path/to/test.pdf')
    assert result['success'] == True
    assert 'raw_text' in result
    assert 'cleaned_text' in result
    print("✓ Resume parsing works")
```

### Test Module 2: Skill Extractor (`utils/skill_extractor.py`)

#### Test 2.1: Keyword Matching
```python
from utils.skill_extractor import SkillExtractor

def test_extract_keywords():
    """Test keyword skill extraction"""
    text = "I have python and javascript experience"
    skills = SkillExtractor.extract_keywords(text)
    assert 'python' in skills
    assert 'javascript' in skills
    print("✓ Keyword extraction works")

def test_case_insensitivity():
    """Test case-insensitive matching"""
    text = "PYTHON Python python PyThOn"
    skills = SkillExtractor.extract_keywords(text)
    # Should only have one entry despite multiple cases
    assert len([s for s in skills if s.lower() == 'python']) <= 1
    print("✓ Case insensitivity works")

def test_word_boundaries():
    """Test word boundary matching"""
    text = "Pythonic code is great but Python is better"
    skills = SkillExtractor.extract_keywords(text)
    assert 'python' in skills
    # 'Pythonic' should not match 'python' due to word boundaries
    print("✓ Word boundary matching works")
```

### Test Module 3: Skill Matcher (`utils/matcher.py`)

#### Test 3.1: Match Calculation
```python
from utils.matcher import SkillMatcher

def test_calculate_match_percentage():
    """Test match percentage calculation"""
    resume_skills = ['python', 'javascript', 'react']
    job_skills = ['python', 'react', 'vue', 'angular']
    
    percentage = SkillMatcher.calculate_match_percentage(
        resume_skills, job_skills
    )
    
    # 2 matches out of 4 required = 50%
    assert percentage == 50.0
    print("✓ Match percentage calculation works")

def test_matched_skills():
    """Test matched skills extraction"""
    resume_skills = ['python', 'flask', 'sql']
    job_skills = ['python', 'django', 'sql', 'mongodb']
    
    matched = SkillMatcher.get_matched_skills(resume_skills, job_skills)
    assert 'python' in matched
    assert 'sql' in matched
    assert 'flask' not in matched
    print("✓ Matched skills extraction works")

def test_missing_skills():
    """Test missing skills extraction"""
    resume_skills = ['python', 'flask']
    job_skills = ['python', 'react', 'aws']
    
    missing = SkillMatcher.get_missing_skills(resume_skills, job_skills)
    assert 'react' in missing
    assert 'aws' in missing
    assert 'python' not in missing
    print("✓ Missing skills extraction works")

def test_match_level_classification():
    """Test match level classification"""
    assert SkillMatcher.get_match_level(90) == "Excellent Match"
    assert SkillMatcher.get_match_level(70) == "Good Match"
    assert SkillMatcher.get_match_level(50) == "Fair Match"
    assert SkillMatcher.get_match_level(30) == "Poor Match"
    assert SkillMatcher.get_match_level(10) == "Very Poor Match"
    print("✓ Match level classification works")
```

---

## 🌐 Integration Testing

### Test 1: Complete Analysis Flow

#### Scenario 1.1: Perfect Match
```
Resume Skills: Python, Flask, PostgreSQL, Docker, AWS, Git, REST APIs
Job Skills: Python, Flask, PostgreSQL, Docker, AWS, Git, REST APIs

Expected Result:
- Match Percentage: 100%
- Match Level: Excellent Match
- Matched: All 7 skills
- Missing: 0 skills
```

#### Scenario 1.2: Partial Match
```
Resume Skills: Python, Java, SQL, Git
Job Skills: Python, React, Node.js, MongoDB

Expected Result:
- Match Percentage: 25%
- Match Level: Very Poor Match
- Matched: 1 skill (Python)
- Missing: 3 skills (React, Node.js, MongoDB)
```

#### Scenario 1.3: High Match
```
Resume Skills: Python, Flask, Django, PostgreSQL, MongoDB, Docker, AWS, Git
Job Skills: Python, Flask, PostgreSQL, Docker, AWS, React

Expected Result:
- Match Percentage: 83.33%
- Match Level: Excellent Match
- Matched: 5 skills
- Missing: 1 skill (React)
```

---

## 📋 Functional Testing

### Test Section 1: File Upload

#### Test 1.1: Valid PDF Upload
- [ ] Upload valid PDF file
- [ ] File accepted without error
- [ ] Filename displayed correctly
- [ ] No file error message shown

#### Test 1.2: Invalid File Type
- [ ] Try uploading .doc file
- [ ] Error message: "Only PDF files are allowed"
- [ ] File not accepted

#### Test 1.3: File Size Validation
- [ ] Upload file > 16MB
- [ ] Error message: "File size exceeds maximum limit (16MB)"
- [ ] File not accepted

#### Test 1.4: Empty File Selection
- [ ] Click submit without file
- [ ] Error message: "No resume file selected"
- [ ] Form not submitted

### Test Section 2: Job Description Input

#### Test 2.1: Valid Job Description
- [ ] Enter job description > 10 characters
- [ ] Form accepts input
- [ ] No error message shown

#### Test 2.2: Empty Job Description
- [ ] Submit form without job description
- [ ] Error message: "No job description provided"
- [ ] Form not submitted

#### Test 2.3: Short Job Description
- [ ] Enter < 10 characters
- [ ] Error message: "Job description must be at least 10 characters"
- [ ] Form not submitted

#### Test 2.4: Very Long Job Description
- [ ] Enter 10,000+ character job description
- [ ] System accepts and processes
- [ ] Results display correctly

### Test Section 3: Analysis Results

#### Test 3.1: Results Display
- [ ] Match percentage displays correctly
- [ ] Progress bar animates to correct percentage
- [ ] Match level label displays
- [ ] Statistics boxes show correct counts

#### Test 3.2: Skill Badges
- [ ] Matched skills show with green background
- [ ] Missing skills show with red background
- [ ] Skill names properly capitalized
- [ ] Icons display correctly

#### Test 3.3: No Results Condition
- [ ] Upload resume with no recognizable skills
- [ ] Show appropriate error message
- [ ] Guide user to try different resume

---

## 🎨 UI/UX Testing

### Test 1: Responsive Design

#### Desktop (1920x1080)
- [ ] Layout displays correctly
- [ ] All buttons and inputs visible
- [ ] No horizontal scroll needed
- [ ] Images load properly

#### Tablet (768x1024)
- [ ] Content adapts to width
- [ ] Buttons are touch-friendly
- [ ] Text is readable
- [ ] Spacing is appropriate

#### Mobile (375x667)
- [ ] Single column layout
- [ ] Full width inputs
- [ ] Large touch targets
- [ ] Scrolling works smoothly

### Test 2: Form Interaction

#### Test 2.1: Focus States
- [ ] Inputs show focus ring when tabbed
- [ ] Submit button highlights on hover
- [ ] All interactive elements are keyboard accessible

#### Test 2.2: Form Validation
- [ ] Client-side validation works
- [ ] Error messages appear immediately
- [ ] Form can be reset and reused

#### Test 2.3: Loading State
- [ ] Loading spinner displays during analysis
- [ ] Submit button is disabled during processing
- [ ] Cannot submit multiple times

### Test 3: Color & Contrast

#### Test 3.1: Accessibility
- [ ] Text has sufficient contrast (WCAG AA)
- [ ] Color is not sole method of information
- [ ] Green/red skills are distinguishable
- [ ] Icons have descriptive text

### Test 4: Navigation

#### Test 4.1: Page Flow
- [ ] Can load page in any browser
- [ ] Back button works correctly
- [ ] Links work as expected
- [ ] New Analysis button resets form

---

## 🔒 Security Testing

### Test 1: File Upload Security

#### Test 1.1: Malicious File Upload
```
Attempts:
- Upload executable file (.exe)
- Upload script file (.js)
- Upload hidden file
Expected: All rejected with error
```

#### Test 1.2: Path Traversal
```
Filename: ../../../etc/passwd.pdf
Expected: Filename sanitized, prevented
```

#### Test 1.3: File Overwrite
```
Attempt: Upload files with duplicate names
Expected: Files stored with unique names, no overwrite
```

### Test 2: Input Validation

#### Test 2.1: XSS Prevention
```javascript
Payload: <script>alert('XSS')</script>
In: Job description field
Expected: Script not executed, text displayed as-is
```

#### Test 2.2: SQL Injection
```sql
Payload: '; DROP TABLE users;--
In: Job description (if DB used)
Expected: Treated as plain text, not executed
```

### Test 3: API Security

#### Test 3.1: CSRF Protection
```
Attempt: POST to /analyze from different origin
Expected: Request rejected or protected
```

#### Test 3.2: Rate Limiting
```
Attempt: Send 1000 requests per second
Expected: Requests throttled or rejected
```

---

## ⚡ Performance Testing

### Test 1: Load Time

#### Test 1.1: Page Load
```
Measurement: Time to first contentful paint
Expected: < 2 seconds
Tool: Lighthouse, DevTools Performance tab
```

#### Test 1.2: Analysis Speed
```
Measurement: Time from upload to results
Expected: < 2 seconds for typical resume
File: 5-page resume (2-5 MB PDF)
```

### Test 2: Resource Usage

#### Test 2.1: Memory Usage
```
Measurement: RAM usage during analysis
Expected: < 100 MB
Tool: Task Manager or Psutil
```

#### Test 2.2: CPU Usage
```
Measurement: CPU during heavy processing
Expected: Spikes, returns to normal
Tool: Task Manager or Psutil
```

### Test 3: Concurrent Users

#### Test 3.1: Multiple Simultaneous Requests
```
Scenario: 10 users analyzing simultaneously
Expected: All complete without errors
```

---

## 🐛 Error Handling Testing

### Test 1: Common Errors

#### Test 1.1: PDF Corruption
```
Attempt: Upload corrupted PDF
Expected Error: "Failed to parse resume: PDF error"
Action: Clear error, allow retry
```

#### Test 1.2: Network Error
```
Simulate: Network disconnect during upload
Expected: "Network error: connection lost"
Recovery: Retry button available
```

#### Test 1.3: Server Error
```
Simulate: Server crash during analysis
Expected: "Internal server error"
Recovery: Graceful error message, clear form
```

### Test 2: Edge Cases

#### Test 2.1: Empty Resume PDF
```
Upload: PDF with only blank pages
Expected: "No recognized skills found in resume"
```

#### Test 2.2: Resume with Only Images
```
Upload: PDF containing only images
Expected: "No text could be extracted from PDF"
```

#### Test 2.3: Job Description with No Skills
```
Input: Job description with no recognized skills
Expected: "No recognized skills found in job description"
```

---

## 📊 Manual Testing Checklist

### Before Each Release:

- [ ] **Functionality**
  - [ ] File upload works
  - [ ] Analysis completes successfully
  - [ ] Results display correctly
  - [ ] Sample data loads
  - [ ] New Analysis resets form

- [ ] **UI/UX**
  - [ ] Layout looks professional
  - [ ] Colors and spacing correct
  - [ ] Responsive on all screen sizes
  - [ ] Icons and images display
  - [ ] Text is readable

- [ ] **Performance**
  - [ ] Page loads quickly
  - [ ] Analysis completes fast
  - [ ] No lag or freezing
  - [ ] Smooth animations

- [ ] **Error Handling**
  - [ ] Error messages are clear
  - [ ] Invalid inputs rejected
  - [ ] No console errors (F12)
  - [ ] Server errors handled gracefully

- [ ] **Security**
  - [ ] File validation works
  - [ ] No stored data
  - [ ] HTTPS ready (in production)
  - [ ] CORS configured correctly

- [ ] **Compatibility**
  - [ ] Chrome latest
  - [ ] Firefox latest
  - [ ] Safari latest
  - [ ] Edge latest
  - [ ] Mobile browsers

---

## 🚀 Performance Benchmarks

### Expected Metrics:

| Metric | Expected | Threshold |
|--------|----------|-----------|
| Page Load Time | < 2s | < 3s |
| Analysis Time | < 2s | < 5s |
| Memory Usage | < 50MB | < 100MB |
| CPU Usage | Spike to 40% | < 80% |
| File Upload | < 500ms | < 1s |
| Skill Extraction | < 200ms | < 500ms |

---

## 📈 Regression Testing

### Before Each Update:

1. Run all unit tests
2. Test critical user flows
3. Test on multiple browsers
4. Test responsive design
5. Check error handling
6. Verify performance metrics
7. Security scan

---

## 🎯 Testing Summary

### Recommended Testing Order:

1. **Unit Tests** (5-10 min)
   - Test individual functions
   - Verify logic correctness

2. **Integration Tests** (10-15 min)
   - Test complete flows
   - Verify module interactions

3. **Functional Tests** (15-20 min)
   - Test user workflows
   - Verify feature completeness

4. **UI/UX Tests** (10-15 min)
   - Check appearance
   - Test responsiveness

5. **Security Tests** (10 min)
   - File upload validation
   - Input sanitization

6. **Performance Tests** (5-10 min)
   - Load time measurement
   - Resource usage check

---

## ✅ Sign-Off

After completing all tests:

- [ ] All tests passed
- [ ] No critical bugs found
- [ ] Performance acceptable
- [ ] Security verified
- [ ] Ready for production

**Tested By:** ________________  
**Date:** ________________  
**Status:** ✅ Ready / ❌ Not Ready
