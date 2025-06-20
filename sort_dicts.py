def sort_dicts_by_key(dicts, key):
    """AI-suggested: Sorts a list of dictionaries by a specific key using sorted()."""
    return sorted(dicts, key=lambda x: x[key])


def sort_dicts_by_key_manual(dicts, key):
    """Manual: Sorts a list of dictionaries by a specific key using nested loops (O(n^2))."""
    for i in range(len(dicts)):
        for j in range(i + 1, len(dicts)):
            if dicts[i][key] > dicts[j][key]:
                dicts[i], dicts[j] = dicts[j], dicts[i]
    return dicts


data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

print("AI-suggested:", sort_dicts_by_key(data, 'age'))
print("Manual:", sort_dicts_by_key_manual(data.copy(), 'age')) 