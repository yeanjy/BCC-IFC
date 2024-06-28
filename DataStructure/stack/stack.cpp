#include <iostream>

struct node
{
    int val;
    node *next;

    node(int val)
        : val(val), next(nullptr) {}
};

struct stack
{
    node *top;
    int size;

    stack()
        : top(nullptr), size(0) {}

    bool is_empty()
    {
        return size == 0;
    }

    void push(int n)
    {
        node *tmp = new node(n);
        if (!top)
            top = tmp;
        else
        {
            tmp->next = top;
            top = tmp;
        }
        size++;
    }

    int pop()
    {
        if (is_empty())
            throw std::out_of_range("Empty stack");

        node *aux = top;
        int result = aux->val;
        top = top->next;
        delete aux;
        return result;
    }

    void print()
    {
        if (is_empty())
            throw std::out_of_range("Empty stack");

        node *aux = top;
        while (aux)
        {
            std::cout << aux->val << " ";
            aux = aux->next;
        }
        std::cout << "\n";
    }
};

int main()
{
    stack a;
    a.push(7);
    a.push(9);
    a.push(0);
    a.push(3);
    a.push(10);
    a.pop();
    a.pop();
    a.pop();
    a.pop();
    a.pop();
    a.push(3);
    a.print();
    return 0;
}