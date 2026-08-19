import requests
import ctypes
import os
import platform

_here = os.path.dirname(__file__)

if platform.system() == "Windows":
    _lib_name = "libprocessor.dll"
elif platform.system() == "Darwin":
    _lib_name = "libprocessor.dylib"
else:
    _lib_name = "libprocessor.so"

_lib_path = os.path.join(_here, "text_processor", _lib_name)
_lib = ctypes.CDLL(_lib_path)
_lib.clean_text.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
_lib.clean_text.restype = None

def sanitize(text: str, max_len: int = 4096) -> str:
    input_bytes = text.encode("utf-8")
    output_buf = ctypes.create_string_buffer(max_len)
    _lib.clean_text(input_bytes, output_buf, max_len)
    return output_buf.value.decode("utf-8", errors="ignore")

def embed(text: str) -> list[float]:
    clean = sanitize(text)
    resp = requests.post("http://localhost:11434/api/embeddings", json={
        "model": "nomic-embed-text",
        "prompt": clean
    })
    data = resp.json()
    if "embedding" not in data:
        raise RuntimeError(f"Ollama embedding request failed: {data}")
    return data["embedding"]