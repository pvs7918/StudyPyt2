import random

from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('logging for function index')

    context = {
        'name': 'Guest',
    }
    # шаблон должен быть расположен в подкаталоге templates приложения
    return render(request, "apptest1/index.html", context=context)


def about(request):
    logger.info('logging for function about')

    context = {
    }
    # шаблон должен быть расположен в подкаталоге templates приложения
    return render(request, "apptest1/about.html", context=context)


def coin(request):
    logger.info('logging for function coin')
    return HttpResponse(random.choice(['Орел', 'Решка']))


def cube(request):
    logger.info('logging for function cube')
    return HttpResponse(random.randrange(1, 7))


def myrand(request):
    logger.info('logging for function myrand')
    return HttpResponse(random.randrange(1, 1001))


def testlog(request):
    a = 1 / 0
    try:  # some code that might raise an exception
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.")
