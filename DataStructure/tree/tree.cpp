#include <iostream>

class tree {
private:
  struct node {
    node *l;
    node *r;
    int key;
    int height;

    node(int key) : key(key), l(nullptr), r(nullptr), height(1) {}
  };

  node *root;

  node *searchHelper(node *current, int key) {
    if (!current || current->key == key)
      return current;

    if (current->key < key) {
      return searchHelper(current->l, key);
    } else {
      return searchHelper(current->r, key);
    }
  }

public:
  tree() : root(nullptr) {}

  int height (node *n) {
    return n? n->height : 0;
  }

  int balanceFactor (node *n) {
    return n? height(n->l) - height(n->r) : 0;
  }

  node *search(int key) { return searchHelper(root, key); }
};
