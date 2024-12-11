import os
import json
import boto3
from utils import getLogger
from abc import ABC, abstractmethod

logger = getLogger(__name__)

class BedrockModel(ABC):
    
    def __init__(self, model, temperature=0, max_tokens=4096, top_p=0.9, top_k=256):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.top_k = top_k
    
    @abstractmethod
    def get_body(instructions, messages):
        pass
    
    @abstractmethod
    def get_content(response):
        pass
    
    def invoke(self, instructions, messages):
        brt = boto3.client(service_name='bedrock-runtime')
    
        body = self.get_body(instructions, messages)
        accept = 'application/json'
        contentType = 'application/json'

        response = brt.invoke_model(body=body, modelId=self.model, accept=accept, contentType=contentType)

        return self.get_content(json.loads(response.get('body').read())) 

class Jamba(BedrockModel):
    
    jamba_15_large = 'ai21.jamba-1-5-large-v1:0'
    jamba_15_mini = 'ai21.jamba-1-5-mini-v1:0'

    def get_body(self, instructions, messages):
        system = [{
            "role": "system",
            "content": instructions
        }]
        
        return json.dumps({
        "messages": system + messages,
        "max_tokens": self.max_tokens,
        "temperature": self.temperature,
        "top_p": self.top_p 
        })

    
    #return response_body.get('content')[0]['text']    
    def get_content(self, response):
        return response.get('choices')[0].get('message').get('content') 

class Claude(BedrockModel):
    sonnet35 = 'us.anthropic.claude-3-5-sonnet-20241022-v2:0'
    sonnet35_arn = 'arn:aws:bedrock:us-east-1:827075926781:inference-profile/us.anthropic.claude-3-5-sonnet-20241022-v2:0'
    haiku35 = 'us.anthropic.claude-3-5-haiku-20241022-v1:0'
    haiku35_arn = 'arn:aws:bedrock:us-east-1:827075926781:inference-profile/us.anthropic.claude-3-5-haiku-20241022-v1:0'
    sonnet3 = 'anthropic.claude-3-sonnet-20240229-v1:0'
    haiku3 = 'anthropic.claude-3-haiku-20240307-v1:0'
    
    def get_body(self, instructions, messages):
        return json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "system": instructions,
        "messages": messages,
        "max_tokens": self.max_tokens,
        "temperature": self.temperature,
        "top_p": self.top_p,
        "top_k": self.top_k
        })
    
    def get_content(self, response):
        return response.get('content')[0]['text'] 
