import google.generativeai as genai
import os

# Template for the prompt
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Configure the Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def parse_with_ollama(dom_chunks, parse_description):
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        # Create the prompt for each chunk
        prompt = template.format(dom_content=chunk, parse_description=parse_description)
        
        # Call the Gemini model with the generated prompt
        response = model.generate_content(prompt)  # Use generate_content to get the response
        
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response.text)  # Append the text of the response

    return "\n".join(parsed_results)
