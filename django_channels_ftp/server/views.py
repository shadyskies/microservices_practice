from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document



def home(request):
    return render(request, 'server/home.html')

def handle_uploaded_file(f):
    with open('some_file.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def file_upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print(f"request files: {request.FILES}")
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            handle_uploaded_file(request.FILES['docfile'])
            return redirect('home')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    
    # Render list page with the documents and the form
    return render(request,'server/file.html',{'form': form}
    )