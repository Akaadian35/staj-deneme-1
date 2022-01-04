from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mysite.models import Post, Category, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def index(request):
    context = dict()
    post_list = Post.objects.all()

    query = request.GET.get('q')

    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(user__first_name__icontains=query)
        ).distinct()

    paginator = Paginator(post_list, 3)  # bir sayfada kaç tane görünmesi gerek
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:

        posts = paginator.page(1)
    except EmptyPage:

        posts = paginator.page(paginator.num_pages)

    context['posts'] = posts
    context['post_list'] = Post.objects.distinct()
    context['cat'] = Category.objects.all()
    context['popular_list'] = Post.objects.all().order_by('-read', '-id')[:3]

    return render(request, 'index.html', context)


class CommentForm:
    def is_valid(self):
        pass

    def save(self, commit):
        pass


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())

    read = post.read
    read += 1
    Post.objects.filter(slug=slug).update(read=read)

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'detail.html', context)
