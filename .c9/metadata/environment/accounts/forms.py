{"filter":false,"title":"forms.py","tooltip":"/accounts/forms.py","ace":{"folds":[],"scrolltop":240,"scrollleft":0,"selection":{"start":{"row":22,"column":54},"end":{"row":22,"column":54},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":14,"state":"start","mode":"ace/mode/python"}},"hash":"5f1848ce37fa68aad26f99ce1f49f918400efa67","undoManager":{"mark":70,"position":70,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":24},"action":"insert","lines":["from django import forms"],"id":155}],[{"start":{"row":0,"column":24},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":156},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":2,"column":0},"end":{"row":5,"column":58},"action":"insert","lines":["class UserLoginForm(forms.Form):","    \"\"\"Form is for user login\"\"\"","    username = forms.CharField()","    password = forms.CharField(widget=forms.PasswordInput)"],"id":157}],[{"start":{"row":3,"column":8},"end":{"row":3,"column":29},"action":"remove","lines":["orm is for user login"],"id":158},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"remove","lines":["F"]}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["t"],"id":159},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["h"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["i"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":[" "],"id":160},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["i"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":[" "],"id":161},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["a"]}],[{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":[" "],"id":162},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["l"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["o"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["g"]}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":[" "],"id":163},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["i"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":[" "],"id":164},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["f"]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["o"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["r"]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["m"]}],[{"start":{"row":5,"column":58},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":165},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]},{"start":{"row":6,"column":4},"end":{"row":7,"column":0},"action":"insert","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":166}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":167}],[{"start":{"row":8,"column":0},"end":{"row":42,"column":64},"action":"insert","lines":["\"\"\"","User registration form","\"\"\"","class UserRegistrationForm(UserCreationForm):","    password1 = forms.CharField(widget=forms.PasswordInput)","    password2 = forms.CharField(label=\"Password Confirmation\", widget=forms.PasswordInput)","    ","    def clean_email(self):","        User = get_user_model()","        ","        user_provided_email = self.cleaned_data.get('email')","        ","        # check if the email already exists inside the User table","        if User.objects.filter(email=user_provided_email):","            # if so, raise an error","            raise forms.ValidationError(\"This email address is already in use\")","        ","        return user_provided_email","        ","    def clean_password2(self):","        password1 = self.cleaned_data.get('password1')","        password2 = self.cleaned_data.get('password2')","        ","        if not password1 or not password2:","            raise forms.ValidationError(\"Please provide your password twice\")","        ","        if password1 != password2:","            raise forms.ValidationError(\"Make sure both passwords are the same\")","            ","        # return password2 as it is becauase it passes all the validtion rules","        return password2","        ","    class Meta:","        model = MyUser","        fields = ['email', 'username', 'password1', 'password2']"],"id":168}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":24},"action":"remove","lines":["from django import forms"],"id":169},{"start":{"row":0,"column":0},"end":{"row":7,"column":26},"action":"insert","lines":["from django import forms","from django.contrib.auth.models import User","from django.contrib.auth.forms import UserCreationForm","from django.core.exceptions import ValidationError","from django.contrib.auth import get_user_model","","# our own user model","from .models import MyUser"]}],[{"start":{"row":27,"column":10},"end":{"row":27,"column":65},"action":"remove","lines":["check if the email already exists inside the User table"],"id":170},{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":["t"]},{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"insert","lines":["o"]}],[{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":[" "],"id":171},{"start":{"row":27,"column":13},"end":{"row":27,"column":14},"action":"insert","lines":["s"]},{"start":{"row":27,"column":14},"end":{"row":27,"column":15},"action":"insert","lines":["e"]},{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":27,"column":16},"end":{"row":27,"column":17},"action":"insert","lines":[" "],"id":172},{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"insert","lines":["i"]},{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"insert","lines":["f"]}],[{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"insert","lines":[" "],"id":173},{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"insert","lines":["t"]},{"start":{"row":27,"column":21},"end":{"row":27,"column":22},"action":"insert","lines":["h"]},{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"insert","lines":[" "],"id":174},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"insert","lines":["e"]},{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"insert","lines":["m"]},{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"insert","lines":["a"]},{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"insert","lines":["i"]},{"start":{"row":27,"column":28},"end":{"row":27,"column":29},"action":"insert","lines":["l"]}],[{"start":{"row":27,"column":29},"end":{"row":27,"column":30},"action":"insert","lines":[" "],"id":175},{"start":{"row":27,"column":30},"end":{"row":27,"column":31},"action":"insert","lines":["a"]},{"start":{"row":27,"column":31},"end":{"row":27,"column":32},"action":"insert","lines":["l"]},{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"insert","lines":["r"]},{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"insert","lines":["e"]},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":["a"]},{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"insert","lines":["d"]},{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"insert","lines":["y"]}],[{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"insert","lines":[" "],"id":176},{"start":{"row":27,"column":38},"end":{"row":27,"column":39},"action":"insert","lines":["e"]},{"start":{"row":27,"column":39},"end":{"row":27,"column":40},"action":"insert","lines":["x"]},{"start":{"row":27,"column":40},"end":{"row":27,"column":41},"action":"insert","lines":["i"]},{"start":{"row":27,"column":41},"end":{"row":27,"column":42},"action":"insert","lines":["s"]},{"start":{"row":27,"column":42},"end":{"row":27,"column":43},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":43},"end":{"row":27,"column":44},"action":"insert","lines":[" "],"id":177},{"start":{"row":27,"column":44},"end":{"row":27,"column":45},"action":"insert","lines":["i"]},{"start":{"row":27,"column":45},"end":{"row":27,"column":46},"action":"insert","lines":["n"]}],[{"start":{"row":27,"column":46},"end":{"row":27,"column":47},"action":"insert","lines":[" "],"id":178},{"start":{"row":27,"column":47},"end":{"row":27,"column":48},"action":"insert","lines":["s"]},{"start":{"row":27,"column":48},"end":{"row":27,"column":49},"action":"insert","lines":["y"]},{"start":{"row":27,"column":49},"end":{"row":27,"column":50},"action":"insert","lines":["s"]},{"start":{"row":27,"column":50},"end":{"row":27,"column":51},"action":"insert","lines":["t"]},{"start":{"row":27,"column":51},"end":{"row":27,"column":52},"action":"insert","lines":["e"]},{"start":{"row":27,"column":52},"end":{"row":27,"column":53},"action":"insert","lines":["m"]}],[{"start":{"row":44,"column":77},"end":{"row":44,"column":78},"action":"remove","lines":["s"],"id":179},{"start":{"row":44,"column":76},"end":{"row":44,"column":77},"action":"remove","lines":["e"]},{"start":{"row":44,"column":75},"end":{"row":44,"column":76},"action":"remove","lines":["l"]},{"start":{"row":44,"column":74},"end":{"row":44,"column":75},"action":"remove","lines":["u"]},{"start":{"row":44,"column":73},"end":{"row":44,"column":74},"action":"remove","lines":["r"]},{"start":{"row":44,"column":72},"end":{"row":44,"column":73},"action":"remove","lines":[" "]},{"start":{"row":44,"column":71},"end":{"row":44,"column":72},"action":"remove","lines":["n"]},{"start":{"row":44,"column":70},"end":{"row":44,"column":71},"action":"remove","lines":["o"]},{"start":{"row":44,"column":69},"end":{"row":44,"column":70},"action":"remove","lines":["i"]},{"start":{"row":44,"column":68},"end":{"row":44,"column":69},"action":"remove","lines":["t"]},{"start":{"row":44,"column":67},"end":{"row":44,"column":68},"action":"remove","lines":["d"]},{"start":{"row":44,"column":66},"end":{"row":44,"column":67},"action":"remove","lines":["i"]},{"start":{"row":44,"column":65},"end":{"row":44,"column":66},"action":"remove","lines":["l"]},{"start":{"row":44,"column":64},"end":{"row":44,"column":65},"action":"remove","lines":["a"]},{"start":{"row":44,"column":63},"end":{"row":44,"column":64},"action":"remove","lines":["v"]},{"start":{"row":44,"column":62},"end":{"row":44,"column":63},"action":"remove","lines":[" "]},{"start":{"row":44,"column":61},"end":{"row":44,"column":62},"action":"remove","lines":["e"]},{"start":{"row":44,"column":60},"end":{"row":44,"column":61},"action":"remove","lines":["h"]},{"start":{"row":44,"column":59},"end":{"row":44,"column":60},"action":"remove","lines":["t"]}],[{"start":{"row":44,"column":58},"end":{"row":44,"column":59},"action":"remove","lines":[" "],"id":180},{"start":{"row":44,"column":57},"end":{"row":44,"column":58},"action":"remove","lines":["l"]},{"start":{"row":44,"column":56},"end":{"row":44,"column":57},"action":"remove","lines":["l"]},{"start":{"row":44,"column":55},"end":{"row":44,"column":56},"action":"remove","lines":["a"]},{"start":{"row":44,"column":54},"end":{"row":44,"column":55},"action":"remove","lines":[" "]},{"start":{"row":44,"column":53},"end":{"row":44,"column":54},"action":"remove","lines":["s"]},{"start":{"row":44,"column":52},"end":{"row":44,"column":53},"action":"remove","lines":["e"]},{"start":{"row":44,"column":51},"end":{"row":44,"column":52},"action":"remove","lines":["s"]},{"start":{"row":44,"column":50},"end":{"row":44,"column":51},"action":"remove","lines":["s"]},{"start":{"row":44,"column":49},"end":{"row":44,"column":50},"action":"remove","lines":["a"]},{"start":{"row":44,"column":48},"end":{"row":44,"column":49},"action":"remove","lines":["p"]},{"start":{"row":44,"column":47},"end":{"row":44,"column":48},"action":"remove","lines":[" "]},{"start":{"row":44,"column":46},"end":{"row":44,"column":47},"action":"remove","lines":["t"]},{"start":{"row":44,"column":45},"end":{"row":44,"column":46},"action":"remove","lines":["i"]},{"start":{"row":44,"column":44},"end":{"row":44,"column":45},"action":"remove","lines":[" "]},{"start":{"row":44,"column":43},"end":{"row":44,"column":44},"action":"remove","lines":["e"]},{"start":{"row":44,"column":42},"end":{"row":44,"column":43},"action":"remove","lines":["s"]},{"start":{"row":44,"column":41},"end":{"row":44,"column":42},"action":"remove","lines":["a"]},{"start":{"row":44,"column":40},"end":{"row":44,"column":41},"action":"remove","lines":["u"]},{"start":{"row":44,"column":39},"end":{"row":44,"column":40},"action":"remove","lines":["a"]},{"start":{"row":44,"column":38},"end":{"row":44,"column":39},"action":"remove","lines":["c"]},{"start":{"row":44,"column":37},"end":{"row":44,"column":38},"action":"remove","lines":["e"]},{"start":{"row":44,"column":36},"end":{"row":44,"column":37},"action":"remove","lines":["b"]},{"start":{"row":44,"column":35},"end":{"row":44,"column":36},"action":"remove","lines":[" "]}],[{"start":{"row":44,"column":34},"end":{"row":44,"column":35},"action":"remove","lines":["s"],"id":181},{"start":{"row":44,"column":33},"end":{"row":44,"column":34},"action":"remove","lines":["i"]},{"start":{"row":44,"column":32},"end":{"row":44,"column":33},"action":"remove","lines":[" "]},{"start":{"row":44,"column":31},"end":{"row":44,"column":32},"action":"remove","lines":["t"]},{"start":{"row":44,"column":30},"end":{"row":44,"column":31},"action":"remove","lines":["i"]},{"start":{"row":44,"column":29},"end":{"row":44,"column":30},"action":"remove","lines":[" "]},{"start":{"row":44,"column":28},"end":{"row":44,"column":29},"action":"remove","lines":["s"]},{"start":{"row":44,"column":27},"end":{"row":44,"column":28},"action":"remove","lines":["a"]}],[{"start":{"row":44,"column":27},"end":{"row":44,"column":28},"action":"insert","lines":["a"],"id":182},{"start":{"row":44,"column":28},"end":{"row":44,"column":29},"action":"insert","lines":["s"]}],[{"start":{"row":44,"column":29},"end":{"row":44,"column":30},"action":"insert","lines":[" "],"id":183},{"start":{"row":44,"column":30},"end":{"row":44,"column":31},"action":"insert","lines":["i"]},{"start":{"row":44,"column":31},"end":{"row":44,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":44,"column":32},"end":{"row":44,"column":33},"action":"insert","lines":[" "],"id":184},{"start":{"row":44,"column":33},"end":{"row":44,"column":34},"action":"insert","lines":["p"]},{"start":{"row":44,"column":34},"end":{"row":44,"column":35},"action":"insert","lines":["a"]},{"start":{"row":44,"column":35},"end":{"row":44,"column":36},"action":"insert","lines":["s"]},{"start":{"row":44,"column":36},"end":{"row":44,"column":37},"action":"insert","lines":["s"]},{"start":{"row":44,"column":37},"end":{"row":44,"column":38},"action":"insert","lines":["e"]},{"start":{"row":44,"column":38},"end":{"row":44,"column":39},"action":"insert","lines":["d"]}],[{"start":{"row":44,"column":39},"end":{"row":44,"column":40},"action":"insert","lines":[" "],"id":185},{"start":{"row":44,"column":40},"end":{"row":44,"column":41},"action":"insert","lines":["c"]},{"start":{"row":44,"column":41},"end":{"row":44,"column":42},"action":"insert","lines":["a"]},{"start":{"row":44,"column":42},"end":{"row":44,"column":43},"action":"insert","lines":["l"]},{"start":{"row":44,"column":43},"end":{"row":44,"column":44},"action":"insert","lines":["i"]},{"start":{"row":44,"column":44},"end":{"row":44,"column":45},"action":"insert","lines":["d"]}],[{"start":{"row":44,"column":44},"end":{"row":44,"column":45},"action":"remove","lines":["d"],"id":186},{"start":{"row":44,"column":43},"end":{"row":44,"column":44},"action":"remove","lines":["i"]},{"start":{"row":44,"column":42},"end":{"row":44,"column":43},"action":"remove","lines":["l"]},{"start":{"row":44,"column":41},"end":{"row":44,"column":42},"action":"remove","lines":["a"]},{"start":{"row":44,"column":40},"end":{"row":44,"column":41},"action":"remove","lines":["c"]}],[{"start":{"row":44,"column":40},"end":{"row":44,"column":41},"action":"insert","lines":["a"],"id":187},{"start":{"row":44,"column":41},"end":{"row":44,"column":42},"action":"insert","lines":["l"]},{"start":{"row":44,"column":42},"end":{"row":44,"column":43},"action":"insert","lines":["l"]}],[{"start":{"row":44,"column":43},"end":{"row":44,"column":44},"action":"insert","lines":[" "],"id":188},{"start":{"row":44,"column":44},"end":{"row":44,"column":45},"action":"insert","lines":["v"]},{"start":{"row":44,"column":45},"end":{"row":44,"column":46},"action":"insert","lines":["a"]},{"start":{"row":44,"column":46},"end":{"row":44,"column":47},"action":"insert","lines":["l"]},{"start":{"row":44,"column":47},"end":{"row":44,"column":48},"action":"insert","lines":["i"]},{"start":{"row":44,"column":48},"end":{"row":44,"column":49},"action":"insert","lines":["d"]},{"start":{"row":44,"column":49},"end":{"row":44,"column":50},"action":"insert","lines":["a"]},{"start":{"row":44,"column":50},"end":{"row":44,"column":51},"action":"insert","lines":["t"]},{"start":{"row":44,"column":51},"end":{"row":44,"column":52},"action":"insert","lines":["i"]},{"start":{"row":44,"column":52},"end":{"row":44,"column":53},"action":"insert","lines":["o"]},{"start":{"row":44,"column":53},"end":{"row":44,"column":54},"action":"insert","lines":["n"]}],[{"start":{"row":44,"column":54},"end":{"row":44,"column":55},"action":"insert","lines":[" "],"id":189},{"start":{"row":44,"column":55},"end":{"row":44,"column":56},"action":"insert","lines":["r"]},{"start":{"row":44,"column":56},"end":{"row":44,"column":57},"action":"insert","lines":["u"]},{"start":{"row":44,"column":57},"end":{"row":44,"column":58},"action":"insert","lines":["l"]},{"start":{"row":44,"column":58},"end":{"row":44,"column":59},"action":"insert","lines":["e"]},{"start":{"row":44,"column":59},"end":{"row":44,"column":60},"action":"insert","lines":["s"]}],[{"start":{"row":29,"column":18},"end":{"row":29,"column":19},"action":"remove","lines":["o"],"id":190},{"start":{"row":29,"column":17},"end":{"row":29,"column":18},"action":"remove","lines":["s"]}],[{"start":{"row":29,"column":17},"end":{"row":29,"column":18},"action":"insert","lines":["e"],"id":191},{"start":{"row":29,"column":18},"end":{"row":29,"column":19},"action":"insert","lines":["m"]},{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"insert","lines":["a"]},{"start":{"row":29,"column":20},"end":{"row":29,"column":21},"action":"insert","lines":["i"]},{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"insert","lines":["l"]}],[{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"insert","lines":[" "],"id":192},{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"insert","lines":["e"]},{"start":{"row":29,"column":24},"end":{"row":29,"column":25},"action":"insert","lines":["x"]},{"start":{"row":29,"column":25},"end":{"row":29,"column":26},"action":"insert","lines":["i"]},{"start":{"row":29,"column":26},"end":{"row":29,"column":27},"action":"insert","lines":["s"]},{"start":{"row":29,"column":27},"end":{"row":29,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":39,"column":70},"end":{"row":39,"column":75},"action":"remove","lines":["twice"],"id":193},{"start":{"row":39,"column":70},"end":{"row":39,"column":71},"action":"insert","lines":["a"]},{"start":{"row":39,"column":71},"end":{"row":39,"column":72},"action":"insert","lines":["g"]},{"start":{"row":39,"column":72},"end":{"row":39,"column":73},"action":"insert","lines":["a"]},{"start":{"row":39,"column":73},"end":{"row":39,"column":74},"action":"insert","lines":["i"]},{"start":{"row":39,"column":74},"end":{"row":39,"column":75},"action":"insert","lines":["n"]}],[{"start":{"row":20,"column":90},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":200},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["a"]},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["d"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["d"]}],[{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["r"],"id":201},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["e"]},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["s"]},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":[" "],"id":202},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":[" "],"id":203},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["f"]},{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":["o"]},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["r"]},{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["m"]},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["s"]}],[{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["."],"id":204}],[{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["C"],"id":205},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["h"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["a"]}],[{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["r"],"id":206},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["f"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["i"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["e"]},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["l"]},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["d"]}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":31},"action":"insert","lines":["()"],"id":207}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"remove","lines":["f"],"id":208}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["F"],"id":209}],[{"start":{"row":21,"column":31},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":210},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["m"],"id":211},{"start":{"row":22,"column":5},"end":{"row":22,"column":6},"action":"insert","lines":["o"]},{"start":{"row":22,"column":6},"end":{"row":22,"column":7},"action":"insert","lines":["b"]},{"start":{"row":22,"column":7},"end":{"row":22,"column":8},"action":"insert","lines":["i"]},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["l"]},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":[" "],"id":212},{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["="]}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":[" "],"id":213},{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["f"]},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["o"]},{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["r"]},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["m"]},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["s"]},{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["."]}],[{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["I"],"id":214},{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["n"]}],[{"start":{"row":22,"column":19},"end":{"row":22,"column":21},"action":"remove","lines":["In"],"id":215},{"start":{"row":22,"column":19},"end":{"row":22,"column":31},"action":"insert","lines":["IntegerField"]}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":33},"action":"insert","lines":["()"],"id":216}],[{"start":{"row":51,"column":63},"end":{"row":51,"column":64},"action":"insert","lines":[","],"id":217},{"start":{"row":51,"column":64},"end":{"row":51,"column":65},"action":"insert","lines":["a"]},{"start":{"row":51,"column":65},"end":{"row":51,"column":66},"action":"insert","lines":["d"]},{"start":{"row":51,"column":66},"end":{"row":51,"column":67},"action":"insert","lines":["d"]}],[{"start":{"row":51,"column":66},"end":{"row":51,"column":67},"action":"remove","lines":["d"],"id":218},{"start":{"row":51,"column":65},"end":{"row":51,"column":66},"action":"remove","lines":["d"]},{"start":{"row":51,"column":64},"end":{"row":51,"column":65},"action":"remove","lines":["a"]}],[{"start":{"row":51,"column":64},"end":{"row":51,"column":66},"action":"insert","lines":["''"],"id":219}],[{"start":{"row":51,"column":65},"end":{"row":51,"column":66},"action":"insert","lines":["a"],"id":220},{"start":{"row":51,"column":66},"end":{"row":51,"column":67},"action":"insert","lines":["d"]},{"start":{"row":51,"column":67},"end":{"row":51,"column":68},"action":"insert","lines":["d"]},{"start":{"row":51,"column":68},"end":{"row":51,"column":69},"action":"insert","lines":["r"]},{"start":{"row":51,"column":69},"end":{"row":51,"column":70},"action":"insert","lines":["e"]},{"start":{"row":51,"column":70},"end":{"row":51,"column":71},"action":"insert","lines":["s"]},{"start":{"row":51,"column":71},"end":{"row":51,"column":72},"action":"insert","lines":["s"]}],[{"start":{"row":51,"column":73},"end":{"row":51,"column":74},"action":"insert","lines":[","],"id":221}],[{"start":{"row":51,"column":74},"end":{"row":51,"column":76},"action":"insert","lines":["''"],"id":222}],[{"start":{"row":51,"column":75},"end":{"row":51,"column":76},"action":"insert","lines":["m"],"id":223},{"start":{"row":51,"column":76},"end":{"row":51,"column":77},"action":"insert","lines":["o"]},{"start":{"row":51,"column":77},"end":{"row":51,"column":78},"action":"insert","lines":["b"]},{"start":{"row":51,"column":78},"end":{"row":51,"column":79},"action":"insert","lines":["i"]},{"start":{"row":51,"column":79},"end":{"row":51,"column":80},"action":"insert","lines":["l"]},{"start":{"row":51,"column":80},"end":{"row":51,"column":81},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":30},"end":{"row":21,"column":31},"action":"insert","lines":["w"],"id":224},{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"insert","lines":["i"]},{"start":{"row":21,"column":32},"end":{"row":21,"column":33},"action":"insert","lines":["d"]},{"start":{"row":21,"column":33},"end":{"row":21,"column":34},"action":"insert","lines":["e"]},{"start":{"row":21,"column":34},"end":{"row":21,"column":35},"action":"insert","lines":["t"]},{"start":{"row":21,"column":35},"end":{"row":21,"column":36},"action":"insert","lines":["="]},{"start":{"row":21,"column":36},"end":{"row":21,"column":37},"action":"insert","lines":["f"]}],[{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"insert","lines":["o"],"id":225},{"start":{"row":21,"column":38},"end":{"row":21,"column":39},"action":"insert","lines":["r"]},{"start":{"row":21,"column":39},"end":{"row":21,"column":40},"action":"insert","lines":["m"]},{"start":{"row":21,"column":40},"end":{"row":21,"column":41},"action":"insert","lines":["s"]},{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"insert","lines":["."]}],[{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"insert","lines":["A"],"id":226},{"start":{"row":21,"column":43},"end":{"row":21,"column":44},"action":"insert","lines":["d"]},{"start":{"row":21,"column":44},"end":{"row":21,"column":45},"action":"insert","lines":["d"]},{"start":{"row":21,"column":45},"end":{"row":21,"column":46},"action":"insert","lines":["r"]},{"start":{"row":21,"column":46},"end":{"row":21,"column":47},"action":"insert","lines":["e"]},{"start":{"row":21,"column":47},"end":{"row":21,"column":48},"action":"insert","lines":["s"]},{"start":{"row":21,"column":48},"end":{"row":21,"column":49},"action":"insert","lines":["s"]},{"start":{"row":21,"column":49},"end":{"row":21,"column":50},"action":"insert","lines":["I"]}],[{"start":{"row":21,"column":50},"end":{"row":21,"column":51},"action":"insert","lines":["n"],"id":227},{"start":{"row":21,"column":51},"end":{"row":21,"column":52},"action":"insert","lines":["p"]},{"start":{"row":21,"column":52},"end":{"row":21,"column":53},"action":"insert","lines":["u"]},{"start":{"row":21,"column":53},"end":{"row":21,"column":54},"action":"insert","lines":["t"]}],[{"start":{"row":21,"column":42},"end":{"row":21,"column":54},"action":"remove","lines":["AddressInput"],"id":228},{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"insert","lines":["T"]},{"start":{"row":21,"column":43},"end":{"row":21,"column":44},"action":"insert","lines":["e"]},{"start":{"row":21,"column":44},"end":{"row":21,"column":45},"action":"insert","lines":["x"]}],[{"start":{"row":21,"column":42},"end":{"row":21,"column":45},"action":"remove","lines":["Tex"],"id":229},{"start":{"row":21,"column":42},"end":{"row":21,"column":51},"action":"insert","lines":["TextInput"]}],[{"start":{"row":21,"column":33},"end":{"row":21,"column":34},"action":"insert","lines":["g"],"id":230}],[{"start":{"row":22,"column":32},"end":{"row":22,"column":54},"action":"insert","lines":["widget=forms.TextInput"],"id":231}]]},"timestamp":1576668665656}