import requests

class SuperPrompter:
    def __init__(self, api_key, base_url="https://promptsgenerator.ai"):
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }

    def search_news(self, query, limit=10):
        """
        Wraps the /api/v1/news/search endpoint.
        """
        endpoint = f"{self.base_url}/api/v1/news/search"
        params = {"q": query, "limit": limit}
        
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            
            # Raise an error for 4xx or 5xx status codes
            response.raise_for_status() 
            
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}", "status_code": response.status_code}
        except Exception as err:
            return {"error": f"An unexpected error occurred: {err}"}

# Usage Example for Developers:
# sdk = SuperPrompter(api_key="sp_live_xxxx")
# results = sdk.search_news("latest AI news")
# Step 5 (Internal SDK Logic) is now complete.
