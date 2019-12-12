{"filter":false,"title":"views.py","tooltip":"/accounts/views.py","undoManager":{"mark":42,"position":42,"stack":[[{"start":{"row":3,"column":0},"end":{"row":5,"column":58},"action":"insert","lines":["# Create your views here.","def index(request):","    return render(request, \"accounts/index.template.html\")"],"id":2}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":25},"action":"remove","lines":["# Create your views here."],"id":3},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":4,"column":50},"end":{"row":4,"column":51},"action":"remove","lines":["e"],"id":4},{"start":{"row":4,"column":49},"end":{"row":4,"column":50},"action":"remove","lines":["t"]},{"start":{"row":4,"column":48},"end":{"row":4,"column":49},"action":"remove","lines":["a"]},{"start":{"row":4,"column":47},"end":{"row":4,"column":48},"action":"remove","lines":["l"]},{"start":{"row":4,"column":46},"end":{"row":4,"column":47},"action":"remove","lines":["p"]},{"start":{"row":4,"column":45},"end":{"row":4,"column":46},"action":"remove","lines":["m"]},{"start":{"row":4,"column":44},"end":{"row":4,"column":45},"action":"remove","lines":["e"]},{"start":{"row":4,"column":43},"end":{"row":4,"column":44},"action":"remove","lines":["t"]}],[{"start":{"row":4,"column":42},"end":{"row":4,"column":43},"action":"remove","lines":["."],"id":5}],[{"start":{"row":4,"column":49},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"remove","lines":["    "],"id":7}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":6,"column":0},"end":{"row":12,"column":26},"action":"insert","lines":["\"\"\"","This is the logout function","\"\"\"","def logout(request):","    auth.logout(request)","    messages.success(request, \"You have been logged out\")","    return redirect(index)"],"id":9}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":12},"action":"remove","lines":["This is the "],"id":10}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":35},"action":"remove","lines":["from django.shortcuts import render"],"id":11},{"start":{"row":0,"column":0},"end":{"row":2,"column":54},"action":"insert","lines":["from django.shortcuts import render, redirect, reverse, HttpResponse","from django.contrib import auth, messages","from .forms import UserLoginForm, UserRegistrationForm"]}],[{"start":{"row":13,"column":31},"end":{"row":13,"column":55},"action":"remove","lines":["You have been logged out"],"id":12},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":["L"]},{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"insert","lines":["o"]},{"start":{"row":13,"column":33},"end":{"row":13,"column":34},"action":"insert","lines":["g"]},{"start":{"row":13,"column":34},"end":{"row":13,"column":35},"action":"insert","lines":["g"]},{"start":{"row":13,"column":35},"end":{"row":13,"column":36},"action":"insert","lines":["e"]},{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"insert","lines":["d"]}],[{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"insert","lines":[" "],"id":13},{"start":{"row":13,"column":38},"end":{"row":13,"column":39},"action":"insert","lines":["o"]},{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"insert","lines":["u"]},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":41},"end":{"row":13,"column":42},"action":"insert","lines":[" "],"id":14},{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"insert","lines":["s"]},{"start":{"row":13,"column":43},"end":{"row":13,"column":44},"action":"insert","lines":["u"]},{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"insert","lines":["c"]},{"start":{"row":13,"column":45},"end":{"row":13,"column":46},"action":"insert","lines":["c"]}],[{"start":{"row":13,"column":46},"end":{"row":13,"column":47},"action":"insert","lines":["e"],"id":15},{"start":{"row":13,"column":47},"end":{"row":13,"column":48},"action":"insert","lines":["s"]},{"start":{"row":13,"column":48},"end":{"row":13,"column":49},"action":"insert","lines":["s"]},{"start":{"row":13,"column":49},"end":{"row":13,"column":50},"action":"insert","lines":["f"]},{"start":{"row":13,"column":50},"end":{"row":13,"column":51},"action":"insert","lines":["u"]},{"start":{"row":13,"column":51},"end":{"row":13,"column":52},"action":"insert","lines":["l"]},{"start":{"row":13,"column":52},"end":{"row":13,"column":53},"action":"insert","lines":["l"]},{"start":{"row":13,"column":53},"end":{"row":13,"column":54},"action":"insert","lines":["y"]}],[{"start":{"row":13,"column":54},"end":{"row":13,"column":55},"action":"insert","lines":[" "],"id":16},{"start":{"row":13,"column":55},"end":{"row":13,"column":56},"action":"insert","lines":["!"]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":54},"action":"remove","lines":["from .forms import UserLoginForm, UserRegistrationForm"],"id":17}],[{"start":{"row":14,"column":26},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":4},"end":{"row":16,"column":0},"action":"insert","lines":["",""]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "],"id":19}],[{"start":{"row":16,"column":0},"end":{"row":67,"column":10},"action":"insert","lines":["\"\"\"","This is login function","\"\"\"","def login(request):","    if request.method == \"POST\":","        # populate the login form with the user's input","        login_form = UserLoginForm(request.POST)","        ","        # if the input to the login form is valid","        if login_form.is_valid():","            # use auth.authenticate to check if the","            # user name and password matches","            user = auth.authenticate(username=request.POST['username'],","                                     password=request.POST['password'])","            #if there is a user (meaning, user is not None)","            if user:","                auth.login(user=user, request=request)","                return redirect(reverse('index'))","    else:","        form = UserLoginForm()","        return render(request, 'accounts/login.template.html', {","            'form':form","        })","        ","@login_required","def profile(request):","    return HttpResponse(\"Profile\")","    ","def register(request):","    if request.method == \"POST\":","        form = UserRegistrationForm(request.POST)","        if form.is_valid():","            form.save()","            # check if the username and password matches","            user = auth.authenticate(username=request.POST['username'],","                                     password=request.POST['password1'])","            if user:","                # actually log the user in","                auth.login(user=user, request=request)","                messages.success(request, \"You have registered successful\")","            else:","                messages.error(request, \"You failed to register\")","            return redirect(reverse('index'))","        else:","            return render(request, \"accounts/register.template.html\",{","                'form': form","            })","    else:","        register_form = UserRegistrationForm()","        return render(request, \"accounts/register.template.html\", {","            'form': register_form","        })"],"id":20}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render, redirect, reverse, HttpResponse","from django.contrib import auth, messages","",""],"id":21},{"start":{"row":0,"column":0},"end":{"row":6,"column":57},"action":"insert","lines":["","from django.shortcuts import render, redirect, reverse, HttpResponse","from django.contrib import auth, messages","from .forms import UserLoginForm, UserRegistrationForm","","# import in the login_required annonation","from django.contrib.auth.decorators import login_required"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":22}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":23}],[{"start":{"row":39,"column":54},"end":{"row":39,"column":55},"action":"remove","lines":["e"],"id":24},{"start":{"row":39,"column":53},"end":{"row":39,"column":54},"action":"remove","lines":["t"]},{"start":{"row":39,"column":52},"end":{"row":39,"column":53},"action":"remove","lines":["a"]},{"start":{"row":39,"column":51},"end":{"row":39,"column":52},"action":"remove","lines":["l"]},{"start":{"row":39,"column":50},"end":{"row":39,"column":51},"action":"remove","lines":["p"]},{"start":{"row":39,"column":49},"end":{"row":39,"column":50},"action":"remove","lines":["m"]},{"start":{"row":39,"column":48},"end":{"row":39,"column":49},"action":"remove","lines":["e"]},{"start":{"row":39,"column":47},"end":{"row":39,"column":48},"action":"remove","lines":["t"]}],[{"start":{"row":39,"column":46},"end":{"row":39,"column":47},"action":"remove","lines":["."],"id":25}],[{"start":{"row":23,"column":4},"end":{"row":70,"column":10},"action":"remove","lines":["if request.method == \"POST\":","        # populate the login form with the user's input","        login_form = UserLoginForm(request.POST)","        ","        # if the input to the login form is valid","        if login_form.is_valid():","            # use auth.authenticate to check if the","            # user name and password matches","            user = auth.authenticate(username=request.POST['username'],","                                     password=request.POST['password'])","            #if there is a user (meaning, user is not None)","            if user:","                auth.login(user=user, request=request)","                return redirect(reverse('index'))","    else:","        form = UserLoginForm()","        return render(request, 'accounts/login.html', {","            'form':form","        })","        ","@login_required","def profile(request):","    return HttpResponse(\"Profile\")","    ","def register(request):","    if request.method == \"POST\":","        form = UserRegistrationForm(request.POST)","        if form.is_valid():","            form.save()","            # check if the username and password matches","            user = auth.authenticate(username=request.POST['username'],","                                     password=request.POST['password1'])","            if user:","                # actually log the user in","                auth.login(user=user, request=request)","                messages.success(request, \"You have registered successful\")","            else:","                messages.error(request, \"You failed to register\")","            return redirect(reverse('index'))","        else:","            return render(request, \"accounts/register.template.html\",{","                'form': form","            })","    else:","        register_form = UserRegistrationForm()","        return render(request, \"accounts/register.template.html\", {","            'form': register_form","        })"],"id":26}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":5},"action":"insert","lines":["r"],"id":27},{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"insert","lines":["e"]},{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"insert","lines":["t"]},{"start":{"row":23,"column":7},"end":{"row":23,"column":8},"action":"insert","lines":["u"]},{"start":{"row":23,"column":8},"end":{"row":23,"column":9},"action":"insert","lines":["r"]},{"start":{"row":23,"column":9},"end":{"row":23,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":23,"column":10},"end":{"row":23,"column":11},"action":"insert","lines":[" "],"id":28},{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"insert","lines":["r"]},{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"insert","lines":["e"]},{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"insert","lines":["n"]},{"start":{"row":23,"column":14},"end":{"row":23,"column":15},"action":"insert","lines":["d"]},{"start":{"row":23,"column":15},"end":{"row":23,"column":16},"action":"insert","lines":["e"]},{"start":{"row":23,"column":16},"end":{"row":23,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":23,"column":17},"end":{"row":23,"column":19},"action":"insert","lines":["()"],"id":29}],[{"start":{"row":23,"column":18},"end":{"row":23,"column":19},"action":"insert","lines":["r"],"id":30},{"start":{"row":23,"column":19},"end":{"row":23,"column":20},"action":"insert","lines":["e"]},{"start":{"row":23,"column":20},"end":{"row":23,"column":21},"action":"insert","lines":["q"]},{"start":{"row":23,"column":21},"end":{"row":23,"column":22},"action":"insert","lines":["u"]},{"start":{"row":23,"column":22},"end":{"row":23,"column":23},"action":"insert","lines":["e"]},{"start":{"row":23,"column":23},"end":{"row":23,"column":24},"action":"insert","lines":["s"]},{"start":{"row":23,"column":24},"end":{"row":23,"column":25},"action":"insert","lines":["t"]},{"start":{"row":23,"column":25},"end":{"row":23,"column":26},"action":"insert","lines":[","]}],[{"start":{"row":23,"column":26},"end":{"row":23,"column":27},"action":"insert","lines":[" "],"id":31}],[{"start":{"row":23,"column":27},"end":{"row":23,"column":29},"action":"insert","lines":["\"\""],"id":32}],[{"start":{"row":23,"column":28},"end":{"row":23,"column":29},"action":"insert","lines":["a"],"id":33},{"start":{"row":23,"column":29},"end":{"row":23,"column":30},"action":"insert","lines":["c"]},{"start":{"row":23,"column":30},"end":{"row":23,"column":31},"action":"insert","lines":["c"]},{"start":{"row":23,"column":31},"end":{"row":23,"column":32},"action":"insert","lines":["o"]},{"start":{"row":23,"column":32},"end":{"row":23,"column":33},"action":"insert","lines":["u"]},{"start":{"row":23,"column":33},"end":{"row":23,"column":34},"action":"insert","lines":["n"]},{"start":{"row":23,"column":34},"end":{"row":23,"column":35},"action":"insert","lines":["t"]},{"start":{"row":23,"column":35},"end":{"row":23,"column":36},"action":"insert","lines":["s"]}],[{"start":{"row":23,"column":36},"end":{"row":23,"column":37},"action":"insert","lines":["/"],"id":34},{"start":{"row":23,"column":37},"end":{"row":23,"column":38},"action":"insert","lines":["l"]},{"start":{"row":23,"column":38},"end":{"row":23,"column":39},"action":"insert","lines":["o"]},{"start":{"row":23,"column":39},"end":{"row":23,"column":40},"action":"insert","lines":["g"]},{"start":{"row":23,"column":40},"end":{"row":23,"column":41},"action":"insert","lines":["i"]},{"start":{"row":23,"column":41},"end":{"row":23,"column":42},"action":"insert","lines":["n"]},{"start":{"row":23,"column":42},"end":{"row":23,"column":43},"action":"insert","lines":["."]}],[{"start":{"row":23,"column":43},"end":{"row":23,"column":44},"action":"insert","lines":["h"],"id":35},{"start":{"row":23,"column":44},"end":{"row":23,"column":45},"action":"insert","lines":["t"]},{"start":{"row":23,"column":45},"end":{"row":23,"column":46},"action":"insert","lines":["m"]},{"start":{"row":23,"column":46},"end":{"row":23,"column":47},"action":"insert","lines":["l"]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":54},"action":"remove","lines":["from .forms import UserLoginForm, UserRegistrationForm"],"id":36}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":54},"action":"insert","lines":["from .forms import UserLoginForm, UserRegistrationForm"],"id":37}],[{"start":{"row":2,"column":33},"end":{"row":2,"column":54},"action":"remove","lines":[" UserRegistrationForm"],"id":38},{"start":{"row":2,"column":32},"end":{"row":2,"column":33},"action":"remove","lines":[","]}],[{"start":{"row":22,"column":19},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":26},"action":"insert","lines":["form = UserLoginForm()"],"id":40}],[{"start":{"row":24,"column":48},"end":{"row":24,"column":49},"action":"insert","lines":[","],"id":41}],[{"start":{"row":24,"column":49},"end":{"row":24,"column":51},"action":"insert","lines":["{}"],"id":42}],[{"start":{"row":24,"column":50},"end":{"row":26,"column":4},"action":"insert","lines":["","        ","    "],"id":43}],[{"start":{"row":25,"column":8},"end":{"row":25,"column":19},"action":"insert","lines":["'form':form"],"id":44}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":25,"column":19},"end":{"row":25,"column":19},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1576181226413,"hash":"8eb5cb920d32b032d570d7a74fbaf73af3927373"}