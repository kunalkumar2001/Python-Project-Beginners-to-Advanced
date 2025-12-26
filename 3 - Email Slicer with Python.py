emailId = input("Enter your email ID: ").strip()

username = emailId[:emailId.index("@")]
domain = emailId[emailId.index("@")+1:]

print(f"Username:{username}, Domain:{domain}")