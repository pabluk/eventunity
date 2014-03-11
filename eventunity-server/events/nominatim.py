import requests


class Geocoder(object):
    """
    A simple class to use the Nominatim API
    http://wiki.openstreetmap.org/wiki/Search
    """
    url = 'http://nominatim.openstreetmap.org/search'
    user_agent = 'Eventunity/0.2 (+http://eventunity.seminar.io; ' \
                 'eventunity@seminar.io)'

    def search(self, name):
        """Search location by name and only returns the first city."""
        params = {'q': name, 'format': 'json'}
        headers = {'User-Agent': self.user_agent}

        location = {'name': u'', 'coordinates': None}
        r = requests.get(self.url, params=params, headers=headers)
        for l in r.json():
            # Filter cities
            if l['type'] in [u'city', u'administrative']:
                location = {
                    'name': l['display_name'],
                    'coordinates': [l['lat'], l['lon']]
                }
                break
        return location


if __name__ == '__main__':
    g = Geocoder()
    location = g.search("Nantes, France")
    assert location['coordinates'] == [u'47.2185155', u'-1.5545147']
