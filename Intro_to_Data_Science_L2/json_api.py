import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    # 
    # Once you've done this, return the name of the number 1 top artist in
    # Spain. 
    
    #Call the API to get data
    data = requests.get(url).text
    #store data into a python dict
    data = json.loads(data);
    
    print data['topartists']['artist'][0]['name'];
    
    rname = data['topartists']['artist'][0]['name'];
    
    return rname # return the top artist in Spain
    

if __name__ == '__main__':

  url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=4beab33cc6d65b05800d51f5e83bde1b&format=json'
  
  #print the name of the top artist
  print api_get_request(url);
  
