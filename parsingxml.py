import xml.dom.minidom

doc  = xml.dom.minidom.parse("empinfo.xml")

print(doc.nodeName)
print(doc.firstChild.tagName)

f_name = doc.getElementsByTagName("fname")
exp = doc.getElementsByTagName("expertise")
print("%d expertise:" %exp.length)
for skill in exp:
    print(skill.getAttribute("name"))

new_exp = doc.createElement("expertise")
new_exp.setAttribute("name","Django")
doc.firstChild.appendChild(new_exp)
print(" ")
exp = doc.getElementsByTagName("expertise")
print("%d expertise:" %exp.length)
for skill in exp:
    print(skill.getAttribute("name"))


import xml.etree.ElementTree as ET
tree = ET.parse("empinfo.xml")
root = tree.getroot()

for ele in root:
    for subele in ele:
        print(subele.text)

