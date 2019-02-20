# from django.shortcuts import render

# Create your views here.


def vista(opcion):
    if opcion:
        return ('Es True')
    else:
        return ('Es False')

    # if False:
    # 	return ('Es False')
    # else:
    # 	return ('Es True')
