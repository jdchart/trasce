import vosk
import os

class VoskWrapper:
    def __init__(self, **kwargs) -> None:
        model_path = kwargs.get("model", os.path.join(os.getcwd(), "data", "models", "vosk-model-small-fr-0.22"))
        