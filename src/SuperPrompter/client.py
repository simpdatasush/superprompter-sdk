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
            response = requests.get(
                endpoint, 
                headers=self.headers, 
                params=params, 
                timeout=10
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
