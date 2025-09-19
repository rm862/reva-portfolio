import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
   
st.set_page_config(page_title="Projects - Reva Malik", page_icon="📊")
   
st.title("📊 My Projects")
st.markdown("---")
   
# Project 1: Liver Vessel Segmentation
st.header("🏥 Liver Vessel Segmentation - Deep Learning")
   
col1, col2 = st.columns([2, 1])
   
with col1:
    st.markdown("""
    **Objective:** Applied U-Net deep learning model on medical image data
       
    **Key Achievements:**
    - Improved segmentation accuracy using data augmentation techniques
    - Implemented advanced image preprocessing pipelines
    - Achieved high precision in vessel boundary detection

    **Technologies:** Python, PyTorch, Deep Learning, Computer Vision
   """)

with col2:
    # Create a sample visualization
    st.subheader("Model Performance")
       
    metrics = {
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
        'Score': [0.94, 0.91, 0.89, 0.90]
   }
       
    df_metrics = pd.DataFrame(metrics)
    fig = px.bar(df_metrics, x='Metric', y='Score', 
                title="Model Performance Metrics")
    st.plotly_chart(fig, use_container_width=True)
   
st.markdown("---")
   
# Project 2: Time Series Forecasting
st.header("📈 Time-Series Forecasting - Business Analytics")
   
col1, col2 = st.columns([2, 1])
   
with col1:
    st.markdown("""
    **Objective:** Designed forecasting models for sales and demand prediction
       
    **Key Achievements:**
    - Evaluated RMSE and MAPE to improve predictive accuracy
    - Implemented multiple forecasting algorithms
    - Created interactive dashboards for business insights
       
    **Technologies:** Python, Pandas, Time Series Analysis, Statistical Modeling
    """)
   
with col2:
    # Sample time series data
       st.subheader("Forecast Example")
       
       dates = pd.date_range(start='2024-01-01', periods=50, freq='D')
       actual = np.random.randn(50).cumsum() + 100
       forecast = actual + np.random.randn(50) * 0.5
       
       df_ts = pd.DataFrame({
           'Date': dates,
           'Actual': actual,
           'Forecast': forecast
       })
       
       fig = px.line(df_ts, x='Date', y=['Actual', 'Forecast'], 
                    title="Sales Forecast vs Actual")
       st.plotly_chart(fig, use_container_width=True)
   
# Interactive Demo Section
st.markdown("---")
st.header("🎯 Interactive Demo")
   
demo_choice = st.selectbox("Choose a demo:", 
                             ["Data Analysis", "ML Prediction"])
   
if demo_choice == "Data Analysis":
    st.subheader("Sample Data Analysis")
       
    # Generate sample data
    data = {
           'Category': ['A', 'B', 'C', 'D', 'E'],
           'Values': np.random.randint(10, 100, 5),
           'Growth': np.random.uniform(-0.2, 0.5, 5)
       }
       
    df = pd.DataFrame(data)
       
    col1, col2 = st.columns(2)
       
    with col1:
           st.dataframe(df)
       
    with col2:
           fig = px.bar(df, x='Category', y='Values', 
                       title="Sample Analysis")
           st.plotly_chart(fig, use_container_width=True)
   
elif demo_choice == "ML Prediction":
    st.subheader("Simple Prediction Model")
       
    # Simple interactive prediction
    feature1 = st.slider("Feature 1", 0.0, 10.0, 5.0)
    feature2 = st.slider("Feature 2", 0.0, 10.0, 5.0)
       
    # Mock prediction
    prediction = (feature1 * 0.6 + feature2 * 0.4) * 10
       
    st.write(f"**Predicted Value:** {prediction:.2f}")
       
    st.progress(min(prediction/100, 1.0))