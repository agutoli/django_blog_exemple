# Create your views here.
from django.template import Context, loader
from agutoli.blog.models import Post, Category
from django.http import HttpResponse

def index(request):
    posts_list = Post.objects.filter(published=True)
    category_list = Category.objects.all()
    t = loader.get_template('blog/index.html')
    c = Context({
        'posts_list': posts_list,
        'category_list': category_list
    })
    return HttpResponse(t.render(c))

def detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        t = loader.get_template('blog/detail.html')
    except Post.DoesNotExist:
        post = None
        t = loader.get_template('blog/404.html')
    category_list = Category.objects.all()
    c = Context({
        'post': post,
        'category_list': category_list
    })
    return HttpResponse(t.render(c))
