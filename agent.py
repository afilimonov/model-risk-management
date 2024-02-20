import os
import json
import boto3
from utils import getLogger
from llama_index.llms import ChatMessage, OpenAI
from abc import ABC, abstractmethod

logger = getLogger(__name__)

class MRMReviewer(ABC):
    @abstractmethod
    def analyze(self, model, objective) -> str:
        pass

    @abstractmethod
    def review(self, model, objective, analysis) -> str:
        pass


class OpenAIReviewer(MRMReviewer):
    def __init__(self, model='gpt-4', temperature=0, max_tokens=4096, top_p=0.5, frequency_penalty=0, presence_penalty=0):
        super().__init__()
        # Initialize any additional attributes for OpenAIReviewer
        self.llm = OpenAI(  
            api_key=os.environ.get('OPENAI_API_KEY'),  
            model=model,    
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty)  

    def analyze(self, model, objective) -> str:
        instructions = f"""As a model risk validator, please conduct a detailed model analysis.
        You are provided with model whitepaper and analysis objective. 
        Your response should use Markdown forman and include:
        Bullet points highlighting specific analysis topic with references or direct quotations from the whitepaper, citing specific sections, tables, or figures that support the analysis
        A clear, evidence-based recommendation on whether the model should be adopted for usage,
        considering the identified limitations."""

        messages = [
            ChatMessage(role="system", content=instructions), 
            ChatMessage(role="assistant", content="provide model whitepaper"),
            ChatMessage(role="user", content=model),
            ChatMessage(role="assistant", content="what is analysis objective"),
            ChatMessage(role="user", content=objective)
        ]
        response = self.llm.chat(messages)
        return response.message.content

    def review(self, model, objective, analysis) -> str:
        innstructions = f"""Act as a reviewer to prvide effective challenge of model analysis document.
        Focus on reviewing and challenging model analyssis document and not the model itself.
        You are provided with model whitepaper, analysis objective, and analysis document to perform the peromrme effective challenge. 
        Your response should use well formatted Markdown forman and include:
        Bullet points highlighting specific observiation, concerns and limitation with direct quotations from the 
        model analsisis document citing specific sections that support the challenge.
        A clear, evidence-based sumary of finding and recommendations for improving analysis document.
        <whitepaper>
        {model}
        </whitepaper>
        <objective>
        {objective}
        </objective>
        <analysis>
        {analysis}
        </analysis>"""
    
    
        messages = [ChatMessage(role="system", content=innstructions)]

        response = self.llm.chat(messages)
        return response.message.content
    
    class BendrockReviewer(MRMReviewer):
        def __init__(self, model='anthropic.claude-v2:1', temperature=0, tokens=3000, top_p=0.9, top_k=250):
            super().__init__()
            self.brt = boto3.client(service_name='bedrock-runtime')
            self.model = model
            self.tokens = tokens
            self.top_p = top_p
            self  

        def analyze(self, model, objective) -> str:
            instructions = f"""Human: As a model risk validator, please conduct a detailed model analysis focusing on this objective: {question}
            You are provided with model whitepaper to perform the analysis. 
            Your response should use well formatted Markdown forman and include:
            Bullet points highlighting specific analysis topic with references or direct quotations from the whitepaper, citing specific sections, tables, or figures that support the analysis
            A clear, evidence-based recommendation on whether the model should be adopted for usage,
            considering the identified limitations.
            <context>
            {document}
            </context>
            Assistant:
            """

            body = json.dumps({
            "prompt": instructions,
            "max_tokens_to_sample": self.tokens,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k
            })

            accept = 'application/json'
            contentType = 'application/json'

            response = self.brt.invoke_model(body=body, modelId=model, accept=accept, contentType=contentType)

            response_body = json.loads(response.get('body').read())

            return response_body.get('completion')