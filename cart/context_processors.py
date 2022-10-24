from .cart import Cart
'''
This makes it so that the class is available everywhere in your program like a Global variable for all django html files
files in your program

'''
def cart(request):
    return {'cart':Cart(request)}