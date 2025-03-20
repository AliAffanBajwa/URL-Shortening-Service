from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ShortURL
from .serializers import ShortURLSerializer
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class ShortenURLView(APIView):
    def post(self, request):
        data = request.data.copy()
        if 'url' not in data and 'original_url' in data:
            data['url'] = data['original_url']
            
        serializer = ShortURLSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'id': str(serializer.data['id']),
                'url': serializer.data['url'],
                'shortCode': serializer.data['short_code'],
                'createdAt': serializer.data['created_at'],
                'updatedAt': serializer.data['updated_at']
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@method_decorator(csrf_exempt, name='dispatch')
class URLDetailView(APIView):
    def get_object(self, short_code):
        return get_object_or_404(ShortURL, short_code=short_code)
    
    def get(self, request, short_code):
        url = self.get_object(short_code)
        serializer = ShortURLSerializer(url)
        return Response(serializer.data)
    
    def put(self, request, short_code):
        url = self.get_object(short_code)
        serializer = ShortURLSerializer(url, data=request.data, partial=True)
        
        if serializer.is_valid():
            new_url = request.data.get('url')
            if new_url and new_url != url.original_url:
                url.short_code = url.generate_short_code()  
            serializer.save()
            
            response_data = {
                'id': str(url.id),
                'url': url.original_url,
                'shortCode': url.short_code,
                'createdAt': url.created_at.isoformat() + 'Z',
                'updatedAt': url.updated_at.isoformat() + 'Z'
            }
            return Response(response_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, short_code):
        try:
            url = ShortURL.objects.get(short_code=short_code)
            url.delete()
            return Response(
                {"message": f"Short URL '{short_code}' successfully deleted"},
                status=status.HTTP_204_NO_CONTENT
            )
        except ShortURL.DoesNotExist:
            return Response(
                {"message": f"Short URL '{short_code}' not found"},
                status=status.HTTP_404_NOT_FOUND
            )
    
class URLRedirectView(APIView):
    def get(self, request, short_code):
        url = get_object_or_404(ShortURL, short_code=short_code)
        url.access_count += 1
        url.save()
        return HttpResponseRedirect(url.original_url)
    
class URLStatsView(APIView):
    def get(self, request, short_code):
        url = get_object_or_404(ShortURL, short_code=short_code)
        serializer = ShortURLSerializer(url)
        return Response({
            'id': str(url.id),
            'url': url.original_url,
            'shortCode': url.short_code,
            'createdAt': url.created_at.isoformat() + 'Z',
            'updatedAt': url.updated_at.isoformat() + 'Z',
            'accessCount': url.access_count
        })

class StatsView(TemplateView):
    template_name = "shortener/stats.html"