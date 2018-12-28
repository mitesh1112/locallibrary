from django.shortcuts import render

# Create your views here.

from catalog.models import Author, Book, BookInstance, Genre

def index(request):
    """View function for the homepage of the site"""

    # Generate count of some of the main objects
    num_book = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

    # The 'all()' is implied by default
    num_authors = Author.objects.count()

    context = {
        'num_book' : num_book,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)