def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x[key])

    #The AI-suggested code uses Python’s built-in sorted() function with a lambda, making it concise and efficient (O(n log n)). The manual implementation uses a nested loop (O(n^2)), which is less efficient and more error-prone. The AI version is preferable for its readability, maintainability, and performance. This demonstrates how AI tools can quickly generate optimal solutions, allowing developers to focus on higher-level logic.