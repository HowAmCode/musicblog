from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(expires__gte=timezone.now()).filter(published_date__lte=timezone.now()).order_by('-published_date')
	
    features = Post.objects.filter(published_date__lte=timezone.now()).filter(featured=1).order_by('-published_date')	
	
    context = {
		'posts': posts, 
		'features':features
	}
	
    return render(request, 'blog/post_list.html', context)
	

def post_list_toronto(request):
    posts = Post.objects.filter(expires__gte=timezone.now()).filter(published_date__lte=timezone.now()).filter(city='Toronto').order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
	
def about_us(request):
	return render(request, 'blog/about_us.html', {})
	

