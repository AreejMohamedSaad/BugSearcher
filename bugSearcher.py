

def search_bug(file_name):
    try:
        new_str = ''
        with open(file_name, 'r') as reader:
            for line in reader.readlines():
                # remove new line and spaces in orrder to have a search key string to search by it easily 
                for character in line.replace('\n', '').replace(' ', ''):
                    new_str +=str(character)
                    # now we will search by (||##O||) in the file 
            return new_str

    except IOError:
      print ("Error: File does not appear to exist.")
      return 0

