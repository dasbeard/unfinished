from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Users



# Create your views here.
def index(request):
    if 'logged_user' in request.session:
        return redirect(reverse('wishlist:index'))

    return render(request, 'loginReg/index.html')

def success(request):
    if 'logged_user' not in request.session:
        return redirect(reverse('users:index'))
    user = Users.objects.get(id=request.session['logged_user'])
    return redirect(reverse ('wishlist:index'), {'user':user})

def signout(request):
    request.session.pop('logged_user', None)
    return redirect(reverse('users:index'))





def register(request):
    if request.method == 'POST':
        form = request.POST
        errors = Users.objects.validateRegistration(form)

        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            if Users.objects.register(form):
                messages.success(request, "Successfully created account!")
            else:
                messages.error(request, "Something went wrong")
    return redirect(reverse('users:index'))

def login(request):
    form = request.POST
    if request.method != "POST":
        return redirect(reverse('users:index'))
    elif len(form['username'])<3:
        messages.error(request, "Please enter a valid username")
        return redirect(reverse('users:index'))
    elif len(form['password']) == 0:
        messages.error(request, "Please enter a password")
        return redirect(reverse('users:index'))


    user = Users.objects.check_login(request.POST)
    if user:
        request.session['logged_user'] = user.id
        return redirect(reverse ('wishlist:index'),{'user':user})

    else:
        messages.error(request, "Login or Password do not match")
        return redirect(reverse('users:index'))
