import requests
from typing import Dict, Any
import logging
import time

class MarketDataCollector:
    def __init__(self):
        self.sources = ['api1', 'api2']  # Different data sources
        
    def fetch_data(self) -> Dict[str, Any]:
        """
        Fetches market data from multiple sources with retry logic.
        
        Returns:
            Dict: Collected market data
        """
        data = {}
        for source in self.sources:
            try:
                response = requests.get(f"http://{source}/market-data")
                if response.status_code == 200:
                    data.update(response.json())
                    break  # Stop after first successful fetch
            except Exception as e:
                logging.error(f"Failed to fetch from {source}: {e}")
                time.sleep(5)  # Wait before retrying
        return data