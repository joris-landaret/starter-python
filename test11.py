from xml.dom import minidom

doc = minidom.parse('domains.xml')
elements = doc.getElementsByTagName("column")
newList = []

for element in elements:
    if element.getAttribute("name")