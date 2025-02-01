from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache

class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'

        faqs = cache.get(cache_key)
        if not faqs:
            faqs = list(FAQ.objects.all())
            cache.set(cache_key, faqs, timeout=3600)  # Cache for 1 hour

        return faqs
