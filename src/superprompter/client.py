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
            
        except requests.exceptions.Timeout:
            return {"error": "The request timed out. Please try again later."}
            
        except requests.exceptions.HTTPError as err:
            # Captures 401 (Unauthorized), 404 (Not Found), etc. [cite: 54-56, 97-99]
            return {
                "error": f"HTTP error occurred: {err}",
                "status_code": response.status_code,
                "details": response.text
            }
            
        except Exception as err:
            # Catch-all for unexpected issues 
            return {"error": f"An unexpected error occurred: {err}"}
