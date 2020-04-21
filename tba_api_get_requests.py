import requests
import json

def get_all_teams_at_event(event):
    """
    For a specified event, get data on all teams specified by that request.
    """
    key = {'X-TBA-Auth-Key': 'cxsuiGdMk5SJdtLDut0PlFovFmpvgOodGp6oT8eYOGsUVUZsHkQuGMSE3WIzNhkg'}
    r = requests.get(f"https://www.thebluealliance.com/api/v3/event/{event}/teams", params=key)
    j = r.json()
    with open(f"./{event}_all_teams_data_file.json", "w") as write_file:
        json.dump(j, write_file, indent=4)


def get_all_team_matches_at_event(team, event):
    """
    For a specified team and event, generate a JSON file in the current working directory
    with every match the team was in
    """
    key = {'X-TBA-Auth-Key': 'cxsuiGdMk5SJdtLDut0PlFovFmpvgOodGp6oT8eYOGsUVUZsHkQuGMSE3WIzNhkg'}
    r = requests.get(f"https://www.thebluealliance.com/api/v3/team/{team}/event/{event}/matches", params=key)
    j = r.json()
    with open(f"./{team}_{event}_data_file.json", "w") as write_file:
        json.dump(j, write_file, indent=4)

get_all_teams_at_event('2019wimi')
get_all_team_matches_at_event('frc3197', '2019wimi')