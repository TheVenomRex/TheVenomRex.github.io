import re

# Function to replace ( with [ and ) with ] if there's another ( following
def replace_parentheses_with_brackets(text):
    # Regex pattern: look for ( or ) but only if another ( follows
    pattern = r'\((?=.*\()|\)(?=.*\()'
    # Replace using re.sub
    result = re.sub(pattern, lambda match: '[' if match.group() == '(' else ']', text)
    return result

# Test the function
text = "This is a test (string with) parentheses (and more parentheses)"
new_text = replace_parentheses_with_brackets(text)
print(new_text)