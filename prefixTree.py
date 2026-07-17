class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class AutoCompleteSystem:
    def __init__(self):
        self.root = TreeNode()

    def insert_word(self, word):
        current = self.root
        for char in word.lower():      # Store in lowercase
            if char not in current.children:
                current.children[char] = TreeNode()   # Create object
            current = current.children[char]
        current.is_end_of_word = True

    def search_prefix(self, prefix):
        current = self.root
        for char in prefix.lower():
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def collect_words(self, node, current_word, result):
        if node.is_end_of_word:
            result.append(current_word)

        for char, child_node in node.children.items():
            self.collect_words(child_node, current_word + char, result)


def get_suggestions(trie_system, prefix):
    current = trie_system.root

    for char in prefix.lower():
        if char not in current.children:
            return []

        current = current.children[char]

    suggestions = []
    trie_system.collect_words(current, prefix.lower(), suggestions)
    return suggestions


engine = AutoCompleteSystem()

for word in ['Apple', 'Banana', 'Apricot', 'Cherry', 'Avocado', 'Blueberry']:
    engine.insert_word(word)

print("Suggestions for 'ap':")
print(get_suggestions(engine, "ap"))