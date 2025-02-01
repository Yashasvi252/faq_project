from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()

    def get_question(self, obj):
        lang = self.context.get('request').query_params.get('lang', 'en')
        return obj.get_question_by_lang(lang)

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']
