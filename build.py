import json
from urllib import request

def load():
  url = "https://raw.githubusercontent.com/NinjasCL/website/main/content/index/projects.json"
  response = request.urlopen(url)
  return json.loads(response.read())

def main():
  data = load()
  out = ""
  for category in data["projects"]:
    
    out += f"""\n# {category["emoji"]} · {category["title"]}"""

    for item in category["items"]:

      out += f"""

## [{item["name"]}]({item["url"]})
{item["about"]}

- Tech: `{item["tech"]}`
- Start: {item["start"]}
- End: {item["end"]}
"""
  
  print(out)

if __name__ == "__main__":
  main()
