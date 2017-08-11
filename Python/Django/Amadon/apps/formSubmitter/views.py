# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect

productInfo = {
"products" : {
"item_id" : [1,2,3,4,5,],
"name" : ["Colored Dice","White Dice","Clear Dice","RGB Dice","Fancy Dice"],
"price" : [1.00, 2.00, 3.00, 4.00, 5.00],
},
}
def index(request):
    global productInfo
    dataLoad = {'code':""}
    print
    for items in range(0,len(productInfo['products']['item_id'])):
        itemname = "item"+str(items)
        itemprice = "price"+str(items)
        csrf_string = get_token(request)
        dataLoad["code"] += "<form action='/results' method='post'><input type='hidden' name='csrfmiddlewaretoken' value='{}'><input type='hidden' name='product_id' value='{}'><div class='row'><ii>".format(csrf_string, productInfo['products']['item_id'][items])+ str(str(productInfo['products']['name'][items]) + " $"+str(productInfo['products']['price'][items])+"<div class='input-field col l1 offset-0'><select name= 'quantity' class='icons'><option value='' disabled selected><option name= 'quantity' value='1'>1</option><option name= 'quantity' value='2'>2</option><option name= 'quantity' value='3'>3</option><option name= 'quantity' value='4'>4</option><option name= 'quantity' value='5'>5</option></select><label>Quantity</label></div><input class='waves-effect waves-light btn' type='submit' value='checkout'></form></div></li>")
    if "total" not in request.session.keys():
        request.session['total'] = 0
    if "current" not in request.session.keys():
        request.session['current'] = 0
    if "items" not in request.session.keys():
        request.session['items'] = 0
    return render(request, "formSubmitter/index.html", dataLoad)
def submitter(request):
    print request.POST['product_id']
    print request.POST['quantity']
    total = int(productInfo['products']['price'][int(request.POST['product_id'])-1])*int(request.POST['quantity'])
    request.session['total'] += total
    request.session['items'] += int(request.POST['quantity'])
    request.session['current'] = total
    print request.session['total']
    return redirect("/checkout")
def checkout(request):
    return render(request, "formSubmitter/result.html")
