#include <iostream>

struct node {
    int key;
    node *left;
    node *right;
    int height;

    node(int key)
    :key(key), left(nullptr), right(nullptr), height(0) {}
};

class AvlTree {
private: 
    node *root;

    int max(int a, int b) {
        return a > b? a:b;
    }

    int height(node *n){
        return n ? n->height : -1;
    }

    int balanceFactor(node *n) {
        return n ? height(n->left) - height(n->right) : 0;
    }

    void updateHeight(node *n) {
        n->height = max(height(n->left), height(n->right)) + 1;
    }

    node *rightRotate(node *n) {
        node *child = n->left;
        node *grandChild = child->right;

        child->right = n;
        n->left = grandChild;

        updateHeight(n);
        updateHeight(child);

        return child;
    }

    node *leftRotate(node *n) {
        node *child = n->right;
        node *grandChild = child->left;

        child->left = n;
        n->right = grandChild;

        updateHeight(n);
        updateHeight(child);

        return child;
    }

    node *rotate(node *n) {
        int _balanceFactor = balanceFactor(n);

        if(_balanceFactor > 1) {
            if (balanceFactor(n->left) >= 0) {
                return rightRotate(n);
            }
            else {
                n->left = leftRotate(n->left);
                return rightRotate(n);
            }
        }

        if (_balanceFactor < -1) {
            if(balanceFactor(n->right) <= 0) {
                return leftRotate(n);
            }
            else {
                n->right = rightRotate(n->right);
                return leftRotate(n);
            }
        }
        return n;
    }

    node *insertHelper(node *n, int val) {
        if (!n)
            return new node(val);

        if (val < n->key)
            n->left = insertHelper(n->left, val);
        else if (val > n->key)
            n->right = insertHelper(n->right, val);
        else 
            return n;

        updateHeight(n);
        n = rotate(n);

        return n;
    }

public:
    AvlTree()
    :root(nullptr) {}

    void insert(int val) {
        root = insertHelper(root, val);
    }

};

int main() {
    AvlTree t;
    t.insert(4);
    t.insert(1);
    t.insert(3);
    t.insert(443);
    t.insert(12312);
    t.insert(95342);
    t.insert(312);
    return 0;
}