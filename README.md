# Facebook Page Posts Scraper  Page Access Token from Facebook Graph API

This code fetches posts from a Facebook page using the Facebook Graph API and saves them in a CSV file. It connects to Facebook's API using the `requests` library, retrieves post data (such as text, image, time, and publisher), and then saves this data in CSV format using the `pandas` library.

## How to Obtain the Page ID and Page Access Token from Facebook Graph API:

### Getting the Page ID:
1. Visit the target page on Facebook.
2. The Page ID can be found in the URL of the page in your browser. It appears after `/page/` in the URL, or you can use Facebook Developer tools like the Graph API Explorer to get the Page ID.

### Getting the Page Access Token:
1. You must have admin or appropriate permissions for the page.
2. Visit the [Facebook Developer Platform](https://developers.facebook.com/).
3. Create a new app if you don't already have one.
4. Go to **Tools** > **Graph API Explorer**.
5. Select the app and choose the page you want to extract data from.
6. Obtain the **Page Access Token** with the necessary permissions (e.g., `pages_read_engagement`).

## Installing Python Libraries:

You need to install two libraries: `requests` for making HTTP requests and `pandas` for data processing. You can install them using the following command:

```bash
pip install requests pandas


Required Page Management Permissions:
The Access Token used must have the necessary permissions to access the page's data, such as:

pages_read_engagement: To access posts and engage with them.
pages_manage_posts: To manage posts.
These permissions must be configured in your app on the Facebook Developer Platform.

Once you have completed these steps and installed the libraries, you can successfully run the code to fetch posts from a Facebook page and save them in a CSV file.

