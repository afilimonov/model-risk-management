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

logger = getLogger(__name__)

class Demo():

    objectives = ['Identify any specific limitations or concerns regarding the use of the model in a stagflation environment',
                  'Consider model usage risks in hyper-inflation scenario',
                  'What is model impact on meaning of life']

    def __init__(self):
        self.reviewer = OpenAIReviewer(model='gpt-4-turbo-preview')
        self.guidance = read_file('data/whitepaper/AB_2013-07_Model_Risk_Management_Guidance.txt')
        self.moodel = read_file('data/whitepaper/riskcalc-3.1-whitepaper.txt')
        self.moodel_md = read_file('data/whitepaper/riskcalc-3.1-whitepaper.md')
        self.guidance_md = read_file('data/whitepaper/AB_2013-07_Model_Risk_Management_Guidance.md')
        self.run_analysis = False
        self.run_review = False
        self.objective = 0
        self.report = ''
        self.review = ''

    def analyze(self):
        self.run_analysis = True
    
    def do_review(self):
        self.run_review = True

    def set_objective(self):
        self.objective = Demo.objectives.index(st.session_state.objective)
        self.run_analysis = False
        self.run_review = False
        self.report = ''
        self.review = ''

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
        
        whitepaper, report, guidance, review = st.tabs(["Whitepaper :file_folder:", "Analize :bulb:", "AB 2013-07 :file_folder:", "Review :ballot_box_with_check:"])
        with whitepaper:
            with st.container(border=True):
                st.markdown(self.moodel_md)

        with guidance:
            with st.container(border=True):
                st.markdown(self.guidance_md)

        with report:
            with st.container(border=True):
                st.markdown(f"**Objective**: {Demo.objectives[self.objective]}")

            with st.container(border=True):
                analyze_button = st.button(label='Analize', on_click=self.analyze, disabled=self.report != '')
                if self.run_analysis:
                    with st.spinner('Analyzing...'):
                        #st.markdown(self.reviewer.analyze(self.moodel, Demo.objectives[self.objective]))
                        self.report = st.write_stream(self.reviewer.analyze_stream(self.moodel_md, Demo.objectives[self.objective]))
                        self.run_analysis = False
                else:
                    st.markdown(self.report)
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
