"""Use our simple XML output API to write XML data about this course."""

from xml_context import Element  # import our XML output API

with Element(print, "class", {  # attributes
        "title": "Programming with Python", "year": 2024}) as cls:
    with cls.element("description") as desc:  # first inner element
        desc.text("This is a class on Python.")  # text of inner element
    with cls.element("teacher", {"name": "Thomas"}) as teach:
        teach.text("I like Python.")  # Write text inside the element.
    with cls.element("students") as studis:
        with studis.element("student", {"name": "Bubba"}):
            pass  # This element does not have any text inside.
        with studis.element("student", {"name": "Bibba"}) as studi:
            studi.text("I like the <Programming with Python> book.")
