from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

def index(request):
    cl = MpesaClient()
    phone_number = '254797245933'
    amount = 1
    account_reference = 'KIBARU HOLDING ACCOUNT'
    transaction_desc = 'Funds entered into holding account'
    callback_url = 'https://6564-102-219-210-106.ngrok-free.app/'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)