import os

class File:
    @staticmethod    
    def delete():
        print ("Delete Update list")
        if os.path.exists("Update_list.txt"):
          os.remove("Update_list.txt")
        else:
          print("The Update_list file does not exist")