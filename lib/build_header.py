#This function writes the header and project sections of a new file
def build_header(repfile,version,project_id,quote_number,project_name):
    #Write the header section
    repfile.write("<Header>\n")
    repfile.write("Version%%" + version + "\n")
    repfile.write("</Header>\n")

    #Write the projects section
    repfile.write("<Projects>\n")
    repfile.write("ProjectID%%" + project_id + "\n")
    repfile.write("QuoteNum%%" + quote_number + "\n")
    repfile.write("ProjectName%%" + project_name + "\n")

