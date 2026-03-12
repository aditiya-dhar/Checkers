import os
import datetime
import requests
import json
from checkers.types.reddit import RedditResponse, reddit_response_from_dict

class RedditManager:
    """
    Handles fetching Reddit data with a 24-hour file-based caching system.
    """
    
    URL = "https://www.reddit.com/r/Temple/.json"
    STALE_DAYS_ALLOWED = 1

    def __init__(self, filename: str):
        self.filename = filename

    def _is_cache_fresh(self) -> bool:
        """Checks if the file exists and was modified within the stale margin"""
        if not os.path.exists(self.filename):
            return False
        
        modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(self.filename))
        now = datetime.datetime.now()
        
        return (now - modified_time) < datetime.timedelta(days=self.STALE_DAYS_ALLOWED)

    def _fetch_and_save(self):
        """Queries the API and saves the raw JSON to a file."""
        response = requests.get(self.URL)

        # We simply fail if the request fails so we dont overwrite the data
        response.raise_for_status()
        
        data = response.json()
        with open(self.filename, 'w') as f:
            json.dump(data, f)
        return data

    def get_data(self) -> RedditResponse:
        """
        The main entry point: Returns cached data or fresh data depending on file age.
        """
        if self._is_cache_fresh():
            with open(self.filename, 'r') as f:
                data = json.load(f)
        else:
            data = self._fetch_and_save()

        return reddit_response_from_dict(data)
