#include <iostream>

struct node {
  int key;
  node *left;
  node *right;

  node(int val) : key(val), left(nullptr), right(nullptr) {}

  node(int val, node *left, node *right) : key(val), left(left), right(right) {}
};

struct tree {
private:
  node *root;

  node *insertHelper(node *n, int val) {
    if (!n)
      return new node(val);

    if (val > n->key)
      n->right = insertHelper(n->right, val);
    else if (val < n->key)
      n->left = insertHelper(n->left, val);

    return n;
  }

  node *searchRec(node *n, int val) {
    if (!n)
      return nullptr;

    if (val == n->key)
      return n;

    if (val > n->key)
      return searchRec(n->right, val);
    else
      return searchRec(n->left, val);
  }

public:
  tree() : root(nullptr) {};

  void insertRec(int val) { root = insertHelper(root, val); }
};

int main() { return 0; }
