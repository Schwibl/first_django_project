from django.shortcuts import render
from .models import PublicationsItem

# Create your views here.
def publications_list(request):
  publications_items = PublicationsItem.objects.all().order_by('published_date')
  return render(request, 'publications/publications_list.html', {'publications_items': publications_items})
