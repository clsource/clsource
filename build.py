import json

def load():
  with open("projects.json") as f:
    return json.loads(f.read())

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
