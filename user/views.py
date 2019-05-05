from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def post_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = ItemForm()
    return render(request, 'item/add_item.html', {'form': form})