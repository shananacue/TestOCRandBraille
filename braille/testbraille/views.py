from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Text
from .forms import TestForm
# Create your views here.

class TestsView(ListView):
    model = Text 
    template_name = 'test.html'

class TestDetailView(DetailView):
    model = Text
    template_name= 'test_details.html'
    context_object_name = 't'

class AddTestView(CreateView):
    model = Text
    form_class = TestForm
    template_name = 'add_test.html'
    #fields = '__all__'


def image(request):
 
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TestForm()
    return render(request, 'add_test.html', {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')