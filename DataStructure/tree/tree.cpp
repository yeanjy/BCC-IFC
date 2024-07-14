#include <iostream>

struct tree {
private:
  struct node {
    node *l;
    node *r;
    int val;

    node(int val) : val(val), l(nullptr), r(nullptr) {}
  };

  node *root;

  void insertHelper(node *current, int val) {
    if (current->val < val) {
      if (!current->l) {
        current->l = new node(val);
      } else {
        insertHelper(current->l, val);
      }
    } else {
      if (!current->r) {
        current->r = new node(val);
      } else {
        insertHelper(current->r, val);
      }
    }
  }

  node *searchHelper(node *current, int val) {
    if (!current || current->val == val)
      return current;

    if (current->val < val) {
      return searchHelper(current->l, val);
    } else {
      return searchHelper(current->r, val);
    }
  }

public:
  tree() : root(nullptr) {}

  void insertion(int val) {
    if (!root) {
      root = new node(val);
    } else {
      insertHelper(root, val);
    }
  }

  node *search(int val) { return searchHelper(root, val); }
};
