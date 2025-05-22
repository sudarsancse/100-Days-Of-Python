from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())

#--onli show first <a> tag in you page
# print(soup.a)

# all of all <a> tage in you page
all_ancor_tag = soup.find_all(name="a")
# print(all_ancor_tag)

# get all the text insite the ancor tag
for tag in all_ancor_tag:
    #print(tag.getText())
    print(tag.get("href"))

