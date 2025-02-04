import random
import json
import streamlit as st
from agent import OpenAIReviewer
from utils import getLogger
from dotenv import load_dotenv
import streamlit as st
from agent import OpenAIReviewer
from utils import getLogger, read_file
from streamlit_pdf_viewer import pdf_viewer
import instructor
from anthropic import AnthropicBedrock
from pydantic import BaseModel
from tabulate import tabulate
import textwrap
import json_repair
from utils import read_file, save_file

logger = getLogger(__name__)

class AnthropicReviewer():
    
    sonnet3 = 'anthropic.claude-3-sonnet-20240229-v1:0'
    haiku3 = 'anthropic.claude-3-haiku-20240307-v1:0'
    
    def __init__(self):
        self.client = AnthropicBedrock()
        
    def generate_compliance_tasks(self, question, document, model=haiku3):
        message = f"""
        Generate a comprehensive list of tasks to be used to analyze model whitepare compiance with provided AB guidance. Each task includes short description, detailed instructions and list of examples to answer this compliance question: {question}.
        Be as detailed as possible. Number of identified tasks should ensure comprehensive analysis.
        Your response should be a valid json object and nothing else. It should pass json validation when creating loading response into json object using joson.loads python funciton.
        """
        example = """
          Example:
        {[
            {
             'description': 'task desciption',
             'insturctions': 'task instructions',
             'examples': ['example', 'example',...]
            },
          ...
         ]}
        """
        guidance = f"""
        <guidnace>
        {document}
        </guidnace>
        """

        tasks = self.client.messages.create(
            model=model,
            system= guidance,
            max_tokens=3000,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": message + example,
                }
            ])
        #print(tasks.content[0].text)
        return json_repair.loads(tasks.content[0].text)
    
class Demo():

    objectives =['Assess model whitepaper for compliance with AB guidance requirements for model documentation',
                 'Assess model whitepaper for compliance with AB guidance']

    def __init__(self):
        # self.reviewer = OpenAIReviewer(model='gpt-4-turbo-preview')
        self.reviewer = AnthropicReviewer()
        self.guidance = read_file('data/whitepaper/AB_2013-07_Model_Risk_Management_Guidance.txt')
        self.moodel = read_file('data/whitepaper/riskcalc-3.1-whitepaper.txt')
        self.moodel_md = read_file('data/whitepaper/riskcalc-3.1-whitepaper.md')
        self.guidance_md = read_file('data/whitepaper/AB_2013-07_Model_Risk_Management_Guidance.md')
        self.run_generate = False
        self.run_analyze = False
        self.run_review = False
        self.objective = 0
        self.report = ''
        self.review = ''
        self.taks = None
        self.task_table = ''


    def generate(self): 
        self.run_generate = True
        
    def analyze(self):
        self.run_analysis = True
    
    def do_review(self):
        self.run_review = True

    def set_objective(self):
        self.objective = Demo.objectives.index(st.session_state.objective)
        self.run_analysis = False
        self.run_review = False
        self.task_table = ''
        self.report = ''
        self.review = ''
        self.taks = None

    def run(self):

        st.set_page_config(
            page_title="Gen AI for MRM Demoe",
            page_icon=":robot:",
            layout="centered"
        )

        st.header("Model Whitepaper Analysis")

        st.session_state.objectives=st.selectbox(
            '''Analysis Objective''',
            Demo.objectives,
            self.objective,
            key='objective',
            on_change=self.set_objective)
        # analyze_button = st.button(label='Analize', on_click=self.analyze)
        
        whitepaper, guidance, tasks, analysis, review = st.tabs(["Whitepaper :file_folder:", "AB 2013-07 :file_folder:", "Tasks :bulb:","Analysis :bulb:",  "Review :ballot_box_with_check:"])
        with whitepaper:
            with st.container(border=True):
                st.markdown(self.moodel_md)

        with guidance:
            with st.container(border=True):
                st.markdown(self.guidance_md)

        with tasks:
            with st.container(border=True):
                st.markdown(f"**Objective**: {Demo.objectives[self.objective]}")

            with st.container(border=True):
                analyze_button = st.button(label='Generate', on_click=self.generate, disabled=self.report != '')
                if self.run_generate:
                    with st.spinner('Generating...'):
                        self.tasks = self.reviewer.generate_compliance_tasks(Demo.objectives[self.objective], self.guidance_md)
                    headers = ['Task', 'Instructions', 'Examples']
                    data = []
                    for task in tasks['tasks']:
                        data.append([task['description'], task['instructions'], task['examples']])
                    self.task_table = tabulate(data, headers=headers, tablefmt='pipe')
                    st.markdown(self.task_table)
                    #self.report = st.write_stream(self.reviewer.analyze_stream(self.moodel_md, Demo.objectives[self.objective], self.guidance))
                    self.run_generate = False
                else:
                    st.markdown(self.task_table)
                    
        with review:
            with st.container(border=True):
                st.markdown(f"**Objective**: {Demo.objectives[self.objective]}")

            with st.container(border=True):
                analyze_button = st.button(label='Review', on_click=self.do_review, disabled=self.report == '')
                if self.run_review:
                    with st.spinner('Reviewing...'):
                        #st.markdown(self.reviewer.analyze(self.moodel, Demo.objectives[self.objective]))
                        self.report = st.write_stream(self.reviewer.review_stream(self.guidance_md, Demo.objectives[self.objective], self.report))
                        self.run_review = False
                else:
                    st.markdown(self.review)

if 'demo' not in st.session_state:
    st.session_state['demo'] = Demo()
demo = st.session_state.demo
demo.run()
