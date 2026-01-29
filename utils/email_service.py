"""
Email Service Module
Send emails for notifications and alerts
"""

from typing import List, Optional, Dict, Any
from enum import Enum
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger(__name__)


class EmailTemplate(Enum):
    """Email template types"""
    WELCOME = "welcome"
    ANALYSIS_COMPLETE = "analysis_complete"
    ERROR_ALERT = "error_alert"
    REPORT = "report"


class EmailService:
    """Service for sending emails"""
    
    def __init__(self, smtp_server: str = "smtp.gmail.com",
                 smtp_port: int = 587,
                 sender_email: Optional[str] = None,
                 sender_password: Optional[str] = None):
        """
        Initialize email service
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Sender email address
            sender_password: Sender email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.is_configured = sender_email is not None
    
    def send_email(self, 
                  recipient: str,
                  subject: str,
                  body: str,
                  html: bool = False) -> bool:
        """
        Send an email
        
        Args:
            recipient: Recipient email address
            subject: Email subject
            body: Email body
            html: Whether body is HTML
            
        Returns:
            True if email sent successfully
        """
        if not self.is_configured:
            logger.warning("Email service not configured")
            return False
        
        try:
            message = MIMEMultipart('alternative')
            message['Subject'] = subject
            message['From'] = self.sender_email
            message['To'] = recipient
            
            if html:
                message.attach(MIMEText(body, 'html'))
            else:
                message.attach(MIMEText(body, 'plain'))
            
            # Send email (placeholder)
            logger.info(f"Email sent to {recipient}: {subject}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            return False
    
    def send_analysis_complete_email(self,
                                     recipient: str,
                                     match_percentage: float,
                                     job_title: str) -> bool:
        """
        Send analysis complete notification email
        
        Args:
            recipient: Recipient email
            match_percentage: Match percentage
            job_title: Job title analyzed
            
        Returns:
            True if email sent
        """
        subject = f"Resume Analysis Complete - {match_percentage}% Match"
        body = f"""
        Your resume analysis is complete!
        
        Job Title: {job_title}
        Match Percentage: {match_percentage}%
        
        Log in to view detailed results.
        """
        
        return self.send_email(recipient, subject, body)
    
    def send_batch_email(self,
                        recipients: List[str],
                        subject: str,
                        body: str) -> int:
        """
        Send bulk email
        
        Args:
            recipients: List of recipient emails
            subject: Email subject
            body: Email body
            
        Returns:
            Number of emails sent successfully
        """
        success_count = 0
        
        for recipient in recipients:
            if self.send_email(recipient, subject, body):
                success_count += 1
        
        logger.info(f"Batch email sent: {success_count}/{len(recipients)} successful")
        return success_count


class EmailTemplate:
    """Email template manager"""
    
    TEMPLATES = {
        'welcome': """
        Welcome to Resume Analyzer!
        
        Thank you for signing up. You can now analyze your resume
        and match it with job descriptions.
        """,
        'analysis_complete': """
        Your resume analysis is complete!
        
        Match: {match_percentage}%
        Job: {job_title}
        
        Login to view detailed results.
        """,
        'error_alert': """
        An error occurred during processing.
        
        Error: {error_message}
        
        Please try again later.
        """
    }
    
    @staticmethod
    def get_template(template_type: str) -> str:
        """
        Get email template
        
        Args:
            template_type: Type of template
            
        Returns:
            Template string
        """
        return EmailTemplate.TEMPLATES.get(template_type, "")
    
    @staticmethod
    def format_template(template_type: str, **kwargs) -> str:
        """
        Format email template with variables
        
        Args:
            template_type: Type of template
            **kwargs: Variables to format
            
        Returns:
            Formatted template
        """
        template = EmailTemplate.get_template(template_type)
        return template.format(**kwargs)
