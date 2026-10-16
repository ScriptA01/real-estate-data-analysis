import xml.etree.ElementTree as ET

tree = ET.parse("data/adverts.xml")
root = tree.getroot()


namespace = {"ns": "http://www.vivareal.com/schemas/1.0/VRSync"}

properties = root.findall(".//ns:Listing", namespace)

print("Total properties:", len(properties))

for property in properties:
    property_id = property.findtext("ns:ListingID", default="N/A", namespaces=namespace)
    property_title = property.findtext("ns:Title", default="N/A", namespaces=namespace)

    property_transaction_type = property.findtext("ns:TransactionType", default="N/A", namespaces=namespace)

    property_price = property.findtext("ns:Details/ns:ListPrice", default="N/A", namespaces=namespace)
    property_rental_price = property.findtext("ns:Details/ns:RentalPrice", default="N/A", namespaces=namespace)

    if property_price == "N/A":
        property_price = "Sale price not available"
    else:
        property_price = float(property_price)
        property_price = f"R$ {property_price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

       

    if property_rental_price == "N/A":
        property_rental_price = "Rental price not available."
    else:
        property_rental_price = float(property_rental_price)
        property_rental_price = f"R$ {property_rental_price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

   
    property_bedrooms = property.findtext("ns:Details/ns:Bedrooms", default="N/A", namespaces=namespace) 
    property_bathrooms = property.findtext("ns:Details/ns:Bathrooms", default="N/A", namespaces=namespace)


    print(f"Property ID: {property_id}, Title: {property_title}, Sale price: {property_price}, Rental price: {property_rental_price}, Transaction Type: {property_transaction_type}, Total bedrooms: {property_bedrooms}, Total bathrooms: {property_bathrooms}")