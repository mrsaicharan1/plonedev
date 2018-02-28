

# Zope imports
from zope.interface import Interface
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class MyView(BrowserView):
    index = ViewPageTemplateFile("myview.pt")