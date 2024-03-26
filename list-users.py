import requests
import sys

# GitHub Collaborator Access Checker
# Author: Guruprasad Gaikwad
# Date: 5th January
# Version : v1
# Description: Checks for users with read access to a specified GitHub repository
#
# Usage: python script.py REPO_OWNER REPO_NAME
#   - REPO_OWNER: The owner (username or organization) of the GitHub repository
#   - REPO_NAME: The name of the GitHub repository

# GitHub API URL
API_URL = "https://api.github.com"

# Function to make a GET request to the GitHub API
def github_api_get(endpoint):
    url = f"{API_URL}/{endpoint}"
    # Send a GET request to the GitHub API with authentication
    response = requests.get(url, auth=(USERNAME, TOKEN))
    return response.json()

# Function to list users with read access to the repository
def list_users_with_read_access(repo_owner, repo_name):
    endpoint = f"repos/{repo_owner}/{repo_name}/collaborators"
    # Fetch the list of collaborators on the repository
    collaborators = github_api_get(endpoint)
    # Filter collaborators with pull permission
    collaborators_with_pull_access = [collaborator['login'] for collaborator in collaborators if collaborator['permissions']['pull']]
    return collaborators_with_pull_access

# Main script
if __name__ == "__main__":
    # Check if the script is executed with required command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py REPO_OWNER REPO_NAME")
        sys.exit(1)
    
    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]

    # Prompt the user to enter GitHub credentials
    USERNAME = input("Enter your GitHub username: ")
    TOKEN = input("Enter your GitHub personal access token: ")

    print(f"Listing users with read access to {repo_owner}/{repo_name}...")
    users_with_read_access = list_users_with_read_access(repo_owner, repo_name)
    
    if not users_with_read_access:
        print(f"No users with read access found for {repo_owner}/{repo_name}.")
    else:
        print(f"Users with read access to {repo_owner}/{repo_name}:")
        for user in users_with_read_access:
            print(user)
