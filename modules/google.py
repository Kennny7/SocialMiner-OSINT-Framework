# modules/google.py
from googlesearch import search

class GoogleMiner:
    def find_profiles(self, name, location):
        dork = f'intext:"{name}" intext:"{location}" site:facebook.com | site:linkedin.com'
        return [result for result in search(dork, num=10, stop=10, pause=2.0)]