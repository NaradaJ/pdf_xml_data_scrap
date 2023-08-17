import xml.etree.ElementTree as ET
import pandas as pd

# Recursive function to extract data from elements
def extract_data(element):
    data = {
        "tag": element.tag,
        "attributes": element.attrib,
        "text_content": element.text.strip() if element.text else "",
    }

    # Recursively process sub-elements
    for sub_element in element:
        sub_data = extract_data(sub_element)
        data.setdefault("sub_elements", []).append(sub_data)

    return data

# Parse the XML file
tree = ET.parse('path_to_your_xml_file.xml')  # Replace with your XML file path
root = tree.getroot()

# List to store extracted data
extracted_data = []

# Iterate through elements
for element in root:
    extracted_data.append(extract_data(element))

# Create a pandas DataFrame from the extracted data
df = pd.DataFrame(extracted_data)

# Specify the full path to save the CSV file
csv_path = 'path_to_save/csv_filename.csv'  # Replace with your desired CSV file path

# Export the DataFrame to a CSV file using the specified path
df.to_csv(csv_path, index=False)

print(f"Data exported to {csv_path}")
