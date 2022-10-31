# Trie

## Intro
Trie is also called prefix tree or word search tree. It's a variation structure of hash tree.  
Trie is good at saving and searching strings.  
The advantages indlude:  
  - Using public prefix of strings to reduce query time.  
  - Reducing all meaningless string comparison.  
  - A better query efficiency than Hash Tree.
  
## Structure
![image](https://user-images.githubusercontent.com/116987376/199016899-383de9ec-d78e-487b-a88c-31caa8e9a1a9.png)
This Trie stores four words: cat, god, deer and panda. Dog and deer share a node 'd'.

## Code

### Basic Trie Node Structure

``` python
class TreeNode(object):  
    def __init__(self):
        self.nodes = {}         # Record the current node
        self.is_leaf = False   # If current node is a word
        self.count = 0          # Amount of words in the word trie
```

### Insert word operation

``` python
  def insert(self,word):      
        curr = self
        for ch in word:                       # For each character in the word
            if not curr.nodes.get(ch,None):   # If current node doesn't lead to the subsequent character, create one node
                new_node = TreeNode()
                curr.nodes[ch] = new_node
            curr = curr.nodes[ch]             # Our pointer'curr' goes to the subsequent character
        curr.is_leaf = True
        self.count += 1
        return
```

### Search word operation

``` python
  def search(self,word)：
        curr = self
        try:                            # Try to get to the last possible node according to the character in the word
            for ch in word:            
                curr = curr.nodes[ch]
        except:
            return False
        return curr.is_leaf             # Return if there is this word in the trie
```
