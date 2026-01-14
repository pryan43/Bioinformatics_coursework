import xml.etree.ElementTree as ET
import urllib.request
import sys


if len(sys.argv) < 2:
    print('provide URL')
    sys.exit(1)

thefile = urllib.request.urlopen(sys.argv[1])


#'http://www.uniprot.org/uniprot/Q9H400.xml'
#'http://www.uniprot.org/uniprot/P13569.xml'


document = ET.parse(thefile)
root = document.getroot()

ns = '{http://uniprot.org/uniprot}'


entry = root.find(ns+'entry')

print("==== References ====")
    

for reference in entry.findall(ns + 'reference'):
    citation = reference.find(ns + 'citation')

    if citation is not None:
        title_ele = citation.find(ns+'title')
        if title_ele is not None:
            title = title_ele.text
        else:
            title = 'No title available'

        #print('Citation attributes:', citation.attrib)

        journal = citation.attrib.get('name', 'No journal name available')
        year = citation.attrib['date']

        print('Title:', title)
        print('Journal:', journal)
        print('Year:', year)

        authors = citation.find(ns + 'authorList')
        if authors is not None:
            print('Authors:')
            for author in authors.findall(ns + 'person'):
                print('  -  ' + author.attrib['name'])
            







