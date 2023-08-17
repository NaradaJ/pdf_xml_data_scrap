import pandas as pd 
import pdfquery

# Define the path to the PDF file
pdf_path = r'C:\Users\NArada...RaaZa\Desktop\New folder\Data_Scrap\BDO Global - Monthly Services Desk Statistics Report October 2019.pdf'

# Read the PDF
pdf = pdfquery.PDFQuery(pdf_path)
pdf.load()

# Define the path to save the XML file
xml_path = r'C:\Users\NArada...RaaZa\Desktop\New folder\Data_Scrap\customers.xml'

# Convert the PDF to XML
pdf.tree.write(xml_path, pretty_print=True)

# Access the data using coordinates
table_title = pdf.pq('LTTextLineHorizontal:in_bbox("956,999,1557,1055")').text()

# Print the extracted customer name
print("Extracted table_title:", table_title)
print("Finished")
