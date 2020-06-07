def email_list(domains):
	emails = []
	for domain_name, users in domains.items():
	  for user in users:
	    emails.append("{}@{}".format(user, domain_name))
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


#wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
#for clothing, colors in wardrobe.items():
#    for color in colors:
#        print("{} {}".format(color, clothing))


#def full_emails(people):
#   result = []
#    for email, name in people:
#        result.append("{} <{}>".format(name, email))
#   return result

