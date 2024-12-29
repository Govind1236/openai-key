import openai
import requests
import json

# Replace with your actual OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def get_openai_response(prompt):
    """
    Fetches a response from the OpenAI API for the given prompt.

    Args:
        prompt: The question or input for the OpenAI API.

    Returns:
        The response text from the OpenAI API.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose an appropriate engine
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error fetching response from OpenAI: {e}")
        return "Error"

def main():
    # Define the input and output columns
    input_column = "A"  # Replace with the actual input column letter
    output_column = "B"  # Replace with the actual output column letter

    # Get the last row with data in the input column
    last_row = ws.max_row

    # Iterate through each row with a question
    for row in range(2, last_row + 1):  # Assuming row 1 is header
        question = ws.cell(row=row, column=ord(input_column) - 64).value

        if question:
            response = get_openai_response(question)
            ws.cell(row=row, column=ord(output_column) - 64).value = response

if __name__ == "__main__":
    main()