#!/usr/bin/env python3
"""
exercise.py - A module to handle storing and retrieving data in Redis
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of calls to a method."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments the call count in Redis."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs of a method."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that stores inputs and outputs in Redis."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        
        return result
    return wrapper

def replay(method: Callable):
    """Display the history of calls of a particular function."""
    redis = method.__self__._redis
    method_name = method.__qualname__
    
    inputs = redis.lrange(f"{method_name}:inputs", 0, -1)
    outputs = redis.lrange(f"{method_name}:outputs", 0, -1)
    
    print(f"{method_name} was called {len(inputs)} times:")
    
    for inp, out in zip(inputs, outputs):
        inp = inp.decode('utf-8')
        out = out.decode('utf-8')
        print(f"{method_name}(*{inp}) -> {out}")

class Cache:
    """
    Cache class for storing and retrieving data in Redis.
    """

    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in Redis and return the generated key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis and optionally apply a conversion function."""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve data as a string."""
        data = self.get(key, lambda d: d.decode('utf-8'))
        return data

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve data as an integer."""
        data = self.get(key, int)
        return data
