# _**Biblioteca LukeLib**_ 

![Versão da LukeLib](https://img.shields.io/badge/Distribuição-1.0.0-blue)
![Versões do Python](https://img.shields.io/badge/Python-3.8%2B-blue)

Esta biblioteca é projetada para otimizar projetos em Python que realizam manipulação significativa de arquivos JSON. Ela oferece uma série de ferramentas e funções para facilitar a leitura, escrita e validação de dados em formato JSON, aumentando a eficiência e a robustez do seu código.

Além disso, a biblioteca inclui a função `dynamicImport`, que permite a importação dinâmica de módulos, criação de instâncias de classes e execução de métodos. Essa funcionalidade adicional pode ser útil em projetos que requerem flexibilidade na importação e execução de componentes baseados em JSON ou em outros contextos onde a importação dinâmica é necessária.

## Write Json Data:

A função `writeJsonData` é responsável por adicionar novos valores a um arquivo JSON existente. Ela realiza quatro etapas para garantir que os dados e o aquivo JSON estejam em um formato correto e utilizável.

### 1. Verificação de Caminho:

A primeira etapa verifica se o caminho para o arquivo JSON especificado existe:

```py
try:
    if not os.path.exists(path):
        raise FileNotFoundError(f"O caminho '{path}' não existe ou foi escrito incorretamente.")
```

Se o caminho fornecido não for encontrado, a função levanta um `FileNotFoundError` indicando que o caminho é inválido ou foi digitado incorretamente.

### 2. Leitura do Conteúdo Existente: 

A função então lê o conteúdo do arquivo JSON:

```py
with open(path, 'r', encoding='utf-8') as file:
    content = file.read()
    if not content:
        existing_data = []
    else:
        existing_data = json.loads(content)
```

Se o arquivo estiver vazio, a função inicializa `existing_data` como uma lista vazia. Caso contrário, o conteúdo é carregado e decodificado do formato JSON.

### 3. Adição de Novos Valores:

Em seguida, a função verifica se existing_data é uma lista e adiciona os novos valores, se ainda não estiverem presentes:

```py
if isinstance(existing_data, list):
    if any(item == new_values for item in existing_data):
        return
    else:
        existing_data.append(new_values)
else:
    raise ValueError(f"O conteúdo do arquivo '{path}' não é uma lista.")
```

Se `existing_data` for uma lista, a função verifica se `new_values` já está presente. Se não estiver, os novos valores são adicionados. Se `existing_data` não for uma lista, a função levanta um `ValueError`.

### 4. Salvamento dos Dados Atualizados:

Por fim, a função grava os dados atualizados de volta no arquivo JSON:

```py
with open(path, 'w', encoding='utf-8') as file: 
    json.dump(existing_data, file, indent=4, ensure_ascii=False)
```

Os dados são salvos com indentação de 4 espaços e sem garantir a codificação ASCII, para preservar caracteres especiais.

### Tratamento de Exceções: 

Finalmente, a função trata e repropaga as exceções que podem ocorrer durante a execução:

```py
except FileNotFoundError as e:
    raise e
except ValueError as e:
    raise e
except Exception as e: 
    raise e
```

Cada tipo de erro é tratado conforme sua especificidade e é levantado novamente para permitir o tratamento apropriado em níveis superiores da aplicação.

## Read Json Data: 

A função `readJsonDara` é responsável por ler e validar os dados de um arquivo JSON. Ela realiza três etapas principais para garantir que o arquivo JSON esteja em um formato correto e utilizável. 

### 1. Verificação de Caminho:

A primeira etapa verifica se o caminho para o arquivo JSON especificado existe:

```py
try:
    if not os.path.exists(path):
        raise FileNotFoundError(f"O caminho '{path}' não existe ou foi escrito incorretamente.")
```

Se o caminho fornecido não for encontrado, a função levanta um `FileNotFoundError` indicando que o caminho é inválido ou foi digitado incorretamente.

### 2. Verificação do Conteúdo do Arquivo:

Na segunda etapa, a função verifica se o arquivo JSON está vazio:

```py
with open(path, 'r', encoding='utf-8') as file:
    content = file.read()
    if not content:
        raise ValueError(f"O arquivo JSON em '{path}' esta vazio.")
data = json.loads(content)
```

Se o arquivo estiver vazio após a leitura, a função levanta um `ValueError`. Caso contrário, o conteúdo do arquivo é carregado e decodificado do formato JSON.

### 3. Verificação do Conteúdo do JSON:

A terceira etapa valida o conteúdo JSON para garantir que ele contenha dados válidos:

```py
if data in ({}, []):
    raise JSONFileError(f"O arquivo JSON em '{path}' contém um dicionário ou lista vazia.")
elif isinstance(data, list) and all(isinstance(item, (dict, list)) and not item for item in data):
    raise JSONFileError(f"O arquivo JSON em '{path}' contém um dicionário ou lista com apenas listas ou dicionários vazios.")
else:
    return data
```

Se o conteúdo JSON for um dicionário ou lista vazia, ou se for uma lista contendo apenas listas ou dicionários vazios, a função levanta um `JSONFileError`. Caso contrário, os dados são retornados para uso posterior.

### Tratamento de Exceções: 

Finalmente, a função trata e repropaga as exceções que podem ocorrer durante a execução:

```py
except FileNotFoundError as e:
    raise e
except ValueError as e:
    raise e
except Exception as e: 
    raise e
```

Cada tipo de erro é tratado conforme sua especificidade e é levantado novamente para permitir o tratamento apropriado em níveis superiores da aplicação.

## Dynamic Import:

A função `dynamicImport` permite importar dinamicamente um módulo, criar uma instância de uma classe especificada e executar um método dessa classe com argumentos fornecidos. A função realiza as seguintes operações:

### 1. Importação do Módulo: 

A primeira etapa da função é importar o módulo especificado:

```py
try:
    module = importlib.import_module(module_path)
```

O módulo é importado dinamicamente usando o caminho fornecido. Se o módulo não for encontrado, será levantado um `ModuleNotFoundError`.

### 2. Instanciação da Classe:

Em seguida, a função obtém a classe do módulo e cria uma instância:

```py
imported_class = getattr(module, class_name)
instance = imported_class()
```

A classe é recuperada usando `getattr` e uma nova instância dessa classe é criada.

### 3. Verificação do Método: 

A função então verifica se a classe possui o método especificado e se ele é chamável:

```py
if not hasattr(instance, method_name):
    raise AttributeError(f"A classe '{class_name}' não possui o método '{method_name}'.")

method = getattr(instance, method_name)

if not callable(method):
    raise AttributeError(f"O atributo '{method_name}' não é um método na classe '{class_name}'.")
```

Se o método não existir na classe, a função levanta um `AttributeError`. Além disso, verifica se o atributo é um método chamável.

### Tratamento de Exceções: 

Finalmente, a função trata e repropaga as exceções que podem ocorrer durante a execução:

```py
except FileNotFoundError as e:
    raise e
except AttributeError as e:
    raise e
except Exception as e: 
    raise e
```

Cada tipo de erro é tratado conforme sua especificidade e é levantado novamente para permitir o tratamento apropriado em níveis superiores da aplicação.

## Como Utilizar a LukeLib: 

A `LukeLib` foi projetada para ser intuitiva e fácil de usar, permitindo a manipulação eficiente de arquivos JSON e a importação dinâmica de módulos. Aqui estão alguns exemplos de como você pode usar as principais funcionalidades da biblioteca:

### 1. Escrevendo Dados em um Arquivo JSON:

A função `writeJsonData` é ideal para situações onde você precisa adicionar novos dados a um arquivo JSON existente de forma segura e consistente. Ela garante que os dados sejam escritos em um formato válido, evitando problemas como duplicação de entradas ou corrupção do arquivo JSON.

### Exemplo de Uso: 

```py
from lukelib import writeJsonData

# Caminho para o arquivo JSON
json_path = 'save_file.json'

# Dados que deseja adicionar
new_values = {"nome": "João", "idade": 30}

# Chamada da função
writeJsonData(json_path, new_values)
```
Esse código adicionará o dicionário `new_values` ao arquivo `save_file.json`, garantindo que o conteúdo do arquivo permaneça consistente e válido.

### 2. Lendo e Validando Dados de um Arquivo JSON:

A função `readJsonData` é útil para quando você precisa garantir que os dados de um arquivo JSON estejam em um formato correto e utilizável antes de processá-los. Ela ajuda a evitar erros ao manipular JSONs vazios ou malformados, oferecendo uma camada extra de segurança para a leitura de arquivos.

### Exemplo de Uso:
```py
from lukelib import readJsonData

# Caminho para o arquivo JSON
json_path = 'save_file.json'

# Leitura e validação do arquivo JSON
try:
    data = readJsonData(json_path)
    print(data)
except JSONFileError as e:
    print(f"Erro ao ler o arquivo JSON: {e}")
```
Esse exemplo lerá o conteúdo do arquivo `save_file.json`, validará os dados e imprimirá o conteúdo se estiver correto. Se houver algum problema com o formato do arquivo, um erro será gerado e exibido.

### 3. Importação Dinâmica de Módulos e Execução de Métodos:

A função `dynamicImport` é útil em situações onde você precisa carregar e executar código de maneira dinâmica e flexível. Por exemplo, quando o nome do módulo, classe ou método só é conhecido em tempo de execução, ou em sistemas onde a modularidade e a extensibilidade são cruciais, como plugins ou componentes configuráveis em tempo de execução.

### Exemplo de Uso:

```py
from lukelib import dynamicImport

# Parâmetros de importação dinâmica
module_path = 'Tests.meu_modulo' 
class_name = 'MinhaClasse'
method_name = 'meu_metodo'
args = (arg1, arg2)  # Argumentos posicionais (Opcional)
kwargs = {'chave': valor}  # Argumentos nomeados (Opcional)

# Importa o módulo, cria a instância da classe e executa o método
result = dynamicImport(module_path, class_name, method_name, *args, **kwargs)
print(result)
```

Esse código demonstra como importar o módulo `meu_modulo`, instanciar a classe `MinhaClasse`, e executar o método `meu_metodo` com os argumentos fornecidos. Os parâmetros `args` e `kwargs` são opcionais e podem ser usados conforme necessário. O resultado da execução do método será armazenado na variável `result`.

### Tratamento de Exceções:

A `LukeLib` foi projetada para lidar com exceções comuns que podem ocorrer durante a manipulação de arquivos JSON e a importação dinâmica de módulos. Certifique-se de capturar e tratar essas exceções de maneira adequada em seus projetos para garantir uma execução segura e estável.