from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm
from django.contrib.auth.decorators import login_required



def index(request):
    context = {

    }

    return render(request, 'index.html', context)


@login_required
def result(request):
	context = {
	
	}
	return render(request, 'result.html', context)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)

            return redirect("result")
        else:
            print(form.error_messages)
            form = RegistrationForm(request.POST)

    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, "register.html", context)


def logout_view(request):
	logout(request)
	return redirect("index")

def login_view(request):

	user = request.user
	if user.is_authenticated:
		return redirect("result")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user:
				login(request, user)
				return redirect("result")

	else:
		form = AccountAuthenticationForm()

	context = { 'form': form }

	return render(request, 'login.html', context)
