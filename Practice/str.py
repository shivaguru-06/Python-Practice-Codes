text = "EatHealthyStayHealthy"
output = ''.join(' ' + c.lower() if c.isupper() else c for c in text).strip()
print(output)