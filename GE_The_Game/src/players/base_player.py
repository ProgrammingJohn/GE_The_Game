

from abc import ABC, abstractmethod



class BasePlayer(ABC):
    
    def __init__(self): pass


    @abstractmethod
    def method(): raise NotImplementedError(f'Must overwrite this method.')