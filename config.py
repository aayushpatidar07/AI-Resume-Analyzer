"""
Configuration File for AI Resume Analyzer & Job Matcher
Customize the application settings here
"""

import os

# =====================================================
# FLASK CONFIGURATIONS
# =====================================================

# Application settings
DEBUG = True
TESTING = False
SECRET_KEY = 'your-secret-key-here'  # Change in production

# Server settings
HOST = '127.0.0.1'
PORT = 5000
DEVELOPMENT_MODE = True

# =====================================================
# FILE UPLOAD CONFIGURATION
# =====================================================

# Maximum file size in bytes (default: 16MB)
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf'}

# Upload folder path
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

# File cleanup (auto-delete after analysis)
AUTO_DELETE_UPLOADS = True

# =====================================================
# SKILL EXTRACTION CONFIGURATION
# =====================================================

# Minimum skill name length
MIN_SKILL_LENGTH = 2

# Maximum skills to return
MAX_SKILLS_TO_RETURN = None  # None = no limit

# Skill matching settings
CASE_INSENSITIVE_MATCHING = True
WORD_BOUNDARY_MATCHING = True

# =====================================================
# MATCHING CONFIGURATION
# =====================================================

# Match percentage calculation method
MATCHING_METHOD = 'intersection'  # Options: 'intersection', 'jaccard', 'cosine'

# Match level thresholds
MATCH_LEVEL_THRESHOLDS = {
    'Excellent Match': 80,
    'Good Match': 60,
    'Fair Match': 40,
    'Poor Match': 20,
    'Very Poor Match': 0
}

# =====================================================
# PDF PARSING CONFIGURATION
# =====================================================

# PDF parser settings
PDF_EXTRACTION_METHOD = 'text'  # Options: 'text', 'ocr'
PRESERVE_FORMATTING = False
REMOVE_NUMBERS = False
REMOVE_SPECIAL_CHARS = True

# =====================================================
# LOGGING CONFIGURATION
# =====================================================

# Enable/disable logging
LOGGING_ENABLED = True
LOG_LEVEL = 'INFO'  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = 'app.log'

# =====================================================
# SECURITY CONFIGURATION
# =====================================================

# Security headers
SECURITY_HEADERS = {
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'SAMEORIGIN',
    'X-XSS-Protection': '1; mode=block'
}

# CORS settings
CORS_ENABLED = False
CORS_ORIGINS = ['http://localhost:5000']

# =====================================================
# API CONFIGURATION
# =====================================================

# API rate limiting
RATE_LIMITING_ENABLED = False
RATE_LIMIT = '100 per hour'

# API response format
API_RESPONSE_FORMAT = 'json'
PRETTY_JSON = True

# =====================================================
# DATABASE CONFIGURATION (Optional)
# =====================================================

# Database settings (for future use)
DATABASE_ENABLED = False
DATABASE_TYPE = 'sqlite'  # Options: 'sqlite', 'postgresql', 'mysql'
DATABASE_PATH = 'resume_analyzer.db'

# Connection settings
DATABASE_CONFIG = {
    'sqlite': {
        'database': 'resume_analyzer.db'
    },
    'postgresql': {
        'host': 'localhost',
        'port': 5432,
        'database': 'resume_analyzer',
        'user': 'postgres',
        'password': 'password'
    },
    'mysql': {
        'host': 'localhost',
        'port': 3306,
        'database': 'resume_analyzer',
        'user': 'root',
        'password': 'password'
    }
}

# =====================================================
# EMAIL CONFIGURATION (Optional)
# =====================================================

# Email settings (for future use)
EMAIL_ENABLED = False
EMAIL_SERVICE = 'smtp'  # Options: 'smtp', 'sendgrid', 'mailgun'

# SMTP settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your-email@gmail.com'
SMTP_PASSWORD = 'your-app-password'
SMTP_USE_TLS = True

# =====================================================
# NOTIFICATION CONFIGURATION
# =====================================================

# Notification settings
NOTIFICATIONS_ENABLED = True
NOTIFICATION_TYPE = 'toast'  # Options: 'toast', 'modal', 'banner'

# =====================================================
# PERFORMANCE CONFIGURATION
# =====================================================

# Cache settings
CACHING_ENABLED = False
CACHE_TYPE = 'simple'
CACHE_DEFAULT_TIMEOUT = 300

# Compression settings
COMPRESSION_ENABLED = True
GZIP_COMPRESSION = True

# =====================================================
# FEATURE FLAGS
# =====================================================

# Enable/disable features
FEATURES = {
    'SAMPLE_DATA': True,
    'SKILL_EXTRACTION': True,
    'MATCH_CALCULATION': True,
    'ERROR_REPORTING': True,
    'ANALYTICS': False,
    'DARK_MODE': False,
    'EXPORT_PDF': False,
    'HISTORY': False,
}

# =====================================================
# CUSTOM SKILL DATABASE
# =====================================================

# Add custom skills here (will be merged with default skills)
CUSTOM_SKILLS = {
    # Programming Languages
    'elixir', 'crystal', 'nim',
    
    # Frameworks
    'phoenix', 'fastapi',
    
    # Tools
    'datadog', 'newrelic',
}

# =====================================================
# UI CONFIGURATION
# =====================================================

# Theme settings
THEME = 'light'  # Options: 'light', 'dark', 'auto'
PRIMARY_COLOR = '#198754'  # Green
SECONDARY_COLOR = '#0d6efd'  # Blue

# Animation settings
ANIMATIONS_ENABLED = True
ANIMATION_DURATION = 300  # milliseconds

# Layout settings
RESPONSIVE_DESIGN = True
MOBILE_FIRST = True
CONTAINER_MAX_WIDTH = 1200  # pixels

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def get_config(section=None):
    """Get configuration dictionary"""
    import sys
    config_module = sys.modules[__name__]
    
    if section:
        return {k: v for k, v in vars(config_module).items() 
                if not k.startswith('_') and k.isupper() and k.startswith(section)}
    
    return {k: v for k, v in vars(config_module).items() 
            if not k.startswith('_') and k.isupper()}

def print_config():
    """Print current configuration"""
    config = get_config()
    print("\n" + "="*60)
    print("CURRENT CONFIGURATION")
    print("="*60)
    for key, value in sorted(config.items()):
        if not isinstance(value, (dict, list)):
            print(f"{key}: {value}")
    print("="*60 + "\n")

# =====================================================
# DEVELOPMENT SETTINGS
# =====================================================

# Development-specific settings
if DEVELOPMENT_MODE:
    DEBUG = True
    AUTO_DELETE_UPLOADS = True

# =====================================================
# PRODUCTION SETTINGS
# =====================================================

# Production-specific settings (uncomment to use)
"""
if not DEVELOPMENT_MODE:
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    CORS_ENABLED = True
    LOGGING_ENABLED = True
    LOG_LEVEL = 'WARNING'
"""

# =====================================================
# VALIDATION
# =====================================================

def validate_config():
    """Validate configuration settings"""
    errors = []
    
    # Check file size
    if MAX_CONTENT_LENGTH < 1 * 1024 * 1024:  # Less than 1MB
        errors.append("MAX_CONTENT_LENGTH should be at least 1MB")
    
    # Check port range
    if not (1024 <= PORT <= 65535):
        errors.append("PORT must be between 1024 and 65535")
    
    # Check thresholds
    thresholds = list(MATCH_LEVEL_THRESHOLDS.values())
    if thresholds != sorted(thresholds):
        errors.append("MATCH_LEVEL_THRESHOLDS must be in ascending order")
    
    if errors:
        print("Configuration Errors:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    return True

# Validate on import
if validate_config():
    print("[CONFIG] Configuration validated successfully")
else:
    print("[CONFIG] Configuration validation failed")
