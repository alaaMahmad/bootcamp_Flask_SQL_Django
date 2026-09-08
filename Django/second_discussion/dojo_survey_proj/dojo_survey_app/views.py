from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST.get('name')
        request.session['location'] = request.POST.get('location')
        request.session['language'] = request.POST.get('language')
        request.session['experience'] = request.POST.get('experience', 'Not specified')
        request.session['skills'] = request.POST.getlist('skills')
        request.session['comment'] = request.POST.get('comment', '')
        return redirect('/result')
    return redirect('/')

def result(request):
    return render(request, 'result.html')