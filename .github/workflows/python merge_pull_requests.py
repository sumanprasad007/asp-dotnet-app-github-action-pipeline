import os
import requests

pat_token = os.environ['PAT_TOKEN']
headers = {'Authorization': f'Bearer {pat_token}'}
repo_url = 'https://api.github.com/repos/sumanprasad007/asp-dotnet-app-github-action-pipeline'

# Get the list of open pull requests created by Dependabot
pulls_url = f'{repo_url}/pulls?state=open&head=dependabot'
response = requests.get(pulls_url, headers=headers)
pull_requests = response.json()

# Iterate through the pull requests and merge them
for pr in pull_requests:
    pr_number = pr['number']
    merge_url = f'{repo_url}/pulls/{pr_number}/merge'
    requests.put(merge_url, headers=headers)
