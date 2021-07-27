import requests

# función para extraer el id de la ciudad
def idCity(city):
    
    try:
        # llamada a la api
        r = requests.get('https://www.metaweather.com/api/location/search/', params={'query':city.lower()})

        if 'woeid' in r.text:
            # devuelve la id
            return r.json()[0]['woeid']
        else:
            # devuelve el mensaje de error
            return print(f'\nLo sentimos {city} no es un lugar registrado')
    
    except Exception as error:
        return print('\nSe ha producido un error al llamar al servicio: ', error)
    
# función para extraer la predicción de un día   
def location(city):
    # extraemos la id
    woeid = idCity(city)
    
    # si woeid es un número
    if type(woeid) == int: 
        try:
            # llamada a la api
            r = requests.get('https://www.metaweather.com/api/location/'+ str(woeid))
            return r.json()

        except Exception as error:
            return print('\nSe ha producido un error al llamar al servicio: ', error)
    
    # woeid no es número
    else:
        return woeid

    
    
# lista de capitales     
capitals = ['Dublin', 'Berlin', 'Riga', 'Oslo', 'Moskow', 'Vienna', 'Madrid', 'Paris']

# iteramos sobre el dataframe
for item in capitals:
    # llamada a la función location
    pred = location(item)

    if type(pred) == dict:
        
        # diccionario de temperaturas
        temperatures = {item['applicable_date']:item['max_temp'] for item in pred['consolidated_weather']}
        
        maxtemp = temperatures[max(temperatures)]
        maxdate = max(temperatures)

        print(f'\nCIUDAD: {row[1]}\nTemperatura máxima: {round(maxtemp, 3)}, registrada el {maxdate}')
    else:
        continue
