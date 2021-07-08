from django.shortcuts import render, get_object_or_404
from .models import PublicationsItem

# Create your views here.
def publications_list(request):
  publications_items = PublicationsItem.objects.all().order_by('published_date')
  return render(request, 'pages/publications_list.html', {'publications_items': publications_items})

def publications_item_detail(request, pk):
  publications_item = get_object_or_404(PublicationsItem, pk=pk)
  return render(request, 'pages/publications_item.html', {'publications_item': publications_item})