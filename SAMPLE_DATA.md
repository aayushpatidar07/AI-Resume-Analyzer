# SAMPLE TEST DATA

## Saample Resume (for manual testing)

```
JOHN ANDERSON
San Francisco, CA | (555) 123-4567 | john@email.com | linkedin.com/in/johnanderson

PROFESSIONAL SUMMARY
Full Stack Developer with 5+ years of experience building scalable web applications. 
Proficient in Python, JavaScript, React, and cloud technologies. 
Experienced in Agile development and leading technical teams.

TECHNICAL SKILLS
Languages: Python, JavaScript, TypeScript, Java, SQL
Web Frameworks: Flask, Django, FastAPI, React, Node.js, Express
Databases: PostgreSQL, MongoDB, Redis, MySQL
Cloud & DevOps: AWS, Docker, Kubernetes, Jenkins, GitLab CI/CD
Tools & Libraries: Git, Git Flow, RESTful APIs, GraphQL, Webpack
Testing: Pytest, Jest, Selenium, Cypress

PROFESSIONAL EXPERIENCE

Senior Full Stack Developer | TechCorp (2021 - Present)
- Architected and deployed microservices using Docker and Kubernetes on AWS
- Developed React-based frontend with 99.9% uptime using Redux
- Built RESTful APIs with Python Flask and FastAPI
- Implemented CI/CD pipelines with Jenkins and GitLab
- Mentored 3 junior developers and conducted code reviews

Full Stack Developer | StartupXYZ (2019 - 2021)
- Developed full-stack web applications using Python Django and React
- Managed PostgreSQL and MongoDB databases
- Implemented authentication using OAuth and JWT
- Deployed applications on AWS EC2 and RDS
- Used Git for version control and collaborative development

Web Developer | Digital Agency (2018 - 2019)
- Built responsive websites using HTML5, CSS3, JavaScript
- Implemented RESTful APIs with Node.js and Express
- Utilized Bootstrap for responsive UI design
- Managed customer projects in Agile/Scrum environment

EDUCATION
Bachelor of Science in Computer Science
University of California (2018)

CERTIFICATIONS
- AWS Solutions Architect Associate
- Docker Certified Associate
- Certified Scrum Master (CSM)

PROJECTS
- E-commerce Platform: Built with React, Flask, PostgreSQL (deployed on AWS)
- Real-time Chat Application: Node.js, Socket.io, MongoDB, Docker
- Data Analytics Dashboard: Python, TensorFlow, Pandas, Matplotlib

ADDITIONAL SKILLS
Machine Learning, Deep Learning, TensorFlow, Natural Language Processing
Linux Administration, Apache, Nginx
Agile/Scrum methodology, Jira, Confluence, Asana
```

## Sample Job Description (for manual testing)

```
SENIOR FULL STACK DEVELOPER

Company: Tech Solutions Inc.
Location: Remote/Hybrid
Salary: $150,000 - $180,000

ABOUT THE ROLE
We're seeking a Senior Full Stack Developer to join our growing engineering team.
You'll work on our flagship web platform serving 100K+ users globally.
Lead architectural decisions, mentor junior developers, and drive technical excellence.

REQUIRED SKILLS
- Python or JavaScript (5+ years)
- React (4+ years)
- Flask, Django, or Node.js
- PostgreSQL and MongoDB
- Docker and Kubernetes
- AWS (EC2, S3, RDS, Lambda)
- REST APIs and GraphQL
- Git and GitHub
- SQL and database design
- CI/CD pipelines (Jenkins, GitLab CI, or GitHub Actions)

NICE TO HAVE
- Machine Learning / TensorFlow experience
- Microservices architecture
- Redis caching
- Elasticsearch
- GraphQL implementation
- AWS Lambda and Serverless
- Docker Swarm
- Terraform or CloudFormation
- Prometheus monitoring
- Apache or Nginx configuration

RESPONSIBILITIES
- Design and implement scalable backend services
- Build responsive React applications
- Optimize database queries and API performance
- Implement security best practices
- Deploy and manage applications on AWS
- Write unit and integration tests
- Conduct code reviews
- Document technical decisions and architecture
- Participate in Agile standups and planning
- Mentor junior team members

NICE TO HAVE QUALIFICATIONS
- Open source contributions
- Technical blog or speaking experience
- Experience with machine learning
- Blockchain or Web3 experience
- DevOps tooling experience

We value candidates who are passionate about technology, enjoy problem-solving,
and have excellent communication skills.
```

## How to Use This Data

1. **Create a PDF Resume**: 
   - Copy the "Sample Resume" text above
   - Paste into a text editor or Word
   - Save as PDF (File > Export as PDF)
   - Use this PDF file in the application

2. **Job Description**:
   - Copy the "Sample Job Description" text above
   - Paste directly into the Job Description textarea
   - Click "Analyze Resume"

3. **Expected Results**:
   - Match Percentage: Should be around 70-80%
   - Matched Skills: Python, JavaScript, React, Flask, PostgreSQL, MongoDB, Docker, 
     Kubernetes, AWS, REST APIs, Git, SQL, CI/CD, Agile, Node.js, Express
   - Missing Skills: GraphQL, TensorFlow, Machine Learning, Redis, Elasticsearch,
     Microservices, Apache, Nginx, Prometheus

## How to Create Your Own PDF Resume

### Option 1: Using Microsoft Word
1. Open Microsoft Word
2. Create your resume content
3. File → Export → Create PDF/XPS
4. Save and use in the application

### Option 2: Using Google Docs
1. Open Google Docs
2. Create your resume
3. File → Download → PDF Document
4. Save and use in the application

### Option 3: Using Online Tools
1. Visit canva.com or similar
2. Create resume
3. Download as PDF
4. Use in the application

## Tips for Testing

✅ **Try Different Scenarios**:
   - High match (70%+): Tech roles matching your skills
   - Medium match (40-60%): Some skills match, some missing
   - Low match (<40%): Completely different tech stack

✅ **Test Edge Cases**:
   - Very short job description (< 50 words)
   - Very long resume (20+ pages)
   - Special characters and symbols
   - Job descriptions in different formats

✅ **Test Mobile**:
   - Resize browser window to test responsive design
   - Use your phone to access http://[your-computer-ip]:5000

## Debugging Tips

If results don't look right:

1. **Check extracted skills**: 
   - Open browser console (F12)
   - Check what skills were detected

2. **Check PDF parsing**:
   - Ensure PDF is readable
   - Try a different PDF file

3. **Check skill database**:
   - Edit `utils/skill_extractor.py`
   - Add new skills to `TECHNICAL_SKILLS` set

## Sample Skills for Testing

### Always Detected:
- Python, Java, JavaScript, React, Angular, Vue
- SQL, MongoDB, PostgreSQL, MySQL
- Docker, Kubernetes, AWS, Azure, GCP
- Flask, Django, Spring Boot, Node.js
- Git, GitHub, GitLab
- REST, GraphQL, API

### Sometimes Missed:
- Niche frameworks
- Company-specific tools
- Uncommon acronyms
- Very new technologies

Add missing skills to improve detection!
