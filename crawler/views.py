from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin 
from django.http import HttpResponse
from django.template import loader

def home(request):
    links = []
    titles=[]
    error = ''
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # base_url = url
            # for a_tag in soup.find_all('a', href=True):
            #     link = urljoin(base_url, a_tag['href'])  # ✅ Fixed Link
            #     links.append(link)
            for book in soup.find_all('h3'):
                title = book.find('a')['title']
                titles.append(title)

        except Exception as e:
            error = str(e)

    # return render(request, 'crawler/home.html', {'links': links, 'error': error})
    return render(request,'crawler/home.html',{'titles':titles,'errro':error})

def main(request):
    template=loader.get_template("crawler/main.html")
    return HttpResponse(template.render())