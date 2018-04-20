from django.shortcuts import render, redirect

from app.models import Blog

def blog_list (request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render (request, 'blog/blog_list.html', {"blogs": blogs})
     
def blog_details (request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render (request, 'blog/blog_details.html', {"blog": blog})

def blog_add (request):
    if (request.method == 'POST'):
        title = request.POST['title']
        body = request.POST['body']
        blog = Blog (title=title, body=body)
        blog.save()
        return redirect('/blogs')
    else:
        return render(request, "blog/blog_add.html")

def blog_update (request, blog_id):
    blog = Blog.objects.get (pk=blog_id)
    
    if (request.method == 'POST'):
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()
        return redirect('/blogs')
    else:
        return render(request, "blog/blog_update.html", {"blog": blog})
    
def blog_delete (request, blog_id):
    blog = Blog.objects.get (pk=blog_id)
    blog.delete()
    return redirect('/blogs/')
    