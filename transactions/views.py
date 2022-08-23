from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from customuser.models import User_Account
from .models import Transaction, Transaction_type
from accounts.models import Account
from company.models import Currency, Company
from contractors.models import Contractor


def transactions_view(request):
    if request.method == 'GET':
        user_account = User_Account.objects.filter(owner=request.user)
        user_account = user_account[0]
        transactions = Transaction.objects.filter(user_account=user_account)
        accounts = Account.objects.filter(user_account=user_account)
        contractors = Contractor.objects.filter(user_account=user_account)
        currencies = Currency.objects.all()
        transactions_types = Transaction_type.objects.all()
        return render(request, 'transactions/transactions.html', {'currencies': currencies,
                                                                  'transactions': transactions,
                                                                  'accounts': accounts, 'contractors': contractors,
                                                                  'transactions_types': transactions_types})


def add_transaction(request):
    if request.method == 'POST':

        account_uid = request.POST.get('account_uid')
        contractor_uid = request.POST.get('contractor_uid')

        transaction_amount = request.POST.get('transaction_amount')
        transaction_type = request.POST.get('transaction_type')

        contractor_name = request.POST.get('contractor_name')


        user_account = User_Account.objects.get(owner=request.user)

        if contractor_name:
            contractor = Contractor.objects.create(contractor_name=contractor_name, user_account=user_account)
        else:
            contractor = Contractor.objects.get(uid=contractor_uid)

        account = Account.objects.get(uid=account_uid, user_account=user_account)
        new_transaction = Transaction.objects.create(account=account,
                                                     contractor=contractor,
                                                     sum_of_transactions=transaction_amount,
                                                     transaction_type=transaction_type,
                                                     user_account=user_account)

        return HttpResponseRedirect('/transactions/')




def delete_transaction(request):

    user_account = User_Account.objects.filter(owner=request.user)
    uid = request.POST.get('uid')
    try:
        transaction = Transaction.objects.filter(user_account=user_account[0], uid=uid)

        if transaction:
            transaction[0].delete()

        return JsonResponse({}, status=200)

    except Exception:
        return redirect('customuser:bad_request')


def transaction_edit(request, tr_uid):
    user_account = User_Account.objects.filter(owner=request.user)
    if request.method == 'GET':
        if user_account:
            user_account = user_account[0]
            accounts = Account.objects.filter(user_account=user_account)
            transaction = Transaction.objects.filter(user_account=user_account, uid=tr_uid)[0]
            contractors = Contractor.objects.filter(user_account=user_account)
            currencies = Currency.objects.all()
            transaction_types = Transaction_type.objects.all()
        return render(request, 'transactions/transaction_edit.html', {'transaction': transaction, 'accounts': accounts,
                                                                      'contractors': contractors, 'currencies': currencies,
                                                                      'transaction_types': transaction_types})
    else:

        user_account = User_Account.objects.filter(owner=request.user)[0]
        transaction = Transaction.objects.filter(uid=tr_uid, user_account=user_account)

        account_uid = request.POST.get('account_uid')
        contractor_uid = request.POST.get('contractor_uid')
        transaction_type = request.POST.get('transaction_type')
        transaction_amount = request.POST.get('transaction_amount')
        # transaction_date = request.POST.get('datetimes')
        if account_uid:
            account = Account.objects.filter(uid=account_uid, user_account=user_account)[0]
            transaction.update(account=account)

        if contractor_uid:
            contractor = Contractor.objects.filter(uid=contractor_uid, user_account=user_account)[0]
            transaction.update(contractor=contractor)

        transaction.update(transaction_type=transaction_type,
                           sum_of_transactions=transaction_amount)
        return HttpResponseRedirect(f'/transactions/{tr_uid}/')