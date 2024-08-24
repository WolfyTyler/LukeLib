import json
import os

class JSONFileError(Exception):
    pass

def readJsonData(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"O caminho '{path}' não existe ou foi escrito incorretamente.")
        
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content:
                raise ValueError(f"O arquivo JSON em '{path}' esta vazio.")
            else:
                data = json.loads(content)

        if data in ({}, []):
            raise JSONFileError(f"O arquivo JSON em '{path}' contém um dicionário ou lista vazia.")
        elif isinstance(data, list) and all(isinstance(item, (dict, list)) and not item for item in data):
            raise JSONFileError(f"O arquivo JSON em '{path}' contém um dicionário ou lista com apenas listas ou dicionários vazios.")
        else:
            return data
    
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e
    except Exception as e: 
        raise e