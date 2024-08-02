# Bot Setup and Running Instructions

## Prerequisites

Before running the bot, ensure you have completed the following setup steps:

### 1. Set Up a Google Cloud Project and Enable APIs

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on the project drop-down and select **New Project**.
3. Enter a project name and click **Create**.

### 2. Enable the APIs

1. In the Google Cloud Console, make sure you have selected your new project.
2. Go to the **API & Services Dashboard**.
3. Click **Enable APIs and Services**.
4. Search for **Google Docs API** and click on it, then click **Enable**.
5. Repeat the process to enable the **Google Drive API**.

### 3. Set Up OAuth 2.0 Credentials

1. Go to the **Credentials** page in the Google Cloud Console.
2. Click **Create Credentials** and select **OAuth client ID**.
3. Configure the consent screen if you haven't done so:
   - Click **Configure consent screen**.
   - Choose **External** and click **Create**.
   - Fill in the required fields (e.g., App name, User support email).
   - Click **Save and continue** through the remaining steps.
4. Back on the **Create OAuth client ID** page:
   - Select **Desktop app** as the application type.
   - Click **Create**.
   - Download the `credentials.json` file and save it in your project directory.

### 4. Ensure You Have the Latest Version of Python

1. Download and install the latest version of Python from the [official website](https://www.python.org/).
2. Verify the installation by running the following command:
   ```bash
   python --version

### Install Required Libraries

Install the required Python libraries by running the following command:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib scholarly


### Configure the Script

1. Open your script and replace `YOUR_GOOGLE_DOC_ID` with the actual ID of your Google Docs document.
2. Ensure that `credentials.json` is in the same directory as your script.

### Run the Script

1. Navigate to the directory where your script is located.
2. Run the script using Python with the following command:

```bash
python main.py