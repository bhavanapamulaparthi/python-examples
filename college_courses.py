import os
import xml.etree.ElementTree as ET

file_name = "college_course.xml"
full_file = os.path.abspath(file_name)

doc = ET.parse(full_file)
courses = doc.findall("course")

for c in courses:
    regno = c.find("regno").text
    subj = c.find("subj").text
    days = c.find("days").text

    print('* {} {} {}'.format(regno, subj, days))
