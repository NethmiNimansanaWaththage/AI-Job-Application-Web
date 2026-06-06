import google.generativeai as genai

# YOUR API KEY HERE
genai.configure(api_key="YOUR_API_KEY_HERE")

print("Checking available models...\n")

try:
    for model in genai.list_models():
        print(f"Model name: {model.name}")
        print(f"  Supports generateContent: {'generateContent' in model.supported_generation_methods}")
        print()
except Exception as e:
    print(f"Error: {e}")
