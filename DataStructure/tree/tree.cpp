#include <iostream>

struct node {
  int key;
  node *left;
  node *right;

  node(int val) : key(val), left(nullptr), right(nullptr) {}

  node(int val, node *left, node *right) : key(val), left(left), right(right) {}
};

struct tree {
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

  node *insertHelperLoop(node *n, int val) {
    if (!n)
      return new node(val);

    node *current = n;
    node *parent;

    while (current) {
      parent = current;
      if (val < current->key)
        current = current->left;
      else if (val > current->key)
        current = current->right;
      else
        return n;
    }

    if (val < parent->key)
      parent->left = new node(val);
    else
      parent->right = new node(val);

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

  node *search(node *n, int val) {
    node *aux = n;
    while (aux) {
      if (aux->key == val)
        return aux;
      if (val > aux->key) {
        aux = aux->right;
      } else
        aux = aux->left;
    }
    return aux;
  }

  void printInOrderHelper(node *n) {
    if (n) {
      printInOrderHelper(n->left);
      std::cout << n->key << std::endl;
      printInOrderHelper(n->right);
    }
  }

  tree() : root(nullptr) {};

  void insertRec(int val) { root = insertHelper(root, val); }
  void insert(int val) { root = insertHelperLoop(root, val); }
  void printInOrder() { printInOrderHelper(root); }

  void remove(int key) {
    if (!root)
      return;

    node *cur = root, *pre = nullptr;

    while (cur) {
      if (cur->key == key)
        break;
      
      pre = cur;

      if (cur->key < key)
        cur = cur->right;
      else 
        cur = cur->left;
    }

    if (!cur)
      return;

    if (cur->left == nullptr || cur->right == nullptr) {
      node *child = cur->left != nullptr ? cur->left : cur->right;

      if (cur != root)
        if (pre->left == cur)
          pre->left = child;
        else 
          pre->right = child;
      else 
        root = child;

      delete cur;
    }
    else {
      node *tmp = cur->right;
      
      while (tmp->left) 
        tmp = tmp->left;

      int tmpVal = tmp->key;
      remove(tmp->key);
      cur->key = tmpVal;
    }
  }
};

void printNode(node *n) {
  if (n)
    std::cout << "node founded " << n->key << std::endl;
  else
    std::cout << "Node not found" << std::endl;
}

int main() {
  tree t;

  t.insertRec(5);
  t.insertRec(3);
  t.insertRec(7);
  t.insertRec(2);
  t.insertRec(4);
  t.insertRec(6);
  t.insertRec(8);
  t.insert(19);
  t.insert(29);
  t.insert(41);
  t.insert(39);
  t.remove(41);
  t.remove(19);
  t.printInOrder();
  node *n = t.searchRec(t.root, 39);
  printNode(n);

  return 0;
}
