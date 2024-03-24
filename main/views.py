from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
import time
import random
import re

from . functions.scraper_ import Scraper

def index(request):

    return render(request, 'main/index.html')

def scrap(request):
    item_url = ''
    info = ''
    if request.method == 'POST':
        item_url = request.POST['item_url']

        if item_url:
            scrap_page = Scraper(item_url)

            if scrap_page:
                info = scrap_page.scrap_list_am()

    return render(request, 'main/scrap.html', {'info': info})
