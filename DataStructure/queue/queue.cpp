#include <iostream>
#include <stdexcept>

struct node
{
  int val;
  struct node* next;

  node(int val)
  : val(val), next(nullptr) {}
};

struct queue
{
  int size = 0;
  node *front;
  node *back;

  queue()
  :size(0), front(nullptr), back(nullptr)
  {}

  bool isEmpty()
  {
    return size == 0;
  }

  void enqueue(int val)
  {
    node *aux = new node(val);
    if (!front)
    {
      front = aux;
      back = aux;
    }
    else 
    {
      back->next = aux;
      back = back->next;
    }
    size++;
  }

  int dequeue()
  {
    if(isEmpty())
      throw std::out_of_range("Queue is empty");

    node *temp = front;
    int val = front->val;
    front = front->next;
    delete temp;
    size--;

    if(!front)
    {
      back = nullptr;
    }

    return val;
  }

  void printQueue()
  {
    node *tmp = front;
    while (tmp != nullptr)
    {
      std::cout << tmp->val << "\n";
      tmp = tmp->next;
    }
  }
};

int main()
{
  queue bla;
  bla.enqueue(4);
  bla.enqueue(6);
  bla.enqueue(2);
  bla.enqueue(1);
  bla.enqueue(10);
  bla.dequeue();
  bla.printQueue();
  return 0;
}
