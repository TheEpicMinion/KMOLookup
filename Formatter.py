from bs4 import BeautifulSoup as BS
import csv
import os

kbos = []
postcode = "2860"

csvFile = open(f"{postcode}.csv", "a", newline="")
fileWrite = csv.writer(csvFile, delimiter=";")
array = ["KBONumber", "Name", "Address", "Postcode", "City"]
fileWrite.writerow(array)

for file in os.listdir("html"):
    html = open(f"html/{file}", "r").read()
    html = BS(html, "html.parser")

    rows = html.find_all(attrs={"class": ["odd", "even"]})
    for row in rows:
        columns = row.find_all("td")
        if not columns[5].text == "":
            KBONumber = columns[2].find("a").text

            if KBONumber in kbos:
                continue
            kbos.append(KBONumber)

            name = columns[4].text
            street, city = columns[5].text.replace("&nbsp", " ").replace(postcode, f" {postcode}").split(postcode)
            fileWrite.writerow([KBONumber,name,street,postcode,city])
