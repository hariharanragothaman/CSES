//
// Created by Hariharan Ragothaman on 11/2/21.
//


#include "bits/stdc++.h"
using namespace std;

/*
 *  Given a string, and K words
 *  in how many ways, can you create the string using the words?
 */

class TrieNode
{
public:
    bool isLeaf;
    TrieNode* children[26];
    TrieNode()
    {
        isLeaf = false;
        for(int i=0; i<26; i++) children[i] = NULL;
    }
};

class Trie
{
public:
    TrieNode* root;
    Trie()
    {
        root = new TrieNode;
    }

    void insert(string word)
    {
        auto n = word.size();
        TrieNode* current = root;
        for(int i=0; i<n; i++)
        {
            int val = word[i] - 'a';
            if(current->children[val] == NULL)
            {
                current->children[val] = new TrieNode();
            }
            current = current->children[val];
        }
        current->isLeaf = true;
    }

    bool search(string word)
    {
        auto n =word.size();
        TrieNode* current = root;
        for(int i=0; i<n; i++)
        {
            int val = word[i] - 'a';
            if(current->children == NULL)
            {
                return false;
            }
            current = current->children[val];
        }
        return current->isLeaf;
    }

    bool startWith(string prefix)
    {
        auto n = prefix.size();
        TrieNode* current = root;
        for(int i=0; i<n; i++)
        {
            int val = prefix[i] - 'a';
            if(current->children == NULL)
            {
                return false;
            }
            current = current->children[val];
        }
        return true;
    }

};


int main()
{
    string s;
    cin >> s;
    int T;
    cin >> T;
    string word;
    Trie* obj = new Trie();
    while(T--)
    {
        cin >> word;
        obj->insert(word);
    }

    return 0;
}




















