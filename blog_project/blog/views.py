import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import BlogPost



def detect_country_view(request):
   
    def get_public_ip():
        url = "https://api.ipify.org?format=json"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json().get('ip')
            else:
                return None
        except Exception as e:
            print(f"Error fetching IP address: {e}")
            return None

  
    def get_user_country(ip_address):
        url = f"http://ip-api.com/json/{ip_address}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                country = response.json().get('country', 'Unknown')
                return country
            else:
                return 'Unknown'
        except Exception as e:
            print(f"Error fetching country: {e}")
            return 'Unknown'

   
    ip_address = get_public_ip()
    
    if ip_address:
       
        detected_country = get_user_country(ip_address)
    else:
        detected_country = 'Unknown'

  
    blog_posts = BlogPost.objects.all()

 
    return render(request, 'blog/index.html', {
        'country': detected_country,
        'blog_posts': blog_posts
    })
    
    
def filter_blog_posts_view(request):

    country = request.GET.get('country', None)
    if country and country != 'All':
        blog_posts = BlogPost.objects.filter(country__iexact=country)
    else:
        blog_posts = BlogPost.objects.all()

    data = [
        {'title': post.title, 'content': post.content, 'country': post.country}
        for post in blog_posts
    ]

    return JsonResponse({'blog_posts': data})
