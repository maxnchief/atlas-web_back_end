#!/usr/bin/env python3
import redis
import uuid
from typing import Union

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        # Convert data to bytes before storing
        if isinstance(data, bytes):
            value = data
        elif isinstance(data, str):
            value = data.encode('utf-8')
        else:
            value = str(data).encode('utf-8')
        self._redis.set(key, value)
        return key
