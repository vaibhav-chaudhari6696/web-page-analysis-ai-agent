# Website Scraping AI Agent

## Project Overview
AI-powered FastAPI application for intelligent website homepage analysis, extracting key insights about companies.


## Prerequisites
- Python 3.10+
- OpenAI API Key
- Docker (optional)

## Installation

### Local Setup
1. Clone the repository
```bash
git clone https://github.com/yourusername/website-scraper-agent.git
cd website-scraper-agent
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Unix
venv\Scripts\activate     # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

### Environment Configuration
Create `.env` file in project root:
```
SECRET_KEY=your_unique_secret_key
OPENAI_API_KEY=your_openai_api_key
```

###Secret Key Generation
Generate a secure secret key:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```


### Running Application

#### Local Run
```bash
uvicorn src.main:app --reload
```

#### Docker Deployment
1. Build Docker image
```bash
docker-compose build
```

2. Run Docker container
```bash
docker-compose up -d
```


## API Usage

### Endpoint
- URL: `/analyze`
- Method: POST
- Authentication:  Secret Key in `Authorization` header

### Request Example
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Authorization: your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

### Response Format
```json
{
  "industry": "Technology",
  "company_size": "Medium",
  "location": "San Francisco, CA"
}
```

## Error Handling
- 401: Invalid Keys
- 400: Scraping Failed
- 422: Invalid URL Format

## Authentication
- Set `SECRET_KEY` in `.env`
- Include key in `Authorization` header
- 401 Unauthorized for invalid keys


## Security Considerations
- Use strong, unique `SECRET_KEY`
- Keep `OPENAI_API_KEY` confidential
- Use HTTPS in production

## Troubleshooting
- Verify API keys
- Check website accessibility
- Verify environment configurations
