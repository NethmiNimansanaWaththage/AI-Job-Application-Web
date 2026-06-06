# JOB POSTING GENERATOR - BEAUTIFUL WEB UI
# Run with: streamlit run web_app.py

import streamlit as st
from groq import Groq
import time

# Page configuration
st.set_page_config(
    page_title="AI Job Posting Generator",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .stButton > button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px;
    }
    .stTextInput > div > div > input {
        font-size: 16px;
    }
    .success-message {
        padding: 10px;
        border-radius: 5px;
        background-color: #d4edda;
        color: #155724;
    }
    </style>
""", unsafe_allow_html=True)

# Title and header
st.title("🤖 AI Job Posting Generator")
st.markdown("*Create professional job postings in seconds*")
st.markdown("---")

# Sidebar with information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This app uses **Groq AI** to generate professional job postings.
    
    **Features:**
    - 📝 Professional formatting
    - 🎯 Industry-standard requirements
    - 💼 Customizable benefits
    - 📥 Download as text file
    
    **Free to use!**
    """)
    
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit & Groq")

# Main form
with st.form("job_posting_form"):
    st.subheader("📋 Job Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        job_title = st.text_input(
            "Job Title *",
            placeholder="e.g., Senior Python Developer",
            help="Enter the exact job title"
        )
        
        experience_level = st.selectbox(
            "Experience Level *",
            ["Entry Level", "Mid Level", "Senior", "Lead", "Principal"],
            help="Select the required experience level"
        )
    
    with col2:
        company_name = st.text_input(
            "Company Name *",
            placeholder="e.g., TechCorp Inc.",
            help="Your company name"
        )
        
        location = st.selectbox(
            "Location Type",
            ["Remote", "Hybrid", "On-site", "Flexible"],
            help="Work location preference"
        )
    
    company_description = st.text_area(
        "Company Description *",
        placeholder="Describe what your company does... e.g., 'We're a fast-growing startup building AI solutions for healthcare'",
        height=100,
        help="Tell candidates about your company"
    )
    
    # Optional fields expander
    with st.expander("➕ Optional Details (Click to add more)"):
        col3, col4 = st.columns(2)
        with col3:
            salary_range = st.text_input(
                "Salary Range (Optional)",
                placeholder="e.g., $80,000 - $100,000"
            )
            hiring_urgency = st.selectbox(
                "Hiring Urgency",
                ["Immediate", "Within 30 days", "Within 90 days", "Flexible"]
            )
        with col4:
            work_hours = st.text_input(
                "Work Hours (Optional)",
                placeholder="e.g., 9 AM - 5 PM EST or Flexible"
            )
            team_size = st.number_input(
                "Team Size (Optional)",
                min_value=0,
                placeholder="Number of team members"
            )
    
    st.markdown("---")
    
    # Submit button
    submitted = st.form_submit_button("🚀 Generate Job Posting", use_container_width=True)

# Store Groq API key (you can also use secrets management)
GROQ_API_KEY = "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"  # REPLACE WITH YOUR ACTUAL KEY

# Process the form
if submitted:
    if not job_title or not company_name or not company_description:
        st.error("❌ Please fill in all required fields (*)")
    else:
        with st.spinner("🤖 AI is writing your job posting... (takes 10-15 seconds)"):
            try:
                # Initialize Groq client
                client = Groq(api_key=GROQ_API_KEY)
                
                # Create progress bar
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                # Build the prompt
                prompt = f"""You are an expert HR professional. Create a detailed, professional job posting.

JOB TITLE: {job_title}
COMPANY: {company_name}
EXPERIENCE LEVEL: {experience_level}
LOCATION: {location}
COMPANY DESCRIPTION: {company_description}
{f"SALARY RANGE: {salary_range}" if salary_range else ""}
{f"HIRING URGENCY: {hiring_urgency}" if hiring_urgency else ""}
{f"WORK HOURS: {work_hours}" if work_hours else ""}
{f"TEAM SIZE: {team_size}" if team_size else ""}

Create an engaging job posting with these sections:

# {job_title}

**Company:** {company_name}
**Location:** {location}
**Employment Type:** Full-time
**Experience Level:** {experience_level}
{f"**Salary Range:** {salary_range}" if salary_range else ""}

## About Us
{company_description}

## The Opportunity
Write 2-3 exciting sentences about why this role matters and the impact the candidate will make.

## Key Responsibilities
• (Write 6 specific, actionable responsibilities)
• Start each with an action verb

## What You'll Bring
### Required Qualifications
• (Write 6 requirements including {experience_level} level experience)
• Include technical skills, soft skills, and education

### Nice to Have (Bonus Points)
• (Write 2-3 preferred qualifications)

## What We Offer
• Competitive salary based on experience
• Comprehensive health benefits
• {location} work flexibility
• Professional development budget
• Paid time off and holidays
• {f"Salary range: {salary_range}" if salary_range else "Equity or bonus potential"}
• (Add 2 more relevant benefits)

{f"## Hiring Timeline\n{hiring_urgency}" if hiring_urgency else ""}

## How to Apply
Please submit your resume and a brief cover letter explaining why you're interested in this role.

## Equal Opportunity
We are an equal opportunity employer. We celebrate diversity and are committed to creating an inclusive environment for all employees.

Make it professional, inclusive, and ready to post immediately. Use markdown formatting with bold text and bullet points."""

                # Generate the job posting
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are an expert HR professional who writes excellent, detailed job postings."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                )
                
                job_posting = response.choices[0].message.content
                
                # Clear progress bar
                progress_bar.empty()
                
                # Display success message
                st.success("✅ Job posting generated successfully!")
                
                # Display the result in a nice box
                st.markdown("### 📄 Your Job Posting")
                st.markdown("---")
                st.markdown(job_posting)
                
                # Download button
                st.markdown("---")
                col_download1, col_download2 = st.columns(2)
                
                with col_download1:
                    st.download_button(
                        label="📥 Download as Text File",
                        data=job_posting,
                        file_name=f"{job_title.lower().replace(' ', '_')}_job_posting.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                with col_download2:
                    if st.button("🔄 Generate Another", use_container_width=True):
                        st.rerun()
                
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.info("Please check your Groq API key and try again")

# Footer
st.markdown("---")
st.markdown("*Powered by Groq AI - 100% Free*")
