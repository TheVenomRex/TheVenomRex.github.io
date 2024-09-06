import re

# Function to replace spans of parentheses and their contents with an empty string
def remove_parentheses_spans(text):
    # Regex pattern to match everything between ( and )
    pattern = r'\(.*?\)'  # Non-greedy match to find the smallest span of parentheses
    # Replace spans with an empty string
    result = re.sub(pattern, '', text)
    return result

# Test the function
text = "This is a test (remove this) but keep this [and Keep this too.]"
new_text = remove_parentheses_spans(text)
print(new_text)