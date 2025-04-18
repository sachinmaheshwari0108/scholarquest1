from bs4 import BeautifulSoup
import json
import csv


with open("scholarshipforme.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")

scholarships = []

cards = soup.find_all("div", class_="single-job")

for card in cards:
    title = card.find("h4").text.strip()
    
    link_tag = card.find("a", href=True)
    link = link_tag['href'] if link_tag else ""

    items = card.find_all("li")
    deadline = amount = location = category = "N/A"

    for li in items:
        text = li.text.strip()
        if "Last Date:" in text:
            deadline = text.replace("Last Date:", "").strip()
        elif "Amount:" in text:
            amount = text.replace("Amount:", "").strip()
        elif "Location:" in text:
            location = text.replace("Location:", "").strip()
        elif "category=" in str(li):  # From link
            category = li.find("a").text.strip()

    scholarships.append({
        "title": title,
        "amount": amount,
        "deadline": deadline,
        "location": location,
        "category": category,
        "link": link
    })


with open("scholarships.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=scholarships[0].keys())
    writer.writeheader()
    writer.writerows(scholarships)


































