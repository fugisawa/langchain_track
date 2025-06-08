import os
import importlib
import sys
import types


class DummyClass:
    def __init__(self, *args, **kwargs):
        pass


def test_reload_sets_token(monkeypatch):
    token = "dummy_token"
    monkeypatch.setenv("HUGGINGFACE_API_TOKEN", token)
    chat_mod = types.ModuleType("chat")
    llms_mod = types.ModuleType("llms")
    chat_mod.ChatHuggingFace = DummyClass
    llms_mod.HuggingFaceEndpoint = DummyClass
    monkeypatch.setitem(sys.modules, "langchain_huggingface.chat_models.huggingface", chat_mod)
    monkeypatch.setitem(sys.modules, "langchain_huggingface.llms.huggingface_endpoint", llms_mod)
    import notebook_fix
    importlib.reload(notebook_fix)
    assert os.environ.get("HUGGINGFACEHUB_API_TOKEN") == token

