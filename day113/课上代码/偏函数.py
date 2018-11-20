from functools import partial

def func(a,b,c):
    print(a,b,c)


res_func = partial(func,"request")

#@app.template_fitler()
#def fit(a)
"""
{{  123 | fit  }}
"""

res_func(999,c=111)
