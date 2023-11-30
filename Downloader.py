import requests
from bs4 import BeautifulSoup as BS
import time
import os

kbos = []
naces = ["011", "012", "013", "014", "015", "016", "017", "021", "022", "023", "024", "031", "032", "051", "052", "061", "062", "071", "072", "081", "089", "091", "099", "141", "142", "143", "151", "152", "161", "162", "171", "172", "181", "182", "191", "192", "201", "202", "203", "204", "205", "206", "211", "212", "221", "222", "231", "232", "233", "234", "235", "236", "237", "239", "241", "242", "243", "244", "245", "251", "252", "253", "254", "255", "256", "257", "259", "261", "262", "263", "264", "265", "266", "267", "268", "271", "272", "273", "274", "275", "279", "281", "282", "283", "284", "289", "291", "292", "293", "301", "302", "303", "304", "309", "310", "321", "322", "323", "324", "325", "329", "331", "332", "351", "352", "353", "360", "370", "381", "382", "383", "390", "411", "412", "421", "422", "429", "431", "432", "433", "439", "451", "452", "453", "454", "461", "462", "463", "464", "465", "466", "467", "469", "471", "472", "473", "474", "475", "476", "477", "478", "479", "491", "492", "493", "494", "495", "501", "502", "503", "504", "511", "512", "521", "522", "531", "532", "551", "552", "553", "559", "561", "562", "563", "581", "582", "591", "592", "601", "602", "611", "612", "613", "619", "620", "631", "639", "641", "642", "643", "649", "651", "652", "653", "661", "662", "663", "681", "682", "683", "691", "692", "701", "702", "711", "712", "721", "722", "732", "732", "741", "742", "743", "749", "750", "771", "772", "773", "774", "781", "782", "783", "791", "799", "801", "802", "803", "811", "812", "813", "821", "822", "823", "829", "841", "842", "843", "851", "852", "853", "854", "855", "856", "861", "862", "869", "871", "872", "873", "879", "881", "889", "900", "910", "920", "931", "932", "941", "942", "949", "951", "952", "960", "970", "981", "982", "990"]
wait = 5

def download(postcode, nace):
    done = False
    i = 1

    while not done:
        listdir = os.listdir("html")
        if (f"{nace} - {i}.html" in listdir):
            i += 1
            continue

        url = f"https://kbopub.economie.fgov.be/kbopub/zoekactiviteitform.html?nacecodes={nace}&keuzeopzloc=postnr&postnummer1={postcode}&page={i}&_ondNP=on&_ondRP=on&vest=true&_vest=on&filterEnkelActieve=true&_filterEnkelActieve=on&actionLu=Zoek"
        response = requests.get(url)

        if response.status_code == 200:

            html = BS(response.text, "html.parser")
            if html.find(attrs={"id": "captcha"}):
                print("CAPTCHA DETECED!!", nace, i)
                exit()

            rows = html.find_all(attrs={"class": ["odd", "even"]})
            if (len(rows) == 0):
                done = True
                time.sleep(wait)
                continue

            file = open(f"html/{nace} - {i}.html", "w")
            file.write(response.text)
            file.close()

            i += 1

            print(f"{naces.index(nace)+1} / {str(len(naces))} - {i-1} done ({nace})")
            time.sleep(wait)
        elif response.status_code == 404:
            done = True
            print(f"{naces.index(nace)+1} / {str(len(naces))} done ({nace})")

postcode = input("Postcode: ")

for nace in naces[223:]:
    download(postcode, nace)