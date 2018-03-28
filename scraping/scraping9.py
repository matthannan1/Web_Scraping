"""
    From https://www.youtube.com/watch?v=hrdDIrT9kJI
    Going after AncestryDNA matches.

"""
# import re
from robobrowser import RoboBrowser
# from lxml import html

# Create RB object
br = RoboBrowser(parser='lxml')
# Open login web page in RB object
br.open("https://www.ancestry.com/account/signin/")

# Fill in login form
form = br.get_form()
form['username'] = "my_username"
form['password'] = "my_password"
br.submit_form(form)
print(br.url)

src = str(br.parsed())
print(src)

# br.follow_link(link="https://www.ancestry.com/dna/")
# dna_page = br.find('navDNA')
# if br.find('About this tree'):
#    print("Found it!")
# else:
#     print("Nope")    

#br.follow_link(dna_page)
#src = str(dna_page.parsed())
#print(src)




# ("navDNA")
