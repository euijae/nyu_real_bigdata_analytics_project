from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import EndPeriod, StartPeriod
from random import randint


class PlayByPlayV3(Endpoint):
    endpoint = "playbyplayv3"
    expected_data = {
        "AvailableVideo": ["videoAvailable"],
        "PlayByPlay": [
            "gameId",
            "actionNumber",
            "clock",
            "period",
            "teamId",
            "teamTricode",
            "personId",
            "playerName",
            "playerNameI",
            "xLegacy",
            "yLegacy",
            "shotDistance",
            "shotResult",
            "isFieldGoal",
            "scoreHome",
            "scoreAway",
            "pointsTotal",
            "location",
            "description",
            "actionType",
            "subType",
            "videoAvailable",
            "actionId",
        ],
    }

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

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = {
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://www.nba.com',
            'Host': 'stats.nba.com',
            'User-Agent': random_agent,
            'Referer': 'https://www.nba.com/',
        }

    def __init__(
        self,
        game_id,
        end_period=EndPeriod.default,
        start_period=StartPeriod.default,
        proxy=None,
        headers=None,
        timeout=5,
        get_request=True,
    ):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
            "GameID": game_id,
            "EndPeriod": end_period,
            "StartPeriod": start_period,
        }
        if get_request:
            self.get_request()

    def get_random_agent(self):
        random_agent = self.USER_AGENTS[randint(0, len(self.USER_AGENTS) - 1)]
        ret = {
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://www.nba.com',
            'Host': 'stats.nba.com',
            'User-Agent': random_agent,
            'Referer': 'https://www.nba.com/',
        }
        return ret

    def get_request(self):
        attempts = 0
        while attempts < 3:  # Retry up to 3 times
            try:
                self.nba_response = NBAStatsHTTP().send_api_request(
                    endpoint=self.endpoint,
                    parameters=self.parameters,
                    proxy=self.proxy,
                    headers=self.headers,
                    timeout=self.timeout,
                )
                self.load_response()
            except TimeoutError:
                attempts += 1
                time.sleep(3)  # Wait for 1 second before retrying

    def load_response(self):
        data_sets = self.nba_response.get_data_sets(self.endpoint)
        self.data_sets = [
            Endpoint.DataSet(data=data_set)
            for data_set_name, data_set in data_sets.items()
        ]
        self.available_video = Endpoint.DataSet(data=data_sets["AvailableVideo"])
        self.play_by_play = Endpoint.DataSet(data=data_sets["PlayByPlay"])
