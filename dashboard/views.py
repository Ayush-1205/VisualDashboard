from django.shortcuts import render
from django.http import JsonResponse
from .models import Data


def get_data(request):
    data = Data.objects.all()
    response_data = []
    for item in data:
        response_data.append({
            'end_year': item.end_year,
            'intensity': item.intensity,
            'sector': item.sector,
            'topic': item.topic,
            'insight': item.insight,
            'url': item.url,
            'region': item.region,
            'start_year': item.start_year,
            'impact': item.impact,
            'added': item.added,
            'published': item.published,
            'country': item.country,
            'relevance': item.relevance,
            'pestle': item.pestle,
            'source': item.source,
            'title': item.title,
            'likelihood': item.likelihood,
        })
    return JsonResponse(response_data, safe=False)
def get_filter_options(request):
    end_years = Data.objects.values_list('end_year', flat=True).distinct()
    topics = Data.objects.values_list('topic', flat=True).distinct()
    sectors = Data.objects.values_list('sector', flat=True).distinct()
    regions = Data.objects.values_list('region', flat=True).distinct()
    pestles = Data.objects.values_list('pestle', flat=True).distinct()
    sources = Data.objects.values_list('source', flat=True).distinct()
    swots = Data.objects.values_list('insight', flat=True).distinct()  # Assuming insight is used as SWOT
    countries = Data.objects.values_list('country', flat=True).distinct()
    cities = Data.objects.values_list('title', flat=True).distinct()  # Assuming title is used as city

    data = {
        'endYear': list(filter(None, end_years)),
        'topic': list(filter(None, topics)),
        'sector': list(filter(None, sectors)),
        'region': list(filter(None, regions)),
        'pestle': list(filter(None, pestles)),
        'source': list(filter(None, sources)),
        'swot': list(filter(None, swots)),
        'country': list(filter(None, countries)),
        'city': list(filter(None, cities)),
    }

    return JsonResponse(data)