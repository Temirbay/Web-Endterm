from django.shortcuts import render

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from api.models import Blog
from api.serializers import BlogSerializer

@csrf_exempt
def blog_list (request):

    if request.method == 'GET':
        blogs = Blog.objects.all()
        ser = BlogSerializer(blogs, many=True)
        return JsonResponse(ser.data, safe=False) 
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser = BlogSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
    
    return JsonResponse(ser.errors, status=400)


@csrf_exempt
def blog_detail(request, blog_id):
    
    blog = Blog.objects.get(pk=blog_id)
    
    if request.method == "GET":
        ser = BlogSerializer(blog)
        return JsonResponse(ser.data) 

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        ser = BlogSerializer(blog, data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data)

    elif request.method == "DELETE":
        blog.delete()
        ser = BlogSerializer(blog)
        return JsonResponse(ser.data)
