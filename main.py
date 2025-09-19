import streamlit as st
import pandas as pd
import numpy as np
   
# Page config
st.set_page_config(
    page_title="Reva Malik - Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)
   
# Header
st.title("🚀 Reva Malik")
st.subheader("Computer Science Postgraduate | ML Engineer | Data Analyst")
   
# Professional Summary
st.markdown("---")
st.header("👋 About Me")
   
col1, col2 = st.columns([2, 1])
   
with col1:
    st.markdown("""
    Computer Science Postgraduate with strong foundations in technical troubleshooting, 
    root cause analysis, and large-scale data handling. Skilled in Python, SQL, and C++ 
    with hands-on experience in cloud platforms, database systems, and machine learning.
      
    🎓 **Currently:** PG Diploma in Computer Science - University of Edinburgh  
    🔍 **Looking for:** ML Engineer / Data Analyst positions  
    📍 **Location:** Reading, England, UK
   """)
   
with col2:
    st.markdown("""
    **📞 Contact**
    - 📧 revam862@gmail.com
    - 📱 +44-7934501339
    - 💼 [LinkedIn](https://linkedin.com/in/reva-malik-b62b6021a)
    """)
   
# Skills section
st.markdown("---")
st.header("🛠️ Technical Skills")
   
# Create skill bars
skills = {
    "Python": 90,
    "SQL": 70,
    "C++": 65,
    "Machine Learning": 85,
    "Data Analysis": 80,
    "Deep Learning": 75
}
   
for skill, level in skills.items():
    st.write(f"**{skill}**")
    st.progress(level/100)
   
# Education
st.markdown("---")
st.header("🎓 Education")
   
col1, col2 = st.columns(2)
   
with col1:
    st.subheader("University of Edinburgh")
    st.write("**PG Diploma, Computer Science**")
    st.write("Sept 2024 – June 2025")
    st.write("• Advanced Database Systems")
    st.write("• Applied Machine Learning")
    st.write("• Data-Driven Business Insights")
   
with col2:
    st.subheader("GGSIP University")
    st.write("**B.Tech Information Technology**")
    st.write("2020 – 2024")
    st.write("**CGPA:** 8.92/10")