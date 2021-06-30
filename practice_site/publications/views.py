from django.shortcuts import render


# Create your views here.
def publications_list(request):
  return render(request, 'publications/publications_list.html', {})
