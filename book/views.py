from django.shortcuts import render

# Create your views here.

def booking(request):
    if request.method == 'POST':
        print('FORM DATA:', request.POST)
    return render(request, 'book/booking.html')
