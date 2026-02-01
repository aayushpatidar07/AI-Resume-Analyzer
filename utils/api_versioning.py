"""
API Versioning
Support multiple API versions
"""

from typing import Dict, Any, Optional, List
from enum import Enum
from datetime import datetime


class APIVersion(Enum):
    """API version enumeration"""
    V1 = "1.0.0"
    V2 = "2.0.0"
    V3_BETA = "3.0.0-beta"


class VersionManager:
    """Manage API versions with deprecation tracking"""
    
    VERSIONS = {
        'v1': {
            'version': APIVersion.V1,
            'deprecated': False,
            'release_date': '2025-01-01',
            'sunset_date': None,
            'endpoints': [
                'GET /',
                'POST /analyze',
                'GET /api/sample-data'
            ]
        },
        'v2': {
            'version': APIVersion.V2,
            'deprecated': False,
            'release_date': '2025-06-01',
            'sunset_date': None,
            'endpoints': [
                'GET /api/v2/health',
                'GET /api/v2/stats',
                'POST /api/v2/batch-analyze',
                'POST /api/v2/skills/recommendations',
                'POST /api/v2/export'
            ]
        },
        'v3': {
            'version': APIVersion.V3_BETA,
            'deprecated': False,
            'status': 'beta',
            'release_date': None,
            'sunset_date': None,
            'endpoints': [
                'POST /api/v3/analyze/advanced',
                'GET /api/v3/reports',
                'POST /api/v3/webhooks'
            ]
        }
    }
    
    @staticmethod
    def get_version_info(version: str = None) -> Dict[str, Any]:
        """Get API version information"""
        if version and version in VersionManager.VERSIONS:
            return VersionManager.VERSIONS[version]
        return VersionManager.VERSIONS
    
    @staticmethod
    def is_deprecated(version: str) -> bool:
        """Check if version is deprecated"""
        if version in VersionManager.VERSIONS:
            return VersionManager.VERSIONS[version]['deprecated']
        return False
    
    @staticmethod
    def get_endpoints(version: str) -> list:
        """Get endpoints for version"""
        if version in VersionManager.VERSIONS:
            return VersionManager.VERSIONS[version]['endpoints']
        return []


def api_version_header(version: str) -> Dict[str, str]:
    """Generate API version header"""
    return {
        'X-API-Version': version,
        'X-API-Deprecation': 'false' if not VersionManager.is_deprecated(version) else 'true'
    }
