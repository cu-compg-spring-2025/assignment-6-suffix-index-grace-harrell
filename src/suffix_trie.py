import argparse
import utils

def get_args():
    parser = argparse.ArgumentParser(description='Suffix Trie')

    parser.add_argument('--reference',
                        help='Reference sequence file',
                        type=str)

    parser.add_argument('--string',
                        help='Reference sequence',
                        type=str)

    parser.add_argument('--query',
                        help='Query sequences',
                        nargs='+',
                        type=str)

    return parser.parse_args()


### Trie Class #######################################################################
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, suffix, index):
        current_node = self.root
        for char in suffix:
            if char not in current_node.children :
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.endOfString = True
    
    def search(self, pattern):
        current_node = self.root
        match_length = 0
        for char in pattern:
            if char in current_node.children:
                current_node = current_node.children[char]
                match_length += 1
            else:
                break
        return match_length

#####################################################################################

def build_suffix_trie(s):
    # YOUR CODE HERE
    trie = Trie()
    for i in range(len(s)):
        suffix = s[i:]
        trie.insert(suffix, i)      
    return trie

def search_trie(trie, pattern):
    return trie.search(pattern)

def main():
    args = get_args()

    T = None

    if args.string:
        T = args.string
    elif args.reference:
        reference = utils.read_fasta(args.reference)
        T = reference[0][1]

    trie = build_suffix_trie(T)

    if args.query:
        for query in args.query:
            match_len = search_trie(trie, query)
            print(f'{query} : {match_len}')

if __name__ == '__main__':
    main()
