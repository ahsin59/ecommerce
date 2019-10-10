{"filter":false,"title":"views.py","tooltip":"/accounts/views.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":66,"column":61},"action":"remove","lines":["from django.shortcuts import render, redirect, reverse","from django.contrib import auth, messages","from django.contrib.auth.decorators import login_required","from django.contrib.auth.models import User","from accounts.forms import UserLoginForm, UserRegistrationForm","","","def index(request):","    \"\"\"Return the index.html file\"\"\"","    return render(request,  'index.html')","","@login_required","def logout(request):","    \"\"\"Log the user out\"\"\"","    auth.logout(request)","    messages.success(request, \"You have successfully been logged out\")","    return redirect(reverse('index'))","","","def login(request):","    \"\"\"Return a login page\"\"\"","    if request.user.is_authenticated:","        return redirect(reverse('index'))","    if request.method == \"POST\":","        login_form = UserLoginForm(request.POST)","","        if login_form.is_valid():","            user = auth.authenticate(username=request.POST['username'],","                                    password=request.POST['password'])","            messages.success(request, \"You have successfully logged in!\")","","            if user:","                auth.login(user=user, request=request)","                return redirect(reverse('index'))","            else:","                login_form.add_error(None, \"Your username or password is incorrect\")","    else:","        login_form = UserLoginForm()","    return render(request, 'login.html', {'login_form': login_form})","","def registration(request):","    \"\"\"Render the registration page\"\"\"","    if request.user.is_authenticated:","        return redirect(reverse('index'))","","    if request.method == \"POST\":","        registration_form = UserRegistrationForm(request.POST)","","        if registration_form.is_valid():","            registration_form.save()","","            user = auth.authenticate(username=request.POST['username'],","                                     password=request.POST['password1'])","            if user:","                auth.login(user=user, request=request)","                messages.success(request, \"You have successfully registered\")","            else:","                messages.error(request, \"Unable to register your account at this time\")","    else:","        registration_form = UserRegistrationForm()","    return render(request, 'registration.html', {","        \"registration_form\": registration_form})","        ","def user_profile(request):","    \"\"\"The user's profile page\"\"\"","    user = User.objects.get(email=request.user.email)","    return render(request, 'profile.html', {\"profile\": user})"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":74,"column":49},"action":"insert","lines":["from django.shortcuts import render, redirect, HttpResponseRedirect","from django.contrib import messages, auth","from django.core.urlresolvers import reverse","from .forms import UserLoginForm, UserRegistrationForm","from django.template.context_processors import csrf","from django.contrib.auth.decorators import login_required","","","# Create your views here.","def index(request):","    \"\"\"A view that displays the index page\"\"\"","    return render(request, \"index.html\")","","","def logout(request):","    \"\"\"A view that logs the user out and redirects back to the index page\"\"\"","    auth.logout(request)","    messages.success(request, 'You have successfully logged out')","    return redirect(reverse('index'))","","","def login(request):","    \"\"\"A view that manages the login form\"\"\"","    if request.method == 'POST':","        user_form = UserLoginForm(request.POST)","        if user_form.is_valid():","            user = auth.authenticate(request.POST['username_or_email'],","                                     password=request.POST['password'])","","            if user:","                auth.login(request, user)","                messages.error(request, \"You have successfully logged in\")","","                if request.GET and request.GET['next'] !='':","                    next = request.GET['next']","                    return HttpResponseRedirect(next)","                else:","                    return redirect(reverse('index'))","            else:","                user_form.add_error(None, \"Your username or password are incorrect\")","    else:","        user_form = UserLoginForm()","","    args = {'user_form': user_form, 'next': request.GET.get('next', '')}","    return render(request, 'login.html', args)","","","@login_required","def profile(request):","    \"\"\"A view that displays the profile page of a logged in user\"\"\"","    return render(request, 'profile.html')","","","def register(request):","    \"\"\"A view that manages the registration form\"\"\"","    if request.method == 'POST':","        user_form = UserRegistrationForm(request.POST)","        if user_form.is_valid():","            user_form.save()","","            user = auth.authenticate(request.POST.get('email'),","                                     password=request.POST.get('password1'))","","            if user:","                auth.login(request, user)","                messages.success(request, \"You have successfully registered\")","                return redirect(reverse('index'))","","            else:","                messages.error(request, \"unable to log you in at this time!\")","    else:","        user_form = UserRegistrationForm()","","    args = {'user_form': user_form}","    return render(request, 'register.html', args)"],"id":3}]]},"ace":{"folds":[],"scrolltop":256.79998779296875,"scrollleft":0,"selection":{"start":{"row":36,"column":21},"end":{"row":36,"column":21},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1570667606038,"hash":"bdb15b7df92867ac9f302cf5b1f886cd3bcf8013"}