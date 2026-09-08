from django.shortcuts import render, redirect

def index(request):
    if 'visits' not in request.session:
        request.session['visits'] = 0
    if 'counter' not in request.session:
        request.session['counter'] = 0
    
    request.session['visits'] += 1
    request.session['counter'] += 1

    return render(request,"index.html")


def destroy_session(request):
    request.session.clear()
    return redirect('/')


def add_two(request):
    request.session['counter'] += 1
    return redirect('/')


def reset(request):
    request.session['counter'] = -1
    return redirect('/')


def custom_increment(request):
    if request.method == "POST":
        increment_value = int(request.POST['increment'])
        request.session['counter'] += (increment_value - 1)
        return redirect('/')