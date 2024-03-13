from nba_api.stats.endpoints import teamdetails, commonplayerinfo, teamgamelogs, playbyplayv3
import json
from nba_api.stats.static import teams


custom_headers = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

# Only available after v1.1.0
# Proxy Support, Custom Headers Support, Timeout Support (in seconds)
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544, proxy='127.0.0.1:80', headers=custom_headers, timeout=100)

# print(teams.get_teams())

team_list = []
i=0
for team in teams.get_teams():
    i+=1
    print(team['id'], team['full_name'])
    team_list.append([team['id'], team['full_name']])



def convert_json_string_to_json(json_string):
    try:
        json_object = json.loads(json_string)
        return json_object
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
game_info_str = playbyplayv3.PlayByPlayV3(end_period=1, game_id="0021700807", start_period=1).get_json()
game_json = convert_json_string_to_json(game_info_str)
print(converted_json["game"]["gameId"])

celtics_id=0
#one line python function to get the team boston celtics from the object game_json
for team in team_list:
    if team[1]=="Boston Celtics":
        print(team[0])
        celtics_id = team[0]


gameLog = convert_json_string_to_json(teamgamelogs.TeamGameLog(date_from="", date_to="", season="2021-22", season_type_all_star="Regular Season", team_id=celtics_id, league_id=0))
