import requests

def main(args):
    try:    
        file_id = args.get('file_id', 'ByHquY48ncR1nQdhhPU7Bj')
        apitoken = args.get('apitoken')

        api_url = f"https://api.figma.com/v1/files/{file_id}"

        headers = {
            "X-Figma-Token": apitoken
        }

        # mandare questa response a openai
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            figma_file = response.json()
            return {"body": figma_file}
        else:
            return {"body": response.status_code}
        
    except Exception as e:
        return {"body": e}
