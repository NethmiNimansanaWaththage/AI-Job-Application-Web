# COMPLETE WORKING JOB POSTING GENERATOR - USES GROQ
# This will work 100%

from groq import Groq

# ============================================
# PASTE YOUR GROQ API KEY HERE
# Get it from: https://console.groq.com
# ============================================
GROQ_API_KEY = "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"  # REPLACE THIS

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

print("\n" + "="*60)
print("🤖 JOB POSTING GENERATOR - POWERED BY GROQ")
print("="*60 + "\n")

# Get job details
job_title = input("📌 Job title (e.g., 'Python Developer'): ")
company_name = input("🏢 Company name: ")
experience_level = input("📊 Experience level (Entry/Mid/Senior/Lead): ")
company_description = input("💼 What does your company do? ")

print("\n" + "="*60)
print("⏳ Generating professional job posting...")
print("="*60 + "\n")

# Create the prompt
prompt = f"""You are an expert HR professional. Create a complete, professional job posting.

JOB TITLE: {job_title}
COMPANY: {company_name}
EXPERIENCE LEVEL: {experience_level}
COMPANY DESCRIPTION: {company_description}

Create a job posting with these exact sections:

# {job_title}

**Company:** {company_name}
**Location:** Remote / Hybrid
**Employment Type:** Full-time
**Experience Level:** {experience_level}

## About Us
{company_description}

## Key Responsibilities
• (Write 6 specific responsibilities)
• Start each with an action verb
• Make them realistic for {experience_level} level

## Requirements
• (Write 6 requirements)
• Include {experience_level} level experience
• Include technical and soft skills

## Nice to Have (Optional)
• (Write 2-3 preferred skills)

## What We Offer
• Competitive salary based on experience
• Health, dental, and vision insurance
• Remote work flexibility
• Professional development budget
• Paid time off and holidays
• (Add 1 more relevant benefit)

## How to Apply
Please submit your resume and a brief cover letter explaining why you're interested.

Equal Opportunity Employer: We celebrate diversity and are committed to creating an inclusive environment.

Make it professional, engaging, and ready to post immediately."""

# Make the API call
try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Fast and capable model
        messages=[
            {"role": "system", "content": "You are an expert HR professional who writes excellent job postings."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    
    # Get the result
    job_posting = response.choices[0].message.content
    
    # Display it
    print(job_posting)
    
    # Save to file
    filename = job_title.lower().replace(' ', '_').replace('/', '_')
    filename = f"{filename}_job_posting.txt"
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(job_posting)
    
    print("\n" + "="*60)
    print("✅ SUCCESS! Your job posting has been created.")
    print(f"💾 Saved to: {filename}")
    print("="*60)
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nTroubleshooting:")
    print("1. Make sure you pasted the correct Groq API key")
    print("2. Check your internet connection")
    print("3. Run: pip install --upgrade groq")
