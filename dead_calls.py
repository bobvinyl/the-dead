import requests
from streamlit import json

class DeadCalls:
    def __init__(self, api_user:str, api_key:str):
        self.api_user = api_user
        self.api_key = api_key
        self.base_url = "https://api.gratefulstats.com/deadapi/v2/"

    def __do_get__(self, call_url:str) -> json:
        url = self.base_url + call_url
        response = requests.get(url, auth=(self.api_user, self.api_key))
        if response.status_code != 200:
            raise Exception(f"API call failed with status code {response.status_code}: {response.text}")
        return response.json()

    def Get_ShowsBy_Year(self, year:int) -> list[str]
        res = self.__do_get__(call_url=f"shows/year/{str(year)}")
        return [show.get("showId",None) for show in res.json()]
