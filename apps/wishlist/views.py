from django.shortcuts import render, redirect, HttpResponse
from . import models
from .models import Products
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    if 'logged_user' not in request.session:
        return redirect(reverse('users:index'))
    else:
        users_id = request.session['logged_user']
        user = models.Users.objects.filter(pk=users_id)
        wishlist = models.Products.objects.all().order_by('created_at')

        context = {
        'wishlist':wishlist,
        'user': user[0],
        }
    return render(request, 'wishlist/index.html', context)


def remove(request, id):
    item = models.Products.objects.get(id=id)
    context = {'item':item}

    item.delete()
    return redirect(reverse('wishlist:index'))


def wishlist(request, id):
    item = models.Products.objects.get(id=id)

    context = {
    'item':item
    }


    return render (request, 'wishlist/wish_items.html', context)


def add_item(request, id):
    if 'logged_user' not in request.session:
        return redirect(reverse('users:index'))
    else:
        users_id = request.session['logged_user']
        user = models.Users.objects.filter(pk=users_id)

        context = {'user': user[0],}

    return render(request, 'wishlist/create.html', context)




def create_item(request):
    if 'logged_user' not in request.session:
        return redirect(reverse('users:index'))
    else:
        users_id = request.session['logged_user']
        user = models.Users.objects.filter(pk=users_id)

        wishItem = request.POST['product']
        add_item = models.Products(name=wishItem)
        add_item.save()

    return redirect (reverse('wishlist:index'))
