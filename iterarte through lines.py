file_name=input("Enter the file name(with extension): ")
with open(file_name, "r",encoding="utf8") as a_file , open("edu_mails.txt",'w+',encoding="utf8") as b_file:

  for line in a_file:

    stripped_line = line.strip()
    if ".edu" in stripped_line:
        b_file.write(stripped_line)
        b_file.write("\n")
  a_file.close()
  b_file.close()
