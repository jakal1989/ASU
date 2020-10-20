import requests
import datetime
import time

now = datetime.datetime.now()

class Rest:
    @staticmethod
    def post():
        #Rest Post from Postman
        print ("Rest Post send")
        now = datetime.datetime.now()
        print (now.strftime("%Y-%m-%d %H:%M:%S"), file=open('Update_list.txt', 'a'))
        url = "https://f910d01a-4731-411c-8275-ce56ded1ec7e.mock.pstmn.io/post/"
        payload = {'Update': 'post'}
        files = []
        headers = {'SnowPOS': 'Online'}
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        print(response.text.encode('utf8'), file=open('Update_list.txt', 'a'))
        print ("Rest Post saved answer in Update_list")
        time.sleep(10)