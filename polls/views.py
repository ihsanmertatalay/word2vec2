from django.shortcuts import render
import os
from gensim.models import Word2Vec
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
"""
  module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'a.py')   #full path to text.
    data_file = open(file_path , 'r')       
    data = data_file.read()
    exec(data)
"""
aaa = 5*5*5*5
print("start")
def index(request):
    print("123")
  
    
    return render(request,'index.html',{"aaa":aaa})


def load(request):
    print("loaded")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'window7.model')
    global model
    model = Word2Vec.load(file_path )
    return render(request,'index.html')

    
def login(request):
    print("123")
    word=request.POST["word"]
    sim = model.wv.most_similar(word)
    print(sim)

    return render(request,'index.html',{"sim":sim})
