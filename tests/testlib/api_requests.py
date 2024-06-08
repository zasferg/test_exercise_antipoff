import requests

host = "http://localhost:8000"

def set_query(data: dict)-> requests.models.Response:
    rs = requests.post(f"{host}/query/",json=data,)
    return rs


def get_history()-> dict:
    rs = requests.get(f"{host}/history/")
    return rs.json()


def get_result(cadastral_number:str)-> dict:
    rs = requests.get(f"{host}/result/{cadastral_number}")
    return rs.json()


def get_ping()-> dict:
    rs = requests.get(f"{host}/ping/")
    return rs.json()
