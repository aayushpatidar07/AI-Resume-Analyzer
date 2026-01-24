# Contributing Guide

## How to Contribute

We welcome contributions to the AI Resume Analyzer & Job Matcher project! Here's how you can help.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/AI-Resume-Analyzer.git
   cd AI-Resume-Analyzer
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Development Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and commit regularly:
   ```bash
   git add .
   git commit -m "feat: description of your changes"
   ```

3. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request** on GitHub with a clear description

## Code Style

- Follow PEP 8 guidelines
- Use type hints for function parameters and return values
- Write docstrings for all public functions and classes
- Use meaningful variable and function names

### Example:
```python
def extract_skills(text: str) -> List[str]:
    """
    Extract skills from text.
    
    Args:
        text: Input text to extract skills from
        
    Returns:
        List of extracted skills
    """
    # Implementation
    pass
```

## Commit Message Format

Use descriptive commit messages following this format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Build, dependencies, etc.

### Example:
```
feat(skill-extractor): add regex-based skill matching

Implement regex-based pattern matching for skill extraction
to improve accuracy when identifying technical skills.

Closes #123
```

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR:
  ```bash
  pytest
  ```
- Maintain or improve code coverage

## Documentation

- Update README.md if adding new features
- Add docstrings to all functions
- Update API_DOCUMENTATION.md for API changes
- Add comments for complex logic

## Pull Request Process

1. Update documentation and README.md
2. Add or update tests as needed
3. Ensure code passes all checks:
   ```bash
   black .          # Code formatting
   flake8 .         # Linting
   mypy .           # Type checking
   pytest           # Tests
   ```
4. Create PR with clear title and description
5. Link related issues (if any)
6. Respond to review feedback promptly

## Reporting Issues

- Use the GitHub Issues tab
- Provide clear description and steps to reproduce
- Include error messages and logs if relevant
- Specify your environment (OS, Python version, etc.)

## Code of Conduct

Be respectful and inclusive. We're all here to learn and improve together!

## Questions?

- Open an issue for discussion
- Comment on pull requests
- Contact the maintainers

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing! 🎉
