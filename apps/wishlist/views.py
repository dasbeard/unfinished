from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . import models
from .models import Products
from ..loginReg.models import Users
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    if 'logged_user' not in request.session:
        return redirect(reverse('users:index'))
    else:
        users_id = request.session['logged_user']
        user = models.Users.objects.filter(pk=users_id)
        myList =  models.Products.objects.filter(wish__id=users_id)
        wishes = models.Products.objects.all().filter(wish=user)
        othersList = models.Products.objects.all().order_by('created_at').exclude(wish=users_id)
        context = {
        'user': user[0],
        'myList':myList,
        'othersList':othersList,
        'wishes':wishes,
        }
    return render(request, 'wishlist/index.html', context)

def delete(request, id):

    item = models.Products.objects.get(id=id)
    context = {
        'item':item,
    }
    item.delete()
    return redirect(reverse('wishlist:index'))

def wishlist(request, id):
    users_id = request.session['logged_user']
    user = models.Users.objects.filter(pk=users_id)
    item = models.Products.objects.get(id=id)
    # myList =  models.Products.objects.filter(wish__id=users_id)
    wishes = models.Products.objects.all().filter(wish=user)
    othersList = models.Products.objects.exclude(wish__id=users_id)
    # print item.wish.all()
    context = {
    'item': item,
    'user': user[0],
    # 'myList':myList,
    'othersList':othersList,
    'wishes':wishes,
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

def create(request):
    if 'logged_user' not in request.session:
        return redirect(reverse('users:index'))
    else:
        users_id = request.session['logged_user']
        user = models.Users.objects.get(pk=users_id)
        wishItem = request.POST['product']
        if len(wishItem)<1:
            messages.error(request, "Wish can not be blank")
            return redirect('/wishlist/add_item/'+str(users_id))

        add_item = models.Products.objects.create(name=wishItem, user=user)
        add_item.wish.add(user)
        add_item.save()

    return redirect (reverse('wishlist:index'))

def add_wish(request, id):
    user = models.Users.objects.get(pk=request.session['logged_user'])
    item = models.Products.objects.get(pk=id)
    item.wish.add(user)
    item.save()
    return redirect(reverse('wishlist:index'))

def remove(request, id):
    user = models.Users.objects.get(pk=request.session['logged_user'])
    item = models.Products.objects.get(id=id)
    item.wish.remove(user)
    item.save()

    return redirect(reverse('wishlist:index'))
