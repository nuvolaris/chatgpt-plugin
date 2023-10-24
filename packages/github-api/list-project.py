import requests
import redis
import json

def check_errors(response):
    if response.status_code == 200:
        return None
    return {"body": f"error: Github API Error: {response.reason}"}

def list_projects(url, organization, token):
    if not organization or not token:
        return {"body": "error: Missing organization or GitHub token"}
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    if url == "":
        url = f'https://api.github.com/orgs/{organization}/repos?per_page=100'

    response = requests.get(url, headers=headers)

    return response

def main(args):
    r = redis.from_url(args.get("redis_url"))
    p = args.get("redis_prefix")

    organization = args.get('organization','apache')

    if r.exists(f"{p}{organization}"):
        data = r.get(f"{p}{organization}").decode()
        return {"body": json.loads(data)}

    token = args.get('githubtoken')   
    response = list_projects("", organization, token)
    error = check_errors(response)

    if error:
        return {
            'statusCode': response.status_code,
            'body': error
        }

    repositories = response.json()

    count = 0
    max_pages = 9   # max pages retrieved

    while 'next' in response.links.keys() and count <= max_pages:
        next_url = response.links['next']['url']
        response = list_projects(next_url, organization, token)
        repositories.extend(response.json())
        count += 1
    
    projects = {}

    for repo in repositories:
        repo_name = repo["name"]
        repo_description = repo["description"]
        projects[repo_name] = repo_description
    
    # Cache into redis with 1 hour expiration time
    r.set(f"{p}{organization}", json.dumps(projects))
    r.expire(f"{p}{organization}",3600) 
    return {"body": projects}
