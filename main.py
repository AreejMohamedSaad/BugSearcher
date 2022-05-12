
import imp
from bugSearcher import search_bug 
from bugSearcherConverter import search_bug_converter

if __name__ == "__main__":
# both files (bugSearcher , bugSearcherConverter ) are the same logic but with slight diffrent way, to make sure that it will work correct

    try :
        # Calling methods here in normal bugSearcher file 
        bug = search_bug('bug.txt')
        landscape = search_bug('landscape.txt')

        print("Testing bugSearcher file without converting ascii\n")

        # to count number of bugs in bug file 
        print("Number of bugs in bug file : " + str(bug.count(bug)))

        # to count number of bugs in bug file (bug file is a part of landscape file)
        print("Number of bugs in landscape file : " + str(landscape.count(bug)))


        print("\n------------------------------------------------------------------------------\n")

        # Calling methods here in normal bugSearcherConverter file 
        bug = search_bug_converter('bug.txt')
        landscape = search_bug_converter('landscape.txt')

        print("Testing bugSearcherConverter file after converting ascii\n")

        # to count number of bugs in bug file 
        print("Number of bugs in bug file : " + str(bug.count(bug)))

        # to count number of bugs in bug file (bug file is a part of landscape file)
        print("Number of bugs in landscape file : " + str(landscape.count(bug)))
    
    except Exception as e :
      print ("Error occurs " + str(e))
      