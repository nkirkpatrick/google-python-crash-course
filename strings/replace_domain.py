def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


email="nkirkpatrick@sempraglobal.com"
old_domain="sempraglobal.com"
new_domain="sempralng.com"
e_mail = replace_domain(email, old_domain, new_domain)

print("Old Email: " + str(email))
print("New Email: " + str(e_mail))





