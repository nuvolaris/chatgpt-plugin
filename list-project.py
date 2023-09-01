import requests

def check_errors(response):
    if response.status_code == 200:
        return None
    return {"body": f"error: Github API Error: {response.reason}"}

def list_projects(organization, token):
    if not organization or not token:
        return {"body": "error: Missing organization or GitHub token"}
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    url = f'https://api.github.com/orgs/{organization}/repos'

    response = requests.get(url, headers=headers)

    return response

def main(args):
    organization = args.get('organization')
    token = args.get('githubtoken')
    
    response = list_projects(organization, token)
    error = check_errors(response)

    if error:
        return {
            'statusCode': response.status_code,
            'body': error
        }

    repositories = response.json()
    
    projects = {}

    for repo in repositories:
        repo_name = repo["name"]
        repo_description = repo["description"]
        projects[repo_name] = repo_description

    return {"body": projects}
