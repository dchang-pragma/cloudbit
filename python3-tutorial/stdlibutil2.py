# import reprlib
# #print((set('supercalifragilisticexpialidocious')))
# print(reprlib.repr(set('supercalifragilisticexpialidocious')))

# import pprint
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
#     'yellow'], 'blue']]]

# pprint.pprint(t, width=10)

# import textwrap
# doc = """The wrap() method is just like fill() except that it returns
# a list of strings instead of one big string with newlines to separate
# the wrapped lines."""

# print(textwrap.fill(doc, width=60))


import locale # The locale module accesses a database of culture specific data formats. The grouping attribute of locale’s format function provides a direct way of formatting numbers with group separators
#locale.setlocale(locale.LC_ALL, 'English_United States.1252') #locale.Error: unsupported locale setting
# locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

# conv = locale.localeconv()          # get a mapping of conventions
# x = 1234567.8
# locale.format("%d", x, grouping=True)

# locale.format_string("%s%.*f", (conv['currency_symbol'],
#                      conv['frac_digits'], x), grouping=True)



