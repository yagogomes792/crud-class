from django.shortcuts import render, redirect
from .models import Books
from .forms import BookForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {}
    data['books'] = Books.objects.all()
    return render(request, 'index.html', data)

def create(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("""Is there something wrong with your template, please reload on <a href="{{url:'index}}">reload</a>""")
    else:
        return render(request, 'create.html', {'form':form})

def update(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Books.objects.get(id=book_id)
    except Books.DoesNotExist:
        return render ('index')
    book_form = BookForm(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request, 'create.html', {'form':book_form})

def delete(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Books.objects.get(id=book_id)
    except Books.DoesNotExist:
        return render('index')
    book_sel.delete()
    return redirect('index')
