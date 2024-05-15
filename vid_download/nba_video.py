import json
import requests
from random import randint

def download_nba_video(gameID, eventID, date):
    """Downloads a specified NBA video.

    Args:
        gameID (str): The ID of the game.
        eventID (str): The ID of the event.
        date (str): The date of the game in the format YYYY/MM/DD

    Returns:
        str: The URL of the video, or None if the video could not be found.
    """

    USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]
    random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]

    base_url = 'https://stats.nba.com/stats/videoeventsasset'
    video_url = base_url + '?GameEventID=%s&GameID=%s' % (eventID, gameID)

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://www.nba.com',
        'Host': 'stats.nba.com',
        'User-Agent': random_agent,
        'Referer': 'https://www.nba.com/',
    }

    found = False
    i=0
    while(not found):
        try:
            if(i>=8):
                break
            response = requests.get(video_url, headers=headers, params={'GameEventID': eventID, 'GameID': gameID}, timeout=20)
            response.raise_for_status()  # Raise an exception for error status codes

            json_data = response.json()
            uuid = json_data['resultSets']['Meta']['videoUrls'][0]['uuid']

            final_video_url = 'https://videos.nba.com/nba/pbp/media/'+ date +'/' + str(gameID) + '/' + str(eventID)+'/' + uuid + '_1280x720.mp4'

            # Download the video
            video_response = requests.get(final_video_url, allow_redirects=True)
            # with open(f"/scratch/dnp9357/rbda/dataset/{ str(gameID) + '-' + str(eventID) }.mp4", 'wb') as f:
            with open(f"./ftdataset/made/{ str(gameID) + '-' + str(eventID) }.mp4", 'wb') as f:
                f.write(video_response.content)

            print('Video download complete!')
            found = True
            return final_video_url  # Return the URL for convenience

        except Exception as e:
            print(f'Error: Could not download the video in try {i}. {e}')
            i+=1
            # return None  # Indicate failure

# Example usage:
if __name__ == "__main__":    
    game_id = '0022200605'
    event_id = '67'
    date = '2024/03/14'

    video_url = download_nba_video(game_id, event_id, date) 
    if video_url:
        print("Video downloaded successfully. URL:", video_url)
