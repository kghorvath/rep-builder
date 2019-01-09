def add_product(repfile,prod_id,project_id,tag,partnum,description,mult,quantity,price):
    repfile.write("<Products>\n")
    repfile.write("ProductID%%" + prod_id + "\n")
    repfile.write("ProjectID%%" + project_id + "\n")
    repfile.write("Tag%%" + tag + "\n")
    repfile.write("PartNumber%%" + partnum + "\n")
    repfile.write("Description%%" + description + "\n")
    repfile.write("Multiplier%%" + mult + "\n")
    repfile.write("Quantity%%" + quantity + "\n")
    repfile.write("Price%%" + price + "\n")
    repfile.write("</Products>\n")


