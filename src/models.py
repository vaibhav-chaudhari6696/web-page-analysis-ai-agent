from pydantic import BaseModel, Field
from typing import Optional

class WebsiteAnalysisRequest(BaseModel):
    url: str = Field(..., description="URL of the website to analyze")

class WebsiteAnalysisResponse(BaseModel):
    industry: Optional[str] = None
    company_size: Optional[str] = None
    location: Optional[str] = None