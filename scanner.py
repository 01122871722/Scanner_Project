import re

# Define token types with COMMENT pattern placed first
TOKEN_TYPES = {
   

    # Keywords
    'KEYWORD': r'\b(break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)\b',

   
    # Identifiers
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',

    # Numeric constants and variable
    'Numeric': r'\b\d+(\.\d+)?\b',
    # Whitespace
    'WHITESPACE': r'[ \t]+',

    # Newline
    'NEWLINE': r'\n',
     # Comments 
    'COMMENT': r'//[^\n]*|/\*[\s\S]*?\*/',

    # Operators
    'OPERATOR': r'(\+\+|--|\+=|-=|\*=|/=|==|!=|<=|>=|->|&&|\|\||<<|>>|[+\-*/%&|^!~<>=])',

    # String literals
    'STRING_LITERAL': r'"([^"\\]*(\\.[^"\\]*)*)"', 

    # Character constants
    'CHAR_LITERAL': r"'([^'\\]|\\.)'", 

    # Special characters
    'SPECIAL_SYMBOL': r'[{}()[\],;.#]',

    
}

# Function to tokenize the entire code at once
def tokenize(code):
    tokens = []
    # Combine all patterns into one regex pattern
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES.items())
    
    # Iterate through matches in the entire code
    for match in re.finditer(token_regex, code, re.DOTALL):  # Apply re.DOTALL to match multi-line comments
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != 'WHITESPACE':  # Ignore whitespace tokens
            tokens.append((token_type, token_value))
    return tokens

# Function to analyze the code as a single block
def analyze_code(code):
    tokens = tokenize(code)
    for token_type, token_value in tokens:
        print(f"Token: Type = {token_type}, Value = {repr(token_value)}")
    print()  # Separate token output

# Main program
if __name__ == "__main__":
    print("Enter your C code (type 'END' on a new line to finish):")
    code_lines = []
    while True:
        line = input()
        if line == "END":
            break
        code_lines.append(line)
    
    code = "\n".join(code_lines)  # Join the lines to form the complete code
    analyze_code(code)
