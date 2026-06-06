# DESKTOP APP - Modern UI
import customtkinter as ctk
from groq import Groq
import threading
import re

# Appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class JobPostingApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("AI Job Posting Generator")
        self.window.geometry("900x700")
        
        # Groq API key
        self.client = Groq(api_key="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")  # REPLACE
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title = ctk.CTkLabel(
            self.window,
            text="🤖 AI Job Posting Generator",
            font=ctk.CTkFont(size=30, weight="bold")
        )
        title.pack(pady=20)
        
        # Main frame
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(pady=20, padx=40, fill="both", expand=True)
        
        # Input fields
        ctk.CTkLabel(main_frame, text="Job Title:", font=ctk.CTkFont(size=16)).pack(anchor="w", padx=20, pady=(20,5))
        self.job_title = ctk.CTkEntry(main_frame, width=400, height=40, font=ctk.CTkFont(size=14))
        self.job_title.pack(padx=20, pady=(0,15))
        
        ctk.CTkLabel(main_frame, text="Company Name:", font=ctk.CTkFont(size=16)).pack(anchor="w", padx=20, pady=(0,5))
        self.company = ctk.CTkEntry(main_frame, width=400, height=40, font=ctk.CTkFont(size=14))
        self.company.pack(padx=20, pady=(0,15))
        
        ctk.CTkLabel(main_frame, text="Experience Level:", font=ctk.CTkFont(size=16)).pack(anchor="w", padx=20, pady=(0,5))
        self.level = ctk.CTkComboBox(main_frame, values=["Entry Level", "Mid Level", "Senior", "Lead"], width=400, height=40)
        self.level.pack(padx=20, pady=(0,15))
        
        ctk.CTkLabel(main_frame, text="Company Description:", font=ctk.CTkFont(size=16)).pack(anchor="w", padx=20, pady=(0,5))
        self.description = ctk.CTkTextbox(main_frame, width=500, height=100, font=ctk.CTkFont(size=14))
        self.description.pack(padx=20, pady=(0,20))
        
        # Generate button
        self.generate_btn = ctk.CTkButton(
            main_frame,
            text="🚀 Generate Job Posting",
            command=self.generate,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.generate_btn.pack(pady=10, padx=20, fill="x")
        
        # Progress indicator
        self.progress = ctk.CTkProgressBar(main_frame)
        self.progress.pack(pady=10, padx=20, fill="x")
        self.progress.set(0)
        
        # Result text area
        self.result = ctk.CTkTextbox(main_frame, height=300, font=ctk.CTkFont(size=12))
        self.result.pack(pady=20, padx=20, fill="both", expand=True)
        
    def generate(self):
        # Get inputs
        job = self.job_title.get()
        company = self.company.get()
        level = self.level.get()
        desc = self.description.get("1.0", "end-1c")
        
        if not all([job, company, desc]):
            self.result.delete("1.0", "end")
            self.result.insert("1.0", "❌ Please fill in all fields!")
            return
        
        # Disable button and show progress
        self.generate_btn.configure(state="disabled", text="⏳ Generating...")
        self.progress.set(0.5)
        
        # Run in thread
        thread = threading.Thread(target=self.generate_posting, args=(job, company, level, desc))
        thread.start()
    
    def generate_posting(self, job, company, level, desc):
        prompt = f"""Write a professional job posting for {job} at {company}. 
        Level: {level}. Company: {desc}. 
        Include responsibilities, requirements, and benefits."""
        
        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content
            
            # Update UI in main thread
            self.window.after(0, self.display_result, result)
            
        except Exception as e:
            self.window.after(0, self.display_result, f"Error: {e}")
    
    def display_result(self, text):
        self.result.delete("1.0", "end")
        self.result.insert("1.0", text)
        self.generate_btn.configure(state="normal", text="🚀 Generate Job Posting")
        self.progress.set(1)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = JobPostingApp()
    app.run()
