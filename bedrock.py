import os
import json
import boto3
from utils import getLogger
from abc import ABC, abstractmethod

logger = getLogger(__name__)

class BedrockModel(ABC):
    
    def __init__(self, model, temperature=0, max_tokens=4096, top_p=0.9, top_k=256):
        self.model = model
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.top_k = top_k
    
    @abstractmethod
    def get_body(instructions, messages):
        pass
    
    @abstractmethod
    def get_content(response):
        pass
    
    def call(self, instrucitons, messages):
        brt = boto3.client(service_name='bedrock-runtime')
    
        body = self.get_body(instructions, messages)
        accept = 'application/json'
        contentType = 'application/json'

        response = brt.invoke_model(body=body, modelId=model, accept=accept, contentType=contentType)

        return self.get_content(json.loads(response.get('body').read())) 

class Jamba(BedrockModel):
    
    jamba_15_large = 'ai21.jamba-1-5-large-v1:0'
    jamba_15_mini = 'ai21.jamba-1-5-mini-v1:0'

    def get_body(self, instructions, messages):
        prompt = [
        {
            "role": "system",
            "content": innstrucitons
        }] = messages
        
        return json.dumps({
        "messages": prompt,
        "max_tokens": self.max_tokens,
        "temperature": self.temperature,
        "top_p": self.top_p 
        })

    
    #return response_body.get('content')[0]['text']    
    def get_content(response):
        return response.get('choices')[0].get('message').get('content') 
