import requests

R_TEMPLE = "https://www.reddit.com/r/Temple/.json"

def get_reddit_data():
    '''
    This function prints the json data from the r/temple subreddit into the terminal.
    FOR TESTING
    '''
    response = requests.get(R_TEMPLE)
    print(response.json())

class RedditManager:
    """
    Responsible for fetching reddit data or querying from saved json data to reduce API abuse.
    """

    def __init__(filename: str):
        self.filename = filename