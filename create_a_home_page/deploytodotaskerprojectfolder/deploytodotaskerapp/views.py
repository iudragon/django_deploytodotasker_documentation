from django.shortcuts import render

# Create a home page --> Create function
def home(request):
    return render(request, 'home.html', {})
    # {} is empty because we do not have any data to pass to the Front End
# Create a home page --> Create function
