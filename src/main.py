from fastapi import FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader
from src.config import settings
from src.models import WebsiteAnalysisRequest, WebsiteAnalysisResponse
from src.scraper import WebsiteScraper
from src.agents.website_analyzer import WebsiteAnalyzer
from src.validate_and_clean_raw_response import ValidateAndCleanRawResponse

app = FastAPI()

api_key_header = APIKeyHeader(name="Authorization")

def validate_api_key(api_key: str = Security(api_key_header)):
    if api_key != settings.SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

@app.post("/analyze", response_model=WebsiteAnalysisResponse)
async def analyze_website(
    request: WebsiteAnalysisRequest, 
    _: str = Security(validate_api_key)
):
    # Scrape homepage
    homepage_content = WebsiteScraper.scrape_homepage(request.url)
    
    if not homepage_content:
        raise HTTPException(status_code=400, detail="Unable to scrape website")

    # Analyze with CrewAI
    analyzer = WebsiteAnalyzer(homepage_content)
    analysis = analyzer.analyze()
    
    return WebsiteAnalysisResponse(**analysis)