formatter = "%r %r %r %r"

# Prints numbers as is.
print formatter % (1, 2, 3, 4)
# Prints the strings quoted with single-quoutes.
print formatter % ("one", "two", "three", "four")
# Prints the four booelan values, no quotes since they are boolen.
print formatter % (True, False, False, True)
# Prints the formatter string four times single-quoted.
print formatter % (formatter, formatter, formatter, formatter)
# Prints the all the strings single-quoted except the third, it is double-quoted
# because it has the apostrophe in "didn't".
print formatter % (
                    "I had this thing",
                    "That you could type up right.",
                    "But it didn't sing.",
                    "So I said goodnight."
                  )
