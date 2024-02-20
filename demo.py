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
load_dotenv()

# if 'df' not in st.session_state:
#    st.session_state['df'], st.session_state['model'], st.session_state['tokenizer'], st.session_state['frequentsearchesinorder'], st.session_state['workplans'] = initialize()

class Demo():

    objectives = ['Identify any specific limitations or concerns regarding the use of the model in a stagflation environment',
                  'Consider model usage risks in hyper-inflation scenario',
                  'What is model impact on meaning of life']

    def __init__(self):
        self.reviewer = OpenAIReviewer(model='gpt-4-turbo-preview')
        self.guidance = read_file('data/whitepaper/AB_2013-07_Model_Risk_Management_Guidance.txt')
        self.moodel = read_file('data/whitepaper/riskcalc-3.1-whitepaper.txt')
        self.moodel_pdf = 'data/whitepaper/riskcalc-3.1-whitepaper.pdf'
        self.render = False
        self.objective = 0

    def analyze(self):
        self.render = True

    def set_objective(self):
        self.objective = Demo.objectives.index(st.session_state.objective)
        self.render = False

    def run(self):

        st.set_page_config(
            page_title="Gen AI for MRM Demoe",
            page_icon=":robot:"
        )

        st.header("Model Whitepaper Analysis")
        # clear_button = st.sidebar.button(label='Clear Chat', on_click=self.clear)

        st.session_state.objectives=st.selectbox(
            '''Analysis Objective''',
            Demo.objectives,
            self.objective,
            key='objective',
            on_change=self.set_objective)
        analyze_button = st.button(label='Analize', on_click=self.analyze)
        
        report, whitepaper = st.tabs(["Feeling Lucky!", "Whitepaper"])
        with whitepaper:
            pdf_viewer(self.moodel_pdf, height=800)
        with report:
            st.markdown(f"> Objective: {Demo.objectives[self.objective]}")
            if self.render:
                st.markdown(self.reviewer.analyze(self.moodel, Demo.objectives[self.objective]))



if 'demo' not in st.session_state:
    st.session_state['demo'] = Demo()
demo = st.session_state.demo
demo.run()
