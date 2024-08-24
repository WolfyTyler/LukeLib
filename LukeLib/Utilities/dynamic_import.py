import importlib

def dynamicImport(module_path, class_name, method_name, *args, **kwargs):
    try:
        module = importlib.import_module(module_path)
        imported_class = getattr(module, class_name)
        instance = imported_class()

        if not hasattr(instance, method_name):
            raise AttributeError(f"A classe '{class_name}' não possui o método '{method_name}'.")

        method = getattr(instance, method_name)

        if not callable(method):
            raise AttributeError(f"O atributo '{method_name}' não é um método na classe '{class_name}'.")

        return method(*args, **kwargs)

    except ModuleNotFoundError as e:
        raise e
    except AttributeError as e:
        raise e
    except Exception as e:
        raise e
