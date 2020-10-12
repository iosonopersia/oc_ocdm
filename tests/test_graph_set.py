#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2016, Silvio Peroni <essepuntato@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.
import unittest

from rdflib import URIRef, Graph

from oc_ocdm import GraphSet
from oc_ocdm.counter_handler import FilesystemCounterHandler
from oc_ocdm.entities import Identifier
from oc_ocdm.entities.bibliographic import AgentRole
from oc_ocdm.entities.bibliographic import BibliographicReference
from oc_ocdm.entities.bibliographic import BibliographicResource
from oc_ocdm.entities.bibliographic import Citation
from oc_ocdm.entities.bibliographic import DiscourseElement
from oc_ocdm.entities.bibliographic import PointerList
from oc_ocdm.entities.bibliographic import ReferenceAnnotation
from oc_ocdm.entities.bibliographic import ReferencePointer
from oc_ocdm.entities.bibliographic import ResourceEmbodiment
from oc_ocdm.entities.bibliographic import ResponsibleAgent


class TestGraphSet(unittest.TestCase):

    def setUp(self):
        self.counter_handler = FilesystemCounterHandler("./info_dir/")
        self.graph_set = GraphSet("http://test/", "context_base", self.counter_handler, "", wanted_label=False)

    def test_get_entity(self):
        ar = self.graph_set.add_ar(self.__class__.__name__)
        ref = ar.res
        result = self.graph_set.get_entity(ref)
        self.assertIsNotNone(result)
        self.assertIs(result, ar)

    def test_add_an(self):
        an = self.graph_set.add_an(self.__class__.__name__)

        self.assertIsNotNone(an)
        self.assertIsInstance(an, ReferenceAnnotation)
        self.assertEqual(str(an.g.identifier), self.graph_set.g_an)

    def test_add_ar(self):
        ar = self.graph_set.add_ar(self.__class__.__name__)

        self.assertIsNotNone(ar)
        self.assertIsInstance(ar, AgentRole)
        self.assertEqual(str(ar.g.identifier), self.graph_set.g_ar)

    def test_add_be(self):
        be = self.graph_set.add_be(self.__class__.__name__)

        self.assertIsNotNone(be)
        self.assertIsInstance(be, BibliographicReference)
        self.assertEqual(str(be.g.identifier), self.graph_set.g_be)

    def test_add_br(self):
        br = self.graph_set.add_br(self.__class__.__name__)

        self.assertIsNotNone(br)
        self.assertIsInstance(br, BibliographicResource)
        self.assertEqual(str(br.g.identifier), self.graph_set.g_br)

    def test_add_ci(self):
        ci = self.graph_set.add_ci(self.__class__.__name__)

        self.assertIsNotNone(ci)
        self.assertIsInstance(ci, Citation)
        self.assertEqual(str(ci.g.identifier), self.graph_set.g_ci)

    def test_add_de(self):
        de = self.graph_set.add_de(self.__class__.__name__)

        self.assertIsNotNone(de)
        self.assertIsInstance(de, DiscourseElement)
        self.assertEqual(str(de.g.identifier), self.graph_set.g_de)

    def test_add_id(self):
        identifier = self.graph_set.add_id(self.__class__.__name__)

        self.assertIsNotNone(identifier)
        self.assertIsInstance(identifier, Identifier)
        self.assertEqual(str(identifier.g.identifier), self.graph_set.g_id)

    def test_add_pl(self):
        pl = self.graph_set.add_pl(self.__class__.__name__)

        self.assertIsNotNone(pl)
        self.assertIsInstance(pl, PointerList)
        self.assertEqual(str(pl.g.identifier), self.graph_set.g_pl)

    def test_add_rp(self):
        rp = self.graph_set.add_rp(self.__class__.__name__)

        self.assertIsNotNone(rp)
        self.assertIsInstance(rp, ReferencePointer)
        self.assertEqual(str(rp.g.identifier), self.graph_set.g_rp)

    def test_add_ra(self):
        ra = self.graph_set.add_ra(self.__class__.__name__)

        self.assertIsNotNone(ra)
        self.assertIsInstance(ra, ResponsibleAgent)
        self.assertEqual(str(ra.g.identifier), self.graph_set.g_ra)

    def test_add_re(self):
        re = self.graph_set.add_re(self.__class__.__name__)

        self.assertIsNotNone(re)
        self.assertIsInstance(re, ResourceEmbodiment)
        self.assertEqual(str(re.g.identifier), self.graph_set.g_re)

    def test_graphs(self):
        count = 10
        for i in range(count):
            self.graph_set.add_ar(self.__class__.__name__)
        result = self.graph_set.graphs()
        self.assertIsNotNone(result)
        self.assertEqual(len(result), count)
        for graph in result:
            self.assertIsInstance(graph, Graph)

    def test_get_graph_iri(self):
        ar = self.graph_set.add_ar(self.__class__.__name__)
        iri = str(ar.g.identifier)
        result = GraphSet.get_graph_iri(ar.g)
        self.assertIsNotNone(result)
        self.assertEqual(iri, result)


if __name__ == '__main__':
    unittest.main()
