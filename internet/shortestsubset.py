# I was asked this question in an interview recently was not able to come up with an optimal solution. Here is the question:

# Question: Given a list of strings, for each string, output the shortest substring that only appears in that string

# Example:

# Input: [ "palantir", "pelantors","cheapair", "cheapoair"]
# output:{
# 	"palantir": "ti", # ti only appears in "palantir"
# 	"pelantors": "s", # s only appears in "pelantors"
# 	"cheapair": "pai" or "apa", # either substring only appears in "cheapair"
# 	"cheapoair": "po" or "oa" # either substring only appears in cheapoair
# }


# Construct a trie of suffixes of all the words and then perform a BFS or DFS until you find a child which was visited once and from there find the first child with number of visits as 1.
# al is missing for word palantir

# public class Main {
#     public static void main(String[] args) {
#         Main obj = new Main();
#         String[] input = {"palantir", "pelantors","cheapair", "cheapoair"};
#         System.out.print(Arrays.toString(obj.findUniqueShortestSubstring(input)));
#     }
    
#     private String[] findUniqueShortestSubstring(String[] strs) {
#         Trie root = new Trie();
#         String[] result = new String[strs.length];
#         for(int i=0; i<strs.length; ++i) {
#             for(int j=0;j<strs[i].length();++j) {
#                 String temp = strs[i].substring(j);
#                 for(int k=1; k<=temp.length(); ++k) {
#                     addToTrie(temp.substring(0, k), i, root, j, j+k);
#                 }
#             }
#         }
        
#         findShortString(root, result, strs);
#         return result;
#     }
    
#     private void findShortString(Trie root, String[] result, String[] strs) {
#         if(root.children == null) return;
#         for(Trie child : root.children) {
#             if(child != null) {
#                 if(child.set.size() == 1) {
#                     int index = child.set.iterator().next();
#                     String temp = strs[index].
#                         substring(child.index[0], child.index[1]);
#                     if(result[index] == null 
#                        || result[index].length() > temp.length()) {
#                         result[index] = temp;
#                     }
#                 }
#                findShortString(child, result, strs); 
#             } 
#         }
#     }
    
#     private void addToTrie(String str, int index, Trie root, int start, int end) {
#         Trie ptr = root;
#         for(char ch : str.toCharArray()) {
#             if(ptr.children == null) {
#                 ptr.children = new Trie[26];
#             }
#             if(ptr.children[ch-'a'] == null) {
#                 ptr.children[ch-'a'] = new Trie();
#             }
#             ptr = ptr.children[ch-'a'];
#         }
#         ptr.index = new int[] {start, end};
#         if(ptr.set == null) ptr.set = new HashSet<>();
#         ptr.set.add(index);
#     }
# }

# class Trie {
#     Trie[] children;
#     int[] index;
#     Set<Integer> set;
# }