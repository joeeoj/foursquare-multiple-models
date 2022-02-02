import requests
class Client:
    CLIENT_ID = "ALECV5CBBEHRRKTIQ5ZV143YEXOH3SBLAMU54SPHKGZI1ZKE"
    CLIENT_SECRET = "3JX3NRGRS2P0KE0NSKPTMCOZOY4MWUU4M3G33BO4XTRJ15SM"
    DATE = "20190407"
    URL = "https://api.foursquare.com/v2/venues/search"
    SHOW_URL = "https://api.foursquare.com/v2/venues"

    def auth_params(self):
        return {'client_id': self.CLIENT_ID,
                   'client_secret': self.CLIENT_SECRET,
                   'v': self.DATE}

    def full_params(self, query_params = {'ll': "40.7,-74", "query": "tacos"}):
        params = self.auth_params().copy()
        params.update(query_params)
        return params

    def request_venues(self):
        response = requests.get(self.URL, self.full_params())
        return response.json()['response']['venues']

    def request_venue(self, venue_id):
        response = requests.get(f"{self.SHOW_URL}/{venue_id}", self.auth_params())
        return response.json()['response']['venue']