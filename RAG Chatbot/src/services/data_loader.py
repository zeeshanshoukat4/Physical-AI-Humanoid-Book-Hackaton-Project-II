import httpx
import xml.etree.ElementTree as ET
from typing import List, Dict
from ..core.config import get_settings

settings = get_settings()

class DataLoader:
    """
    Service for fetching and parsing content from a sitemap and individual URLs.
    """

    def __init__(self):
        self.client = httpx.Client()
        self.sitemap_url = settings.SITEMAP_URL

    def fetch_sitemap_urls(self) -> List[str]:
        """
        Fetches the sitemap and extracts all content URLs.
        """
        print(f"Fetching sitemap from: {self.sitemap_url}")
        try:
            response = self.client.get(self.sitemap_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            root = ET.fromstring(response.content)
            urls = []
            # Namespace for sitemap XML
            namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            for url_elem in root.findall('sitemap:url', namespace):
                loc_elem = url_elem.find('sitemap:loc', namespace)
                if loc_elem is not None and loc_elem.text:
                    # Temporary fix for incorrect domain in sitemap
                    correct_url = loc_elem.text.replace(
                        "https://physical-ai-book.example.com", 
                        "https://physical-ai-humanoid-book-hackaton-zeta.vercel.app"
                    )
                    urls.append(correct_url)
            print(f"Found {len(urls)} URLs in sitemap (and corrected domain).")
            return urls
        except httpx.HTTPStatusError as e:
            print(f"HTTP error fetching sitemap: {e}")
            return []
        except ET.ParseError as e:
            print(f"XML parsing error for sitemap: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error occurred while fetching sitemap: {e}")
            return []

    def fetch_url_content(self, url: str) -> Dict[str, str]:
        """
        Fetches content from a single URL.
        Returns a dictionary with 'url' and 'content', or an empty dict on error.
        """
        print(f"Fetching content from: {url}")
        try:
            response = self.client.get(url)
            response.raise_for_status()
            # Assuming content is HTML for now, and we'll extract relevant text later
            return {"url": url, "content": response.text}
        except httpx.HTTPStatusError as e:
            print(f"HTTP error fetching {url}: {e}")
            return {}
        except Exception as e:
            print(f"An unexpected error occurred while fetching {url}: {e}")
            return {}

# Example Usage (for testing)
if __name__ == "__main__":
    loader = DataLoader()
    sitemap_urls = loader.fetch_sitemap_urls()
    if sitemap_urls:
        print(f"\nFirst 3 URLs from sitemap: {sitemap_urls[:3]}")
        first_url_content = loader.fetch_url_content(sitemap_urls[0])
        if first_url_content:
            print(f"\nContent from first URL ({first_url_content['url']}) snippet:")
            print(first_url_content['content'][:500]) # Print first 500 characters
    else:
        print("No URLs found in sitemap or sitemap could not be fetched.")
