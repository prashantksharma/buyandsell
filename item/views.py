from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemForm
from django.utils import timezone
from django.shortcuts import redirect
from .models import Item

# Create your views here.


def check(request):
	return HttpResponse("Fuck")


def post_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
            #return HttpResponse(""+str(post))
    else:
        form = ItemForm()
    return render(request, 'item/add_item.html', {'form': form})


def item_list(request):
    item_list = Item.objects.all()
    return render(request, "item/item_list.html", {"item_list": item_list})
