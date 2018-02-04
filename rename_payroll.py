#! python2
# rename_payroll.py - Rename Continental Payrolls based on payments date.

import PyPDF2, os, re, shutil

# Get all the PDF filenames.
pdfFiles = []

for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

regexFechaInicial = r"(?<=([0-9]{2}\/[0-9]{2}\/[0-9]{4}))Fecha inicial de pago"
regexFechaFinal = r"(?<=([0-9]{2}\/[0-9]{2}\/[0-9]{4}))Fecha final de pago"

for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pageObj = pdfReader.getPage(0)
	pageText = pageObj.extractText()
	initialDate = re.search(regexFechaInicial, pageText).group(1)
	finalDate = re.search(regexFechaFinal, pageText).group(1)
	d,m,a = initialDate.split('/')
	initialDate = a+m+d
	d,m,a = finalDate.split('/')
	finalDate = a+m+d
	newFileName = initialDate+"_"+finalDate+".pdf"
	print "Renaming file: " + filename
	print "New filename: " + newFileName
	shutil.copy(filename,newFileName)