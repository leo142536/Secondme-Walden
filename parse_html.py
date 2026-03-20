import re
with open("public/index.html", "r", encoding="utf-8") as f:
    text = f.read()
print(f"Total length: {len(text)}")
