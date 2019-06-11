from django.shortcuts import render

# Create function
def home(request):
    return render(request, 'home.html', {})
