#coding=utf-8
from uliweb import expose, functions
from uliweb.core.template import get_templatefile

#testlink
def tl(r):
    l = ["<strong>"]
    for index in r:
        l.append('<a href="test%d">⚑test%d</a> '%(index,index))
    l.append("</strong>")
    return " ".join(l)

@expose('/')
def index():
    return {"tl":tl}

@expose('/test<tid>')
def test(tid):
    response.template = fn = "test"+tid+".html"
    if get_templatefile(fn, application.template_dirs)==None:
        return redirect("test1")
    return {"testid":int(tid)}
