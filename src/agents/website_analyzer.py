from crewai import Agent, Task, Crew
from langchain_community.llms import OpenAI
from src.config import settings
from src.validate_and_clean_raw_response import ValidateAndCleanRawResponse


class WebsiteAnalyzer:
    def __init__(self, homepage_content):
        self.homepage_content = homepage_content
        self.llm = OpenAI(api_key=settings.OPENAI_API_KEY, model="gpt-4o-mini")
            
    def analyze(self):
        # Single intelligent agent for analysis
        analysis_agent = Agent(
            role='Comprehensive Website Analyzer',
            goal='Extract detailed insights about a company from its website',
            backstory='An expert business intelligence analyst skilled at deciphering company characteristics from website content',
            llm=self.llm
        )

        analysis_task = Task(
            description=f'''
            Analyze this scraped website home page content comprehensively. 
            Only use information from website home page content to analyze and don't use any inferred or assumed information
            Don't search for any relevant information which is not found in website home page content for identification in such case you can return N/A

            Extract and categorize the following:
            1. Precise industry classification
            2. Company size estimation based on any relevant information about company size (e.g small,medium,large,N/A(If not found any relevant information in website home page content)). Also provide reason on which basis company size is identified from website homepage content.
            3. Geographical location
            
            Content to analyze: {self.homepage_content}
            
            Provide output as a JSON with keys: industry, company_size, location
            Output MUST be in format JSON object as:
            {{
              "industry": "...",
              "company_size": "...",
              "location": "..."
            }}
            ''',
            agent=analysis_agent,
            expected_output='JSON with industry, company_size, and location'
        )

        crew = Crew(
            agents=[analysis_agent],
            tasks=[analysis_task],
            verbose=True
        )
    
        try:
            raw_result = crew.kickoff()
            result = ValidateAndCleanRawResponse.validate_and_clean_json(raw_result.raw)
            
            return result

        except Exception as e:

            return {
                'industry': None,
                'company_size': None,
                'location': None
            }