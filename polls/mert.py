from gensim.models import Word2Vec
import os

module_dir = os.path.dirname(__file__)  
file_path = os.path.join(module_dir, 'window7.model')
model = Word2Vec.load("${file_path}/window7.model")
print(model.wv.most_similar("silah"))
print(model.wv.most_similar("patates"))
print(model.wv.most_similar("kumaş"))
print(model.wv.most_similar("pantalon"))
print(model.wv.most_similar("eşşek"))
print(model.wv.most_similar("koşmak"))
