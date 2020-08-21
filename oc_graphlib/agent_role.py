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
from __future__ import annotations
from rdflib import URIRef

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from oc_graphlib.bibliographic_resource import BibliographicResource
from oc_graphlib.graph_entity import GraphEntity
from oc_graphlib.bibliographic_entity import BibliographicEntity

"""
Notes about AR:

    HAS ROLE TYPE is generated by the factory methods!
    IS HELD BY is generated by ResponsibleAgent.has_role method! Have a look at responsible_agent.py for more info.
    Chill down, everything seems OK here!
"""


class AgentRole(BibliographicEntity):
    """
    AAA: this should have inverse logic!!!
    See below:

    # HAS NEXT (AgentRole)
    def has_next(self, ar_res: AgentRole) -> None:
        self.g.add((self.res, GraphEntity.has_next, URIRef(str(ar_res))))
    """
    def follows(self, ar_res: AgentRole) -> None:
        ar_res.g.add((URIRef(str(ar_res)), GraphEntity.has_next, self.res))

    # ++++++++++++++++++++++++ FACTORY METHODS ++++++++++++++++++++++++
    def create_publisher(self, br_res: BibliographicResource) -> bool:
        return self._associate_role_with_document(GraphEntity.publisher, br_res)

    def create_author(self, br_res: BibliographicResource) -> bool:
        return self._associate_role_with_document(GraphEntity.author, br_res)

    def create_editor(self, br_res: BibliographicResource) -> bool:
        return self._associate_role_with_document(GraphEntity.editor, br_res)

    # <self.res> PRO:withRole <role_type>
    # <br_res> PRO:isDocumentContextFor <role_type> (BibliographicResource's HAS CONTRIBUTOR)
    def _associate_role_with_document(self, role_type: URIRef, br_res: BibliographicResource) -> bool:
        self.g.add((self.res, GraphEntity.with_role, role_type))
        br_res.g.add((URIRef(str(br_res)), GraphEntity.is_document_context_for, self.res))
        return True
