"""Use our simple XML output API to write XML data to a file."""

from os import remove  # The function for deleting the file at the end.

from xml_context import Element  # import our XML output API

# This time, we pass the `write` method of an output stream to the API.
with open("example.xml", mode="w", encoding="UTF-8") as stream_out:
    with Element(stream_out.write, "class", {  # attributes
            "title": "Programming with Python", "year": 2024}) as cls:
        with cls.element("description") as desc:  # first inner element
            desc.text("This is a class on Python.")
        with cls.element("teacher", {"name": "Thomas"}) as teach:
            teach.text("I like Python.")  # Write text inside the element.
        with cls.element("students") as studis:
            with studis.element("student", {"name": "Bubba"}):
                pass  # This element does not have any text inside.
            with studis.element("student", {"name": "Bibba"}) as studi:
                studi.text("I like the <Programming with Python> book.")

# Now we open the file again and read and print its contents.
with open("example.xml", encoding="UTF-8") as stream_in:
    for line in stream_in:  # Iterate over the lines in the file.
        print(line.rstrip())  # Print the line (without trailing newline).

remove("example.xml")  # Finally, we delete the file.
