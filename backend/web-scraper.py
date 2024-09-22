import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS  # Make sure to install the duckduckgo_search package

class WebScraper:
    def __init__(self, lastName):
        self.lastName = lastName
        self.name_info, self.name_url = self.get_last_name_info()

    # Function to search for the last name on DuckDuckGo and get top 5 results
    def get_top_five_results(self):
        ddgs = DDGS()  # Create an instance of DDGS
        search_results = ddgs.text(f"{self.lastName} last name meaning history", max_results=5)
        return search_results

    # Function to scrape the content from a URL
    def scrape_content(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Example heuristic: Look for content under tags that might hold relevant info
            paragraphs = soup.find_all('p')
            content = ' '.join([p.get_text() for p in paragraphs if 'name' in p.get_text().lower()])
            
            # If the heuristic doesn't return enough content, add more rules.
            if len(content) < 200:
                content = ' '.join([p.get_text() for p in paragraphs[:10]])
            
            return content.strip()
        
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return ""

    # Function to get the last name meaning and history from top 5 results
    def get_last_name_info(self):
        search_results = self.get_top_five_results()
        info = []

        # Scrape content from each result
        for result in search_results:
            print(f"Scraping {result['title']} - {result['href']}")
            content = self.scrape_content(result['href'])
            if content:
                info.append({
                    'title': result['title'],
                    'url': result['href'],
                    'content': content
                })

        return info, search_results

# Example usage
if __name__ == "__main__":
    scraper = WebScraper("Smith")
    last_name_info = scraper.name_info
    print(last_name_info)
