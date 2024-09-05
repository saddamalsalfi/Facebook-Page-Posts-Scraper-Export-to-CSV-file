import requests
import pandas as pd

# Place your Page Access Token here
access_token = 'YOUR_PAGE_ACCESS_TOKEN'

# The page ID for the Facebook page
page_id = 'YOUR_PAGE_ID'

# Create a list to store all posts
all_posts = []

# Initial query to get posts with the required fields
url = f'https://graph.facebook.com/v20.0/{page_id}?fields=id,name,posts{{id,message,full_picture,created_time,from{{name}}}}&access_token={access_token}'

# Send a GET request to the API
response = requests.get(url)
data = response.json()

# Check if posts are present in the response
if 'posts' in data:
    posts_data = data['posts']
    
    # Check if there is data in "posts"
    if 'data' in posts_data:
        all_posts.extend(posts_data['data'])

        # Check if there are more pages of posts
        while 'paging' in posts_data and 'next' in posts_data['paging']:
            next_page_url = posts_data['paging']['next']
            response = requests.get(next_page_url)
            data = response.json()

            # Check if the "data" key exists in the response
            if 'data' in data:
                all_posts.extend(data['data'])
            
            # Update posts_data for pagination
            posts_data = data
    else:
        print("No data found in posts.")
else:
    print("No posts found or error fetching data.")

# Check if there are any posts to fetch
if all_posts:
    # Convert the data to a DataFrame
    df = pd.DataFrame(all_posts)

    # Handle missing columns due to absence of certain fields in some posts
    df['created_time'] = df.get('created_time', '')
    df['message'] = df.get('message', '')
    df['full_picture'] = df.get('full_picture', '')
    df['from_user'] = df['from'].apply(lambda x: x['name'] if pd.notna(x) and 'name' in x else '')

    # Select the columns to be saved in the CSV file
    df = df[['id', 'message', 'full_picture', 'created_time', 'from_user']]
    
    # Save the data to a CSV file
    df.to_csv('facebook_page_posts.csv', index=False, encoding='utf-8-sig')

    print("All posts have been saved in the file facebook_page_posts.csv")
else:
    print("No posts found or an error occurred while fetching data.")
