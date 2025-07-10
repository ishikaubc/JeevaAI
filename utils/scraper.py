import requests
from bs4 import BeautifulSoup

URL = "https://thalassaemia.org.cy/haemoglobin-disorders/thalassaemia/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Target the main content area
    article = soup.find("article")
    content_div = article.find("div", class_="entry-content")

    # Extract headings and paragraphs
    with open("thalassaemia_info.txt", "w", encoding="utf-8") as f:
        for element in content_div.find_all(["h1", "h2", "h3", "p"]):
            text = element.get_text(strip=True)
            if text:
                f.write(text + "\n\n")

    print("✅ Content saved to thalassaemia_info.txt")
else:
    print(f"❌ Failed to retrieve page: {response.status_code}")
