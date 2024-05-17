#include <iostream>

struct node
{
  int val;
  struct node* next;

  node(int val)
  {
    val = val;  
    next = nullptr;
  }
};

struct queue
{
  int size = 0;
  node *front;

  queue()
  {
    front = nullptr;
  }

  bool isEmpty()
  {
    return size>0? false : true;
  }

  void enqueue(int val)
  {
    if (!front)
    {
      front->val = val;
      front->next = nullptr;
      size = 1;
    }
  }
};
