#Some example variables to get started with
version = "2018.05"
projectid = "12603"
quotenum = "19EX999"

#Open the file for writing
repfile = open("examples/example_write.xml","w")

#Write the header
version_write = "Version%%Version " + version

repfile.write("<Header>\n")
repfile.write(version_write + "\n")
repfile.write("</Header>\n")

#Write the project information
projectid_write = "ProjectID%%" + projectid
quotenum_write = "QuoteNum%%" + quotenum

repfile.write("<Project>\n")
repfile.write(projectid_write + "\n")
repfile.write(quotenum_write + "\n")
repfile.write("</Project>\n")