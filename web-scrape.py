import requests
from bs4 import BeautifulSoup

def get_html(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)
        return None

def get_title(html):
    # Parse the HTML content of the page
    soup = BeautifulSoup(html, 'html.parser')

    # Extract and return the title of the page
    return soup.title.text if soup.title else "Title not found"

def get_links(html):
    # Parse the HTML content of the page
    soup = BeautifulSoup(html, 'html.parser')

    # Extract and return all links on the page
    links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
    return links

def get_text(html):
    # Parse the HTML content of the page
    soup = BeautifulSoup(html, 'html.parser')

    # Extract and return all text from the page
    text = soup.get_text()
    return text.strip()

def main():
    # Get the URL from the user
    user_url = input("Enter the URL of the website you want to scrape: ")

    # Fetch HTML content from the given URL
    html_content = get_html(user_url)

    if html_content:
        # Extract and print the title of the page
        title = get_title(html_content)
        print("Title:", title)

        # Extract and print all links on the page
        links = get_links(html_content)
        print("Links:")
        for link in links:
            print(link)

        # Extract and print all text from the page
        text_content = get_text(html_content)
        print("\nText Content:")
        print(text_content)

if __name__ == "__main__":
    main()
