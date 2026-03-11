# import statements
import requests

# r/temple json file
r_temple = "https://www.reddit.com/r/Temple/.json"

def get_reddit_data():
    '''
    This function prints the json data from the r/temple subreddit into the terminal.
    FOR TESTING
    '''
    response = requests.get(r_temple)
    print(response.json())