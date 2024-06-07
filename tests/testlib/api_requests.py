import requests

host = "http://localhost:8000"

def set_query(data: dict)-> requests.models.Response:
    rs = requests.post(f"{host}/query/",json=data,)
    return rs


def get_history(carastral_id:str)-> dict:
    rs = requests.get(f"{host}/history/{carastral_id}")
    return rs.json()


def get_result(id:int)-> dict:
    rs = requests.get(f"{host}/result/{id}")
    return rs.json()


def get_ping()-> dict:
    rs = requests.get(f"{host}/ping/")
    return rs.json()
