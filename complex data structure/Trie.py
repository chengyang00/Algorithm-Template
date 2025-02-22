class Trie:
    '''字典树实现'''
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isWord = False

    def insert(self, word: str) -> None:
        '''插入一个单词'''
        node = self
        for c in word:
            node = node.children[c]
        node.isWord = True

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word: str) -> bool:
        '''搜索word是否存在'''
        node = self.searchPrefix(word)
        return node is not None and node.isWord

    def startsWith(self, prefix: str) -> bool:
        '''之前插入的单词的前缀是否包含prefix'''
        return self.searchPrefix(prefix) is not None
