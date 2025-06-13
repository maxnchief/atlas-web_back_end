#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        # Store input arguments as string
        self._redis.rpush(input_key, str(args))
        # Call the original method
        output = method(self, *args, **kwargs)
        # Store output as string
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper

def replay(method: Callable) -> None:
    """Display the history of calls of a particular function."""
    r = method.__self__._redis
    qualname = method.__qualname__
    calls = int(r.get(qualname) or 0)
    print(f"{qualname} was called {calls} times:")
    inputs = r.lrange(f"{qualname}:inputs", 0, -1)
    outputs = r.lrange(f"{qualname}:outputs", 0, -1)
    for inp, out in zip(inputs, outputs):
        inp_str = inp.decode('utf-8')
        out_str = out.decode('utf-8')
        print(f"{qualname}(*{inp_str}) -> {out_str}")

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        if isinstance(data, bytes):
            value = data
        elif isinstance(data, str):
            value = data.encode('utf-8')
        else:
            value = str(data).encode('utf-8')
        self._redis.set(key, value)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda d: d.decode('utf-8') if d is not None else None)

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=lambda d: int(d) if d is not None else None)
