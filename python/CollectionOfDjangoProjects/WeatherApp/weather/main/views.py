from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urlib,request to make a request to api
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        '''  apit key might be expired user you own api_key
             place api_key in place of appid="your_api_key_here) " '''

        # source contain JSON dat from API 
        #NOTE: need a personal api weaher key  
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q ='
            + city + '&appid = your_api_key_here').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)
