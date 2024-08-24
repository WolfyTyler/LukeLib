import json
import os
    
def writeJsonData(path, new_values):
    try: 
        if not os.path.exists(path): 
            raise FileNotFoundError(f"O caminho '{path}' não existe ou foi escrito incorretamente.")
        
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content:
                existing_data = []
            else: 
                existing_data = json.loads(content)

        if isinstance(existing_data, list):
            if any(item == new_values for item in existing_data):
                return 
            else:
                existing_data.append(new_values) 
        else:
            raise ValueError(f"O conteúdo do arquivo '{path}' não é uma lista.")

        with open(path, 'w', encoding='utf-8') as file: 
            json.dump (existing_data, file, indent=4, ensure_ascii=False)

    except FileNotFoundError as e:
        raise e  
    except ValueError as e:
        raise e
    except Exception as e: 
        raise e