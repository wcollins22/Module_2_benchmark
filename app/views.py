from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Book:
    title: str
    author: str
    num_pages: int
# Create your views here.

def view_home(request):
    context = {
        "book_list" : ['Harry Potter', 'Effective Testing with RSpec 3','Automate the Boring Stuff', 'Quiet', 'Peak'],  
    }
    return render(request, "home.html", context)

def view_info(request, book):
    context = {
        "book": book,
        "book_list" : {
            'Harry Potter': Book("Harry Potter", "JK Rowling", 15),

            'Effective Testing with RSpec 3': Book('Effective Testing with RSpec 3', 'Myron Marston', 15),

            'Automate the Boring Stuff': Book('Automate the Boring Stuff', 'Al Sweigart', 15),

            'Quiet': Book('Quiet', 'Susan Cain', 15),

            'Peak': Book('Peak', 'Anders Ericsson', 15)
        },

    }
    return render(request, "authors.html", context)