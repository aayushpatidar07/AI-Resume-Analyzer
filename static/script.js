/**
 * AI Resume Analyzer & Job Matcher - Frontend Script
 * Handles form submission, API calls, and result display
 */

document.addEventListener('DOMContentLoaded', function() {
    const analyzeForm = document.getElementById('analyzeForm');
    const loadSampleBtn = document.getElementById('loadSampleBtn');
    const newAnalysisBtn = document.getElementById('newAnalysisBtn');

    // Form submission handler
    analyzeForm.addEventListener('submit', handleFormSubmit);
    
    // Load sample job description
    loadSampleBtn.addEventListener('click', handleLoadSample);
    
    // New analysis button
    newAnalysisBtn.addEventListener('click', resetForm);

    // File validation on change
    document.getElementById('resumeFile').addEventListener('change', validateFile);
});

/**
 * Handle form submission
 */
function handleFormSubmit(event) {
    event.preventDefault();

    const resumeFile = document.getElementById('resumeFile');
    const jobDescription = document.getElementById('jobDescription');
    const submitBtn = document.getElementById('submitBtn');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const errorMessage = document.getElementById('errorMessage');

    // Validate inputs
    if (!resumeFile.files.length) {
        showError('Please select a resume file');
        return;
    }

    if (!jobDescription.value.trim()) {
        showError('Please enter a job description');
        return;
    }

    // Prepare form data
    const formData = new FormData();
    formData.append('resume', resumeFile.files[0]);
    formData.append('job_description', jobDescription.value);

    // Disable submit button and show loading
    submitBtn.disabled = true;
    loadingSpinner.style.display = 'block';
    errorMessage.style.display = 'none';

    // Send request
    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        submitBtn.disabled = false;
        loadingSpinner.style.display = 'none';

        if (data.success) {
            displayResults(data);
        } else {
            showError(data.error || 'An error occurred during analysis');
        }
    })
    .catch(error => {
        submitBtn.disabled = false;
        loadingSpinner.style.display = 'none';
        showError('Network error: ' + error.message);
        console.error('Error:', error);
    });
}

/**
 * Display analysis results
 */
function displayResults(data) {
    // Hide form, show results
    document.querySelector('.card').style.display = 'none';
    document.getElementById('resultsSection').style.display = 'block';
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Update match percentage bar
    const matchPercentage = data.match_percentage;
    const matchPercentageBar = document.getElementById('matchPercentageBar');
    const matchPercentageText = document.getElementById('matchPercentageText');
    const matchLevel = document.getElementById('matchLevel');

    // Determine color based on percentage
    let barColor = 'bg-danger';
    if (matchPercentage >= 80) barColor = 'bg-success';
    else if (matchPercentage >= 60) barColor = 'bg-info';
    else if (matchPercentage >= 40) barColor = 'bg-warning';

    matchPercentageBar.className = 'progress-bar ' + barColor;
    matchPercentageBar.style.width = matchPercentage + '%';
    matchPercentageBar.setAttribute('aria-valuenow', matchPercentage);
    matchPercentageText.textContent = matchPercentage + '%';

    // Update match level
    matchLevel.textContent = data.match_level;
    matchLevel.className = getMatchLevelClass(matchPercentage);

    // Update statistics
    document.getElementById('matchedCount').textContent = data.matched_count;
    document.getElementById('missingCount').textContent = data.missing_count;
    document.getElementById('resumeSkillsCount').textContent = data.resume_skills_count;
    document.getElementById('requiredSkillsCount').textContent = data.required_skills_count;

    // Display matched skills
    displaySkills('matchedSkillsList', data.matched_skills, 'matched');

    // Display missing skills
    displaySkills('missingSkillsList', data.missing_skills, 'missing');
}

/**
 * Display skills with badges
 */
function displaySkills(elementId, skills, type) {
    const container = document.getElementById(elementId);
    container.innerHTML = '';

    if (skills.length === 0) {
        container.innerHTML = '<div class="empty-message">No skills to display</div>';
        return;
    }

    skills.forEach(skill => {
        const badge = document.createElement('span');
        badge.className = 'skill-badge ' + type;
        
        const icon = type === 'matched' ? 'fa-check-circle' : 'fa-times-circle';
        badge.innerHTML = `<i class="fas ${icon}"></i>${capitalizeSkill(skill)}`;
        
        container.appendChild(badge);
    });
}

/**
 * Capitalize skill name
 */
function capitalizeSkill(skill) {
    return skill.split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

/**
 * Get match level CSS class
 */
function getMatchLevelClass(percentage) {
    if (percentage >= 80) return 'text-success';
    else if (percentage >= 60) return 'text-info';
    else if (percentage >= 40) return 'text-warning';
    else return 'text-danger';
}

/**
 * Show error message
 */
function showError(message) {
    const errorMessage = document.getElementById('errorMessage');
    const errorText = document.getElementById('errorText');
    errorText.textContent = message;
    errorMessage.style.display = 'block';
}

/**
 * Validate file input
 */
function validateFile(event) {
    const file = event.target.files[0];
    const fileError = document.getElementById('fileError');

    if (file) {
        // Check file type
        if (file.type !== 'application/pdf') {
            fileError.textContent = 'Only PDF files are allowed';
            fileError.style.display = 'block';
            event.target.value = '';
            return;
        }

        // Check file size (16MB)
        const maxSize = 16 * 1024 * 1024;
        if (file.size > maxSize) {
            fileError.textContent = 'File size must be less than 16MB';
            fileError.style.display = 'block';
            event.target.value = '';
            return;
        }

        fileError.style.display = 'none';
    }
}

/**
 * Load sample job description
 */
function handleLoadSample(event) {
    event.preventDefault();

    fetch('/api/sample-data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('jobDescription').value = data.sample_job_description;
            
            // Add a toast notification
            showToast('Sample job description loaded!');
        })
        .catch(error => {
            showError('Failed to load sample data');
            console.error('Error:', error);
        });
}

/**
 * Reset form and return to input
 */
function resetForm(event) {
    event.preventDefault();

    // Reset form
    document.getElementById('analyzeForm').reset();
    document.getElementById('resumeFile').value = '';
    document.getElementById('jobDescription').value = '';

    // Show form, hide results
    document.querySelector('.card').style.display = 'block';
    document.getElementById('resultsSection').style.display = 'none';
    document.getElementById('errorMessage').style.display = 'none';

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });

    showToast('Ready for a new analysis!');
}

/**
 * Show toast notification
 */
function showToast(message) {
    // Create toast element
    const toast = document.createElement('div');
    toast.className = 'alert alert-success position-fixed bottom-0 end-0 m-3';
    toast.style.zIndex = '1050';
    toast.innerHTML = `
        <i class="fas fa-check-circle"></i> ${message}
    `;

    document.body.appendChild(toast);

    // Auto remove after 3 seconds
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

/**
 * Handle Enter key in textarea
 */
document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter' && event.ctrlKey) {
        const analyzeForm = document.getElementById('analyzeForm');
        if (analyzeForm) {
            analyzeForm.dispatchEvent(new Event('submit'));
        }
    }
});

// Prevent default drag and drop
document.addEventListener('dragover', function(e) {
    e.preventDefault();
    e.stopPropagation();
});

document.addEventListener('drop', function(e) {
    e.preventDefault();
    e.stopPropagation();
});
