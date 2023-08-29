import requests
import json

def main(args):
    organization = args.get('organization')
    github_token = args.get('GITHUB_TOKEN')
        
    if github_token is None:
        return {'error': 'GitHub token not set'}

    headers = {
        'Authorization': f'Bearer {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Se non viene trovato il nome dell'organizzazione, restituisce un errore
    if organization is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Organization name not exists'})
        }
    
    url = f'https://api.github.com/orgs/{organization}/repos'
    
    response = requests.get(url, headers=headers)

    repositories = response.json()
    
    projects = {}

    if response.status_code == 200:
        for repo in repositories:
            repo_name = repo["name"]
            repo_description = repo["description"]
            projects[repo_name] = repo_description

        return {'repos': projects}
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
