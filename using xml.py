from bs4 import BeautifulSoup

# path to xml file
xml_path = r'C:\Users\NArada...RaaZa\Desktop\New folder\Data_Scrap\customers.xml'

# Load and work with the XML file
with open(xml_path, 'r') as xml_file:
    xml_content = xml_file.read()

# Create a Beautiful Soup object
soup = BeautifulSoup(xml_content, 'lxml')

# Find all <LTTextBoxHorizontal> elements
text_boxes = soup.find_all('LTTextBoxHorizontal')

# Iterate through the text boxes and extract the bbox coordinates
for text_box in text_boxes:
    bbox = text_box['bbox']
    bbox_coordinates = [float(coord) for coord in bbox.split(',')]
    x0, y0, x1, y1 = bbox_coordinates
    print(f"Text Box Bounding Box Coordinates: x0={x0}, y0={y0}, x1={x1}, y1={y1}")