#include <iostream>

class tree {
private:
  struct node {
    node *l;
    node *r;
    int key;
    int height;

    node(int key) : key(key), l(nullptr), r(nullptr), height(0) {}
  };

  node *root;

  int max (int a, int b) {
    return a > b? a:b;
  }

  node *rightRotate(node *n) {
    node *aux = n->l;
    node *aux2 = aux->r;

    aux->r = n;
    n->l = aux2;
    updateHeight(n);
    updateHeight(aux);
    return aux;
}

node *leftRotate (node *n) {
  node *aux = n->r;
  node *aux2 = aux->l;

  aux->l = n;
  n->r = aux2;
  updateHeight(n);
  updateHeight(aux);
  return aux;
}

int height (node *n) {
  return n? n->height : -1;
}

int balanceFactor (node *n) {
  return n? height(n->l) - height(n->r) : 0;
}

void updateHeight (node *n) {
  n->height = 1 + max(height(n->l), height(n->r));
}

node *balance(node *n) {
  updateHeight(n);

  int balance = balanceFactor(n);

  if (balance > 1) {
    if (balanceFactor(n->l) < 0) {
      n->l = leftRotate(n->l);
    }
    return rightRotate(n);
  }
  if (balance < -1) {
    if (balanceFactor(n->r) > 0) {
      n->r = rightRotate(n->r);
    }
    return leftRotate(n);
  }

  return n;
}

node *insert(node *n, int key) {
  if (!n)
    return new node (key);

  if (key < n->key)
    n->l = insert (n->l, key);
  else if (key > n->key)
    n->r = insert(n->r, key);
  else 
    return n;

  return balance(n);
}

public:
  tree() : root(nullptr) {}
  
  void insert (int key) {
    insert(root, key);
  }

};

int main() {
  tree t;
  t.insert(4);
  t.insert(1);
  t.insert(3);
  t.insert(443);
  t.insert(12312);
  t.insert(95342);
  t.insert(312);

  return 0;
}
