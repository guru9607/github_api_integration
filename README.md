# GitHub Repository Access Manager

This script facilitates the retrieval of users who have access to a specific repository on GitHub. As a DevOps Engineer managing multiple repositories, it's essential to have an efficient method for regularly checking access permissions. Automating the process of checking access permissions using a Python script integrated with GitHub's API makes the work a lot easier.

## How to Interact with the Application?

There are two primary methods to interact with applications programmatically:


1. **API (Application Programming Interface)**: Allows communication with the application using predefined endpoints.
2. **CLI (Command Line Interface)**: Utilizes commands directly in the terminal to interact with the application.

### Programmatic Access:

- Python scripts leverage libraries like `requests` to communicate with applications exposing their APIs.
- As DevOps engineers, we consume existing APIs rather than developing them ourselves.

## Steps to Run the Script:

1. **Set Up an EC2 Instance** (Optional):

   - If you prefer, you can set up an EC2 instance for running the script. Otherwise, you can run it on your local machine.
   - Create an EC2 instance and log in using your terminal: 
     ```bash
     $ ssh -i YOURFILE.pem ubuntu@00.000.000.00  
     ```
     - Replace `YOURFILE.pem` with your private key file and `00.000.000.00` with your EC2 instance's public IP address.

2. **Clone the Repository**:

   - Clone the GitHub repository containing the script.

3. **Install Dependencies**:

   - Ensure you have the necessary dependencies installed. You can install them using pip:
     ```bash
     $ pip install requests
     ```

4. **Obtain GitHub Credentials**:

   - Create a GitHub Personal Access Token:
     - Navigate to Developer Settings -> Personal Access Tokens -> Generate Token.
     - Ensure the token is kept secure and not shared with others.

5. **Run the Script**:

   - Execute the script with the following command, replacing `ORGANIZATION-NAME` and `REPOSITORY` with the appropriate values:
     ```bash
     $ python script.py ORGANIZATION-NAME REPOSITORY
     ```

By following these steps, you can efficiently retrieve a list of users with access to a specific repository on GitHub.
