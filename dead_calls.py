import requests
import json
from dead_objects import DEAD_SONG, DEAD_SHOW

class DeadCalls:
    def __init__(self, api_user:str, api_key:str):
        self.api_user = api_user
        self.api_key = api_key
        self.headers = {'apiKey': self.api_key, 'apiUserId': self.api_user}
        self.base_url = "https://api.gratefulstats.com/deadapi/v2/"

    def __do_get__(self, call_url:str) -> json:
        url = self.base_url + call_url
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"API call failed with status code {response.status_code}: {response.text}")
        return response.json()

    def Get_Tunes(self):
        tunes = self.__do_get__('tunes/gettunes')['alltunes']
        return [DEAD_SONG(**tune) for tune in tunes]
    
    def Get_Shows_By_Year(self, year:int) -> list[str]:
        res = self.__do_get__(call_url=f"years/getyeardata/{str(year)}")
        shows = res.get("ShowsOneYear")
        return [show.get("showId",None) for show in shows]
    
    def Get_Show(self, showId:str) -> DEAD_SHOW:
        res = self.__do_get__(call_url=f'shows/getshowdatabyshowid/{showId}')
        return DEAD_SHOW(**res[0])
    
    def Test_Key(self):
        res = requests.get(self.base_url + "keytest/validatekey", headers=self.headers)
        return res.text

