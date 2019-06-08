from jinja2 import Template
t = Template("{{ variable }}")
print(t.render(variable=100))
class A(object):  
    def __str__(self):
        return "__str__"
    def __unicode__(self):
        return "__unicode__"
a1 = A()
print(t.render(variable=a1))
