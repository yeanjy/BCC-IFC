#include <iostream>

struct node
{
    node *l;
    node *r;
    int val;

    node(int val) : val(val), l(nullptr), r(nullptr)
    {
    }
};

struct binaryTree
{
    node *root;

    binaryTree() : root(nullptr)
    {
    }

    void insertion(int val)
    {
        if (!root)
        {
            root = new node(val);
        }
        else
        {
        }
    }
};
