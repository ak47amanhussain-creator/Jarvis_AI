from google import genai

client = genai.Client(api_key="YOUR_API_KEY")  


Conversation= """
what is coding
"""

response = client.models.generate_content(
        model="gemini-2.5-Pro",
        contents=f"""
                You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud {Conversation}
                """
    )


print(response.text)


