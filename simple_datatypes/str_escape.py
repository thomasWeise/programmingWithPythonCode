print("A single quotation mark: '")   # We can simply use the
print('A double quotation mark: "')   # "other" quotation mark...

# But now we need to use escaping.
print("A single (') and a double (\") quotation mark.")

print("\"Hello World!\"")  # We simply put a backslash (\) before
print('\'Hello World\'')   # the forbidden character.
print("\\")                # Backslashes are escaped like this, too.
print("\"\'\\\"\"")        # This becomes "'\""

print("Hello\nWorld!")     # \n is a newline.
print("Hello\r\nWorld!")   # On Windows systems, \r\n is common.

print("The horizontal tab is like a bigger space: '\t'.")

# A backslash before a line break removes the line break.
>>> print("Hello \
... World!")
