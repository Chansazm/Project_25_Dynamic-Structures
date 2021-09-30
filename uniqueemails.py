def uniqueaddresses(emails):
    a = set()
    for email in emails:
        first, last = email.split('@')
        if '+' in first:
            first = first[:first.index('+')]
        a.add(first.replace('.','') +'@'+ last)
    return len(a)








#Driver function
emai = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"] #2
print(uniqueaddresses(emai)) #3