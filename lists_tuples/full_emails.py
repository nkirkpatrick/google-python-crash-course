def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("nkirkpatrick@sempraglobal.com", "Norbert Kirkpatrick"), ("mmenard@sempraglobal.com", "Michael Menard")]))

