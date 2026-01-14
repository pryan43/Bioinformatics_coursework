"""
Title:
MS/MS Peptide Fragment Ion Annotator

Purpose:
Parse an mzXML mass spectrometry file, compute theoretical b and y fragment
ions for a given peptide sequence, match them to observed MS/MS peaks, and
visualize the annotated spectrum.

Concepts Demonstrated:
- File parsing (gzip, XML)
- Command-line argument handling
- Error checking and validation
- Proteomics domain logic (b/y ion fragmentation)
- Visualization with matplotlib
"""

#Import modules
import gzip
import xml.etree.ElementTree as ET
import sys
from base64 import b64decode
from array import array
import matplotlib.pyplot as plt

#Check if there are enough command-line arguments
if len(sys.argv) < 4:
    print('Please provide mzXML file, scan number, and peptide sequence in that order on command-line.', file=sys.stderr)
    sys.exit(1)


#Check if command line-arguments are valid
try:
    xmlfile = gzip.open(sys.argv[1],'rt')
except FileNotFoundError:
    print('File', sys.argv[1], 'was not found.', file=sys.stderr)
    sys.exit(1)

try:
    scan_number = int(sys.argv[2])
except ValueError:
    print('Input:', sys.argv[2], 'is invalid. Scan number must be an integer', file=sys.stderr)
    sys.exit(1)


peptide_seq = sys.argv[3]


#Get namespace
ns = '{http://sashimi.sourceforge.net/schema/}'


#Parse through file and access peaks
for event, elem in ET.iterparse(xmlfile):
    if elem.tag == (ns + 'scan'):
        scan_num = int(elem.attrib.get('num'))

        if scan_num == scan_number:
            peaks_ele = elem.find(ns + 'peaks')
            peaks = array('f', b64decode(peaks_ele.text))
            if sys.byteorder != 'big':
                peaks.byteswap()

            mzs = peaks[::2]
            ints = peaks[1::2]
            
            
            #print(mzs)
            #print(ints)
        elem.clear()
            
xmlfile.close()

mw = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
      'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
      'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
      'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06 }

#Make sure only valid mw are being used
valid_aa = mw.keys()
for aa in peptide_seq:
    if aa not in valid_aa:
        print('Please only provide characters from the single-letter amino acid code.', file=sys.stderr)
        sys.exit(1)
        
#Compute b and y ions
def compute_ions(peptide):
    b_ions = []
    y_ions = []

    n_term = 0
    c_term = 0

    for i in range(len(peptide)):
        n_term += mw[peptide[i]]
        b_ions.append(n_term + 1)

        c_term += mw[peptide[-(i + 1)]]
        y_ions.append(c_term + 19)

    return b_ions, y_ions

b_ions, y_ions = compute_ions(peptide_seq)

#print('b_ions:', b_ions)
#print('y_ions:', y_ions)


#Annotate b and y ions and match to peaks 
def annotate_peaks(b_ions, y_ions, mzs, ints):
    b_annotations = []
    y_annotations = []

    max_ints = max(ints)
    ints_threshold = max_ints * 0.05

    for i, mz in enumerate(mzs):
        if ints[i] >= ints_threshold:
            for j, b_ion in enumerate(b_ions):
                if abs(mz - b_ion) <= 0.05:
                    annotation = ['b'+str(j + 1), mz, ints[i]]
                    b_annotations.append(annotation)

            for j, y_ion in enumerate(y_ions):
                if abs(mz - y_ion) <= 0.05:
                    annotation = ['y'+str(j + 1), mz, ints[i]]
                    y_annotations.append(annotation)

    return b_annotations, y_annotations

b_annots, y_annots = annotate_peaks(b_ions, y_ions, mzs, ints)
#print(b_annots)
#print(y_annots)

if not b_annots and not y_annots:
    print('No matching b or y ions found in the spectrum.', file=sys.stderr)
    sys.exit(1)
elif not b_annots:
    print('No matching b ions found in the spectrum.', file=sys.stderr)
    sys.exit(1)
elif not y_annots:
    print('No matching y ions found in the spectrum.', file=sys.stderr)
    sys.exit(1)


#Prep for plotting
b_labels = []
b_mzs = []
b_ints = []


for annot in b_annots:
    b_labels.append(annot[0])
    b_mzs.append(annot[1])
    b_ints.append(annot[2])


y_labels = []
y_mzs = []
y_ints = []


for annot in y_annots:
    y_labels.append(annot[0])
    y_mzs.append(annot[1])
    y_ints.append(annot[2])

#Plot matched and unmatched peaks
plt.stem(mzs, ints, linefmt='black', markerfmt='None')
plt.stem(b_mzs, b_ints, linefmt='red', markerfmt='None')
plt.stem(y_mzs, y_ints, linefmt='blue', markerfmt='None')

#Plot annotations           
for i in range(len(b_labels)):
    plt.text(b_mzs[i], b_ints[i], b_labels[i], ha='center', fontsize=9, color='black')


for i in range(len(y_labels)):
    plt.text(y_mzs[i], y_ints[i], y_labels[i], ha='center', fontsize=9, color='black')

#Add title and axis labels
plt.title('MS/MS Viewer')
plt.xlabel('Mass-to-Charge Ratio (m/z)')
plt.ylabel('Absolute Intensity')

plt.show()






