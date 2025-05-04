# intelligence/pattern_analyzer.py
from datetime import datetime

class BehaviorProfiler:
    def detect_work_schedule(self, post_times):
        """Identify 9-5 patterns from posting times"""
        work_hours = [t for t in post_times if 9 <= t.hour < 17]
        return len(work_hours)/len(post_times) > 0.8  # 80%+ daytime activity

# modules/instagram.py
from instaloader import Instaloader, Profile

class InstagramMiner:
    def get_geo_patterns(self, username):
        L = Instaloader()
        profile = Profile.from_username(L.context, username)
        
        locations = []
        for post in profile.get_posts():
            if post.location:
                locations.append(post.location.name)  # Publicly available data
        
        return self._cluster_locations(locations)  # No private API calls