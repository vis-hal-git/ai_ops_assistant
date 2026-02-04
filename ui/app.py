import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.verifier import verifier_agent

st.title("AI Operations Assistant")

task = st.text_input("Enter your task")

if st.button("Run"):
    plan = planner_agent(task)
    data = executor_agent(plan)
    final = verifier_agent(task, data)

    st.subheader("Final Answer")
    st.write(final)
