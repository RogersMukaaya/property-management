from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
from django.shortcuts import render

from .models import Listing

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)

    page = request.GET.get('page')

    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    # Check if listing is available or throw a 404
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    querySet_list = Listing.objects.order_by('-list_date')

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
          #See if any of the listing in the listings contains anything being searched  
          querySet_list = querySet_list.filter(description__icontains=keywords)  
             

    context = {
        'listings':  querySet_list
    }
     
    return render(request, 'listings/search.html', context)
