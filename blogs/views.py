from django.http import HttpResponse
from django.template import loader
from .models import User,Blog
# Create your views here.
def blog(request):
    return HttpResponse('blog')
def home(request):
    
        me = User.objects.all().values()[0]
        blogs = Blog.objects.all().values()
        Home = loader.get_template('Home.html')
        context = {
            'user':me,
            'blogs':blogs
        }
        return HttpResponse(Home.render(context,request))

def signup(request):
    Signup = loader.get_template('Signup.html')
    return HttpResponse(Signup.render())
def login(request):
    Login = loader.get_template('Login.html')
    return HttpResponse(Login.render())
def profile(request,name):
    try:
        user = User.objects.get(username=name)
        Profile = loader.get_template('Profile.html')
        return HttpResponse(Profile.render({'user':user},request))
    except:
        return HttpResponse('User Not Found')