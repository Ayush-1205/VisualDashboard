import json
import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from dashboard.models import Data

with open('jsondata.json', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    added = datetime.strptime(item["added"], '%B, %d %Y %H:%M:%S') if item["added"] else None
    published = datetime.strptime(item["published"], '%B, %d %Y %H:%M:%S') if item["published"] else None
    
    Data.objects.create(
        end_year=item["end_year"] if item["end_year"] else None, 
        intensity=int(item["intensity"]) if item["intensity"] else None, 
        sector=item["sector"], 
        topic=item["topic"], 
        insight=item["insight"], 
        url=item["url"], 
        region=item["region"], 
        start_year=item["start_year"] if item["start_year"] else None, 
        impact=item["impact"], 
        added=added, 
        published=published, 
        country=item["country"], 
        relevance=int(item["relevance"]) if item["relevance"] else None, 
        pestle=item["pestle"], 
        source=item["source"], 
        title=item["title"], 
        likelihood=int(item["likelihood"]) if item["likelihood"] else None
    )
