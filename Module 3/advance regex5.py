import re

print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))

print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

print(re.sub(f"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts955@my.example.com]"))

print(re.sub(r"^([\w.]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))