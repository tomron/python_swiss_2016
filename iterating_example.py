books = ["The Hitchhiker's Guide to the Galaxy",
"The Restaurant at the End of the Universe", 
"Life, the Universe and Everything",
"So Long, and Thanks for All the Fish",
"Mostly Harmless", "And Another Thing..."]

for index, book in enumerate(books, 1):
	print "\"%s\" is the %s book"%(book, index)

print
publish_years = [1979, 1980, 1982, 1984, 1992, 2009]

for book, year in zip(books, publish_years):
	print "%s was published in %s"%(book, year)


from itertools import takewhile
books_publish_year = zip(books, publish_years)

# All books published before 1900
# Assuming books are sorted

books_before_1990 = takewhile(lambda (book, year): year < 1990, books_publish_year)
print "Books published before 1990:"
print "\n".join([book for book, year in books_before_1990])


# Taking 2 books for to read on my vacation
from itertools import combinations

for book1, book2 in combinations(books, 2):
	print "\"%s\"\t\"%s\""%(book1, book2)


# But which one should I read first?
from itertools import permutations

for book1, book2 in permutations(books, 2):
	print "\"%s\"\t\"%s\""%(book1, book2)


# group by - books by decades
from itertools import groupby

for decade, gr in groupby(books_publish_year, lambda x: 10*(x[1]/10)):
	print decade, ";".join(["\"%s\""%(g[0]) for g in gr])