# -*- coding: utf-8 -*-
from plone.folder.default import DefaultOrdering
from plone.folder.ordered import OrderedBTreeFolderBase
from plone.folder.tests.layer import PloneFolderLayer
from plone.folder.unordered import UnorderedOrdering
from unittest import defaultTestLoader
from unittest import TestCase
from zope.component import ComponentLookupError


class OrderingAdapterTests(TestCase):
    """ tests regarding available ordering adapters """

    layer = PloneFolderLayer

    def testDefaultAdapter(self):
        folder = OrderedBTreeFolderBase()
        self.failUnless(isinstance(folder.getOrdering(), DefaultOrdering))

    def testUnorderedOrdering(self):
        folder = OrderedBTreeFolderBase()
        folder._ordering = 'unordered'
        self.failUnless(isinstance(folder.getOrdering(), UnorderedOrdering))

    def testUnknownOrdering(self):
        folder = OrderedBTreeFolderBase()
        folder._ordering = 'foo'
        self.failUnless(isinstance(folder.getOrdering(), DefaultOrdering))

    def testSetOrdering(self):
        folder = OrderedBTreeFolderBase()
        folder.setOrdering('unordered')
        self.failUnless(isinstance(folder.getOrdering(), UnorderedOrdering))
        folder.setOrdering()
        self.failUnless(isinstance(folder.getOrdering(), DefaultOrdering))

    def testSetUnknownOrdering(self):
        folder = OrderedBTreeFolderBase()
        self.assertRaises(ComponentLookupError, folder.setOrdering, 'foo')


def test_suite():
    return defaultTestLoader.loadTestsFromName(__name__)
