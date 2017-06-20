import re

# regular expression to match dates in format: 2010-08-27 and 2010/08/27
date_reg_exp = re.compile('\d{4}[-]\d{2}[-]\d{2}')


# a string to test the regular expression above
data="my birthdate is on 1994-12-14 and my friend birthdate is on 1992-05-25"
test_str= """
     fsf2010/08/27sdfsdfsd
     dsf sfds f2010/08/26 fsdf 
     asdsds 2009-02-02 afdf
     """
# finds all the matches of the regular expression and
# returns a list containing them
matches_list=date_reg_exp.findall(data)

# iterates the matching list and prints all the matches
for match in matches_list:
  print match