import re

sentence = "\"The Hitchhiker's Guide to the Galaxy\" was published in 1979"
regex = "\"([\w ']+)\" was published in (\S+)"
print "find_all: %s"%(re.findall(regex, sentence))

match1 = re.match(regex, sentence)
print "match1 groups: %s"%(str(match1.groups()))
print "match1 group1: %s"%(str(match1.group(1)))
print "match1 group1 span: %s"%(str(match1.span(1)))


match2 = re.search("\"(?P<book>[\w ']+)\" was published in (?P<year>\S+)", sentence)
print "match2 groups: %s"%(str(match2.groups()))
print "match2 group1: %s"%(str(match2.group(1)))
print "match2 group1 span: %s"%(str(match2.span(1)))

print "match2 groupdict: %s"%(str(match2.groupdict()))