# GitHub API Integration

This script facilitates the retrieval of users who have access to a specific repository on GitHub. As a DevOps Engineer managing multiple repositories, it's essential to have an efficient method for regularly checking access permissions. If suppose someone is resigning the organisation, we also have to revoke the access. Therefore automating the process of checking access permissions using a shell script integrated with GitHub's API makes our work a lot easier.

## How to Interact with the Application?

There are two primary methods to interact with applications programmatically:
1. **API (Application Programming Interface)**: Allows communication with the application using predefined endpoints.
2. **CLI (Command Line Interface)**: Utilizes commands directly in the terminal to interact with the application.

### Programmatic Access:
- Bash scripts leverage tools like `curl` to communicate with applications exposing their APIs (request module is use for python).
- As DevOps engineers, we consume existing APIs rather than developing them ourselves.

## Steps to Run the Script:

1. **Set Up an EC2 Instance**:
   - Create an EC2 instance and log in using your terminal: 
     ```bash
     $ ssh -i YOURFILE.pem ubuntu@00.000.000.00  
     ```
    -  Put you own public IP address. 
2. **Clone the Repository**:
   - Clone the GitHub repository containing the script.

3. **Obtain GitHub Credentials**:
   - You can test it by creating your own organisation.
   - Then, create a Personal Access Token from your GitHub account:
     - Navigate to Developer Settings -> Personal Access Tokens -> Generate Token.
     - Ensure the token is kept secure and not shared with others.

5. **Export Credentials**:
   - Export your GitHub username and token as environment variables:
     ```bash
     $ export username="YOUR_USERNAME"
     $ export token="YOUR_TOKEN"
     ```

6. **Run the Script**:
   - Execute the script with the following command:
     ```bash
     $ ./list-users.sh ORGANIZATION-NAME REPOSITORY
     ```

7. **Install `jq`**:
   - Ensure `jq` is installed on your system to parse JSON responses:
     ```bash
     $ sudo apt install jq -y
     ```

By following these steps, you can efficiently retrieve a list of users with access to a specific repository on GitHub.



