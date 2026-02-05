import requests

class SuperPrompter:
    def __init__(self, api_key, base_url="https://promptsgenerator.ai"):
        """
        Initializes the SuperPrompter client. 
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }

    def search_news(self, query, limit=10):
        """
        Searches for news using the SuperPrompter API.
        """
        endpoint = f"{self.base_url}/api/v1/news/search"
        params = {"q": query, "limit": limit}
        
        try:
            # Added timeout to prevent hanging, following your latest logic [cite: 10, 63]
            response = requests.get(
                endpoint, 
                headers=self.headers, 
                params=params, 
                timeout=10
            )
            response.raise_for_status() [cite: 50, 93]
            return response.json() [cite: 51, 94]
            
        except requests.exceptions.RequestException as e:
            # Handles Timeouts, HTTP errors, and Connection issues [cite: 52, 54, 57]
            return {"error": str(e)}
