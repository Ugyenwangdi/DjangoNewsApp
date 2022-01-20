from django.shortcuts import render
from newsapi import NewsApiClient 

# Create your views here.
def home(request):

    newsapi = NewsApiClient(api_key='815257c1744f4713ad80335dace16ff9')
    # topnews = newsapi.get_sources(country='cnn') 

    filter = request.GET.get('query')    
    # print(filter)

    try:
        if filter == None:
            filter = ''
            topnews = newsapi.get_top_headlines(sources='cnn')   # source=ndtv, bbc-news, cnn,techcrunch,foxnews.
        else:
            if 'country=' in filter:
                filter = filter.replace('country=', '')
                print(filter)
                topnews = newsapi.get_top_headlines(country=filter)   # source=ndtv, bbc-news, cnn,techcrunch,foxnews.
            elif 'category=' in filter:
                filter = filter.replace('category=', '')
                print(filter)
                topnews = newsapi.get_top_headlines(category=filter)   # source=ndtv, bbc-news, cnn,techcrunch,foxnews.

        latest = topnews['articles']
        print(topnews)
        # print(latest)

        
        title = []
        desc = []
        url = []
        author = []
        date = []

        for i in range(len(latest)):
            news = latest[i]
            
            title.append(news['title'])
            desc.append(news['description'])
            url.append(news['url'])
            author.append(news['author'])
            date.append(news['publishedAt'])

        all_news = zip(title, desc, url, author, date)

        context = {
            'all_news': all_news
        }

        return render(request, "index.html", context)

    except:
        return render(request, "index.html", {"error":"Sorry the number of requests has reached to its limit"})
        print("Sorry the number of requests has reached to its limit")

