import requests

url = 'https://api.openai.com/v1/chat/completions'

def main(args):
    try:    
        file_id = args.get('file_id', 'ByHquY48ncR1nQdhhPU7Bj')
        apitoken = args.get('apitoken')
        chatgpt_api_key = args.get('openaitoken')

        api_url = f"https://api.figma.com/v1/files/{file_id}"

        figma_headers = {
            "X-Figma-Token": apitoken
        }

        openai_headers = {
            'Authorization': f'Bearer {chatgpt_api_key}',
            'Content-Type': 'application/json'
        }

        # mandare questa response a openai (risposta di figma)
        figma_response = requests.get(api_url, headers=figma_headers)

        if figma_response.status_code != 200:
            return {"body": figma_response.status_code}
        
        figma_file = figma_response.json()

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a perfect converter of Figma JSON files into HTML with CSS. Please, ensure accuracy and maintain the original design, included style and text style. The HTML should be titled ChatGPT Plugin."
                },
                {
                    "role": "user",
                    "content": f"Give me Html with Css inside for this Figma Json? Respect exactly style and structure {figma_file}"
                }
            ],
            "temperature": 0.2
        }

        # risposta di openai
        openai_response = requests.post(url, headers=openai_headers, json=data)

        response_data = openai_response.json()

        #this is a mapping created from a file example (a simple page with some text inside), is not sure that can work with others figma files
        content = response_data['choices'][0]['message']['content']

        with open('example.html', "w") as html_file:
            html_file.write(content)
            html_file.flush()

        print(content)

        return {"body": content}
            
    except Exception as e:
        return {"body": e}
