#!/bin/bash

#################################################################################
# GitHub Collaborator Access Checker
# Author: Guruprasad Gaikwad
# Date: 5th January
# Version : v1
# Description: Checks for users with read access to a specified GitHub repository
#
# Usage: ./script.sh REPO_OWNER REPO_NAME
#   - REPO_OWNER: The owner (username or organization) of the GitHub repository
#   - REPO_NAME: The name of the GitHub repository
#################################################################################3

helper

# GitHub API URL
API_URL="https://api.github.com"

# GitHub username and personal access token 
USERNAME=$username
TOKEN=$token

# User and Repository information
REPO_OWNER=$1
REPO_NAME=$2

# Function to make a GET request to the GitHub API
function github_api_get {
    # Only the funtion github_api_get can access the local variables.
    local endpoint="$1"
    local url="${API_URL}/${endpoint}"

    # Send a GET request to the GitHub API with authentication
    curl -s -u "${USERNAME}:${TOKEN}" "$url" 
}

# Function to list users with read access to the repository
function list_users_with_read_access {
    local endpoint="repos/${REPO_OWNER}/${REPO_NAME}/collaborators"

    # Fetch the list of collaborators on the repository
    collaborators="$(github_api_get "$endpoint" | jq -r '.[] | select(.permissions.pull == true) | .login')"

    # Display the list of collaborators with read access
    if [[ -z "$collaborators" ]]; then
        echo "No users with read access found for ${REPO_OWNER}/${REPO_NAME}."
    else
        echo "Users with read access to ${REPO_OWNER}/${REPO_NAME}:"
        echo "$collaborators"
    fi
}

function helper {
    expected_cmd_args=2
    
    if [ $# -ne $expected_cmd_args ]; then
        echo "Please execute the script with the required command-line arguments."
    fi
}


# Main script

echo "Listing users with read access to ${REPO_OWNER}/${REPO_NAME}..."
list_users_with_read_access