from datetime import datetime
from hashlib import new
from tkinter import messagebox

from MySQLdb import Date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.db import models
# Create your views here.
from django.urls import reverse
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.utils.decorators import method_decorator

from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DeleteView

from .decorator import login_message_required
from .forms import *
import json

def index(request):
    return render(request, 'index.html')

# 완성본 게시판
class test2(ListView):

    @method_decorator(login_message_required)
    def get(self, request):

        # mainboard
        contextForm = ContextForm
        department_text = request.GET.get('department')
        month_text = request.GET.get('month')
        if month_text is None:
            month_text = DateFormat(datetime.now()).format('m')
        if department_text is None:
            department_text = "개발"
        board_list = Board.objects.filter(month=month_text, department=department_text).order_by("user")

        # 회사목표
        companyForm = CompanyForm
        company_list = Company.objects.all()

        # 부서목표
        departmentForm = DepartmentForm
        department_list = Departmentgoal.objects.filter(department=department_text)

        # 개별목표
        personalgoalForm = PersonalgoalForm
        personalgoal_list = Personalgoal.objects.filter(department=department_text)

        # 분류
        classificationForm = ClassificationForm
        classification_list = Classification.objects.filter(department=department_text)

        # board_list 페이징 처리
        page = request.GET.get('page', '1')
        paginator = Paginator(board_list, '10')
        page_obj = paginator.page(page)

        context = {
            # company context
            'company_list': company_list,
            'companyForm': companyForm,

            # test2 context
            'contextForm': contextForm,
            'board_list': page_obj,
            'month_text': month_text,
            'department_text': department_text,

            # personal context
            'personalgoalForm': personalgoalForm,
            'personalgoal_list': personalgoal_list,

            # departmentgoal context
            'departmentForm': departmentForm,
            'department_list': department_list,

            # classification context
            'classificationForm': classificationForm,
            'classification_list': classification_list,
        }
        return render(request, 'test1.html', context)

    def post(self, request):

        # 월 - 게시판
        if request.method == 'POST' and 'attr_name' in request.POST:

            board = Board(
                context=request.POST['context'],
                num=request.POST['num'],
                task=request.POST['task'],
                expect=request.POST['expect'],
                startdate=request.POST['startdate'],
                enddate=request.POST['enddate'],
                time=request.POST['time'],
                problem=request.POST['problem'],
                result=request.POST['result'],
                solution=request.POST['solution'],
                team=request.POST['team'],
                level=request.POST['level'],
            )

            month_text = request.GET.get('month')
            department_text = request.GET.get('department')
            if month_text is None:
                month_text = DateFormat(datetime.now()).format('m')
            if department_text is None:
                department_text = "개발"
            board.department = department_text
            board.month = month_text
            user = request.user
            username = User.objects.get(username=user)
            board.user = username
            context_text = request.POST.get('context')
            same_context = Board.objects.filter(context=context_text, month=month_text, department=department_text)

            try:
                if len(same_context) == 0:
                    board.save()
                    return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.warning(request, " 세부테스크의 내용이 중복입니다. 다른 내용으로 바꿔주세요.")
                    return redirect(request.META.get('HTTP_REFERER'))
            except ValueError:
                messages.warning(request, " 숫자여야 합니다. ")
                return redirect(request.META.get('HTTP_REFERER'))


        # 회사

        if request.method == 'POST' and 'attr_name2' in request.POST:
            company = Company(
                title=request.POST['title'],
                context=request.POST['context'],
            )
            company.save()
            return redirect(request.META.get('HTTP_REFERER'))


        # 개인목표

        if request.method == 'POST' and 'attr_name3' in request.POST:
            personalgoal = Personalgoal(
                person=request.POST['person'],
                title=request.POST['title'],
                context=request.POST['context'],
            )
            department_text = request.GET.get('department')
            if department_text is None:
                department_text = "개발"
            personalgoal.department = department_text
            personalgoal.save()
            return redirect(request.META.get('HTTP_REFERER'))


        # 부서 목표

        if request.method == 'POST' and 'attr_name4' in request.POST:

            departmentgoal = Departmentgoal(
                title=request.POST['title'],
                context=request.POST['context'],
            )

            department_text = request.GET.get('department')
            if department_text is None:
                department_text = "개발"
            departmentgoal.department = department_text
            departmentgoal.save()
            return redirect(request.META.get('HTTP_REFERER'))


        # 분류
        if request.method == 'POST' and 'attr_name5' in request.POST:
            classification = Classification(
                num=request.POST['num'],
                title=request.POST['title'],
            )
            department_text = request.GET.get('department')
            if department_text is None:
                department_text = "개발"
            classification.department = department_text
            try:
                classification.save()
                return redirect(request.META.get('HTTP_REFERER'))
            except ValueError:
                messages.warning(request, " 숫자여야 합니다. ")
                return redirect(request.META.get('HTTP_REFERER'))


# 게시판 수정 삭제

def postdelete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect(request.META.get('HTTP_REFERER'))


# 회사 삭제

def companypostdelete(request, pk):
    company = Company.objects.get(pk=pk)
    company.delete()
    return redirect(request.META.get('HTTP_REFERER'))


# 개별목표 삭제

def personalgoaldelete(request, pk):
    personalgoal = Personalgoal.objects.get(pk=pk)
    personalgoal.delete()
    return redirect(request.META.get('HTTP_REFERER'))


# 부서 삭제

def departmentpostdelete(request, pk):
    departmentgoal = Departmentgoal.objects.get(pk=pk)
    departmentgoal.delete()
    return redirect(request.META.get('HTTP_REFERER'))


# 분류 삭제

def classificationpostdelete(request, pk):
    classification = Classification.objects.get(pk=pk)
    classification.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@csrf_exempt
def savetable(request):
    # main Board
    id = request.POST.get('id', '')
    type = request.POST.get('type', '')
    value = request.POST.get('value', '')
    board = Board.objects.get(id=id)
    if type == "context":
        board.context = value
    if type == "expect":
        board.expect = value
    if type == "startdate":
        board.startdate = value
    if type == "enddate":
        board.enddate = value
    if type == "time":
        board.time = value
    if type == "problem":
        board.problem = value
    if type == "result":
        board.result = value
    if type == "solution":
        board.solution = value
    if type == "team":
        board.team = value
    if type == "level":
        board.level = value
    board.save()
    return JsonResponse({"success": "Updated!!"})


def timeline(request):
    department_text = request.GET.get('department')
    month_text = request.GET.get('month')
    if month_text is None:
        month_text = DateFormat(datetime.now()).format('m')
    if department_text is None:
        department_text = "개발"

    board_list = Board.objects.filter(month=month_text, department=department_text).order_by("startdate")
    department_list = Departmentgoal.objects.filter(department=department_text)
    personalgoal_list = Personalgoal.objects.filter(department=department_text)
    classification_list = Classification.objects.filter(department=department_text)
    company_list = Company.objects.all()

    data = []
    for i in board_list:
        data.append([i.context, i.context, str(i.user), str(i.startdate), str(i.enddate), None, i.result * 100, None])

    modified_data = json.dumps(data, ensure_ascii=False)

    context = {
        'values': modified_data,
        'board_list': board_list,
        'month_text':month_text,
        'department_text': department_text,
        'classification_list': classification_list,
        'department_list': department_list,
        'personalgoal_list': personalgoal_list,
        'company_list': company_list,
    }

    return render(request, 'timeex.html', context)
