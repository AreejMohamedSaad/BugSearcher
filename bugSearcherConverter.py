

def search_bug_converter(file_name):
    try:
        ascii_str = ''
        with open(file_name, 'r') as reader:
            for line in reader.readlines():
                # remove new line and spaces to be able to convert them easily 
                for character in line.replace('\n', '').replace(' ', ''):
                    # ord() function returns an integer representing the Unicode code of character
                    # convert the unicode to string to be easy to search with in text file 
                    ascii_str += str(ord(character))
            return ascii_str

    except IOError:
      print ("Error: File does not appear to exist.")
      return 0
