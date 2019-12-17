{"filter":false,"title":"forms.py","tooltip":"/checkout/forms.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["from .models import Charge","from django import forms","","class OrderForm(forms.ModelForm):","    class Meta:","        model = Charge","        fields = (","            'full_name', 'phone_number', 'country', 'postcode',","            'town_or_city', 'street_address1', 'street_address2'","        )","        ","class PaymentForm(forms.Form):","","    # use list comprhenison to generate the months and years","    MONTH_CHOICES = [(i, i) for i in range(1, 12)] # [ (1,1), (2,2), (3,3), (4,4) ... ]","    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)] # [ (2019, 2019), (2020, 2020), (2021, 2021)...]","","    credit_card_number = forms.CharField(label='Credit card number', required=False)","    cvv = forms.CharField(label='Security code (CVV)', required=False)","    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)","    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)","    stripe_id = forms.CharField(widget=forms.HiddenInput)",""],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":22},"end":{"row":5,"column":22},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1576600194695,"hash":"143edd4469ec92f9332a7071bc6de4926360cebc"}