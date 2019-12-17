{"filter":false,"title":"models.py","tooltip":"/shop/models.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":26},"action":"remove","lines":["from django.db import models","","# Create your models here."],"id":2},{"start":{"row":0,"column":0},"end":{"row":15,"column":28},"action":"insert","lines":["from django.db import models","","# Create your models here.","class Product(models.Model):","    name = models.CharField(max_length=255, blank=False)","    sku = models.CharField(max_length=100, blank=False)","    description = models.TextField(blank=False)","    cost = models.IntegerField(blank=False)","    quantity = models.IntegerField(blank=False, default=0)","    image = models.ImageField(blank=True, null=True)","    ","    def __str__(self):","        return self.name + \" : \" + self.sku","        ","    def getCostInDollars(self):","        return self.cost/100"]}],[{"start":{"row":0,"column":28},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":4}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":45},"action":"insert","lines":["from pyuploadcare.dj.models import ImageField"],"id":5}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":52},"action":"remove","lines":["image = models.ImageField(blank=True, null=True)"],"id":6},{"start":{"row":10,"column":4},"end":{"row":10,"column":33},"action":"insert","lines":["photo = ImageField(null=True)"]}],[{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"remove","lines":["e"],"id":9},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"remove","lines":["g"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"remove","lines":["a"]},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"remove","lines":["m"]},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"remove","lines":["i"]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["i"],"id":9},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["m"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["a"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["g"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"remove","lines":["o"],"id":10},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"remove","lines":["t"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"remove","lines":["o"]},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"remove","lines":["h"]},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"remove","lines":["p"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":4},"end":{"row":10,"column":9},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1576513662483,"hash":"928bbd98b1a0d5faba6644f5d1234b2d41eac230"}