import streamlit as st
   
st.set_page_config(page_title="Contact - Reva Malik", page_icon="📞")
   
st.title("📞 Get In Touch")
st.markdown("---")
   
# Contact Information
col1, col2 = st.columns(2)
   
with col1:
    st.header("📧 Contact Details")
    st.markdown("""
    **Email:** revam862@gmail.com  
    **Phone:** +44-7934501339  
    **Location:** United Kingdom  
    **LinkedIn:** [reva-malik-b62b6021a](https://linkedin.com/in/reva-malik-b62b6021a)
   """)
       
    st.header("💼 Current Status")
    st.info("🔍 Actively seeking ML Engineer / Data Analyst positions")
       
with col2:
    st.header("📝 Send Message")
       
    # Contact form
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        company = st.text_input("Company (Optional)")
        message = st.text_area("Message", height=150)
           
        submitted = st.form_submit_button("Send Message")
           
        if submitted:
            if name and email and message:
                st.success("Thank you for your message! I'll get back to you soon.")
                st.balloons()
            else:
                st.error("Please fill in all required fields.")
   
st.markdown("---")
   
# Resume Download
st.header("📄 Download Resume")
  
st.markdown("""
Click the button below to download my complete resume:
""")
   
# You'll need to add your actual resume file to the project
st.download_button(
    label="📄 Download PDF Resume",
    data="Resume content would go here",  # Replace with actual file
    file_name="Reva_Malik_Resume.pdf",
    mime="application/pdf"
   )
   
st.markdown("---")
   
# Availability
st.header("🗓️ Availability")
st.markdown("""
**Available for:**
- Full-time positions
- Contract work
- Freelance projects
- Consultations
   
**Preferred roles:**
- Machine Learning Engineer
- Data Analyst
- Python Developer
- Technical Analyst
""")