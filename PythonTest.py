from collections import deque

def generateParentheses(n):
    result = []
    queue = deque([("", 0, 0)])  # Start with an empty string and 0 open and close counts
    
    while queue:
        s, left, right = queue.popleft()
        
        # If the current string is complete, add it to the result
        if len(s) == 2 * n:
            result.append(s)
            continue
        
        # Add an opening parenthesis if possible
        if left < n:
            queue.append((s + "(", left + 1, right))
        
        # Add a closing parenthesis if possible
        if right < left:
            queue.append((s + ")", left, right + 1))
    
    return result

# Example usage
n = 3
combinations = generateParentheses(n)
for combo in combinations:
    print(combo)
