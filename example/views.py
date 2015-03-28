from django.shortcuts import render_to_response
from example.forms import SampleModelForm


def home(request):
    form = SampleModelForm()
    return render_to_response('example/home.html', {'form': form})
