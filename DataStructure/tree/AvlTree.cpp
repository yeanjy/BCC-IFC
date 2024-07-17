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

public:
    AvlTree()
    :root(nullptr) {}

};

int main() {

    return 0;
}