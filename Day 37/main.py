import requests
from datetime import datetime

USENAME= "sarkar2456"
TOKEN = "khifvOHD;kdjwpidfkgbsiuf"
today = datetime.now()
print(today)

piexla_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username":USENAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}


##-----------------Step 1------------------------------------##
# res = requests.post(url=piexla_endpoint, json=user_params)
# res.raise_for_status()
# print(res.text)

##-----------------Step 3 (get agraph)------------------------------------##
graph_endpoint =  f"{piexla_endpoint}/{USENAME}/graphs"
graph_config = {
    "id":"graph1",
    "name":"coding",
    "unit": "KM",
    "type":"float",
    "color":"shibafu"
}

headers ={
    "X-USER-TOKEN": TOKEN
}

# res_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(res_graph.text)

##-----------------Step 4------------------------------------##
graph_endpoint_pixel =  f"{piexla_endpoint}/{USENAME}/graphs/graph1"

body ={
    "date":f"{today.strftime("%Y%m%d")}",
    "quantity":"2000"
}

print()
# add_pixel = requests.post(url=graph_endpoint_pixel, headers=headers,json=body)
# print(add_pixel.text)

##-----------------Step 4 (update pixel)------------------------------------##\

graph_pixel_update =  f"{piexla_endpoint}/{USENAME}/graphs/graph1/{today.strftime("%Y%m%d")}"

update ={
    "quantity":"18"
}


# update = requests.put(url=graph_pixel_update, headers=headers, json=update)
# print(update.text)


##-----------------Step 4 (delete pixel)------------------------------------##\

graph_pixel_delete =  f"{piexla_endpoint}/{USENAME}/graphs/graph1/20240513"

delete = requests.delete(url=graph_pixel_delete, headers=headers)
print(delete.text)