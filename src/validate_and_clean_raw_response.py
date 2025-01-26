import json

class ValidateAndCleanRawResponse:
    @staticmethod
    def validate_and_clean_json(response: str) -> dict:
        """
        Validates and cleans up JSON response from LLM.
        Args:
            response: The raw response string from LLM
            default_value: Default value to use if JSON parsing fails
        Returns:
            A dictionary with market_segment key
        """
        try:
            # Clean up the response to ensure it's valid JSON
            json_str = response.strip()

            if not json_str.startswith("{"):
                json_str = json_str[json_str.find("{") :]
            if not json_str.endswith("}"):
                json_str = json_str[: json_str.rfind("}") + 1]

            return json.loads(json_str)

        except (json.JSONDecodeError, ValueError):
             return {
            "industry": "Unknown",
            "company_size": "Unknown",
            "location": "Unknown"
            }