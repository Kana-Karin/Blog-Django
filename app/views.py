from django.shortcuts import render,redirect
from .models import Memo
from .forms import MemoForm
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    memos = Memo.objects.all().order_by("-updated_datatime")
    return render(request, 'app/index.html', { 'memos': memos })

def detail(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    return render(request, 'app/detail.html',{'memo':memo})

def post (request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:   
        form = MemoForm
    return render(request, 'app/post.html', {'form': form })

def about (request):
    return render(request, 'app/about.html')

@require_POST
def delete_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return redirect('app:index')