import os
import json
import boto3
from utils import getLogger
from abc import ABC, abstractmethod

logger = getLogger(__name__)

calss BedrockModel(ABC):
    
    def __init__(self, model, temperature=0, max_tokens=4096, top_p=0.9, top_k=256):
        self.model = model
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.top_k = top_k
    
    @abstractmethod
    def parameters():
        pass
    
    def call(self, instrucitons, messages):
        pass
    