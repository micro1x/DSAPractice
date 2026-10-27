#include <iostream>

struct Node
{
    int data;
    Node* next;

    Node(int value)
        : data{ value }, next{ nullptr }
    {
    }
};


class LinkedList
{
    public:
        void printList(Node* head);
        Node* deleteNode(Node* head, int pos);
        void deleteList(Node*& head);
};


void LinkedList::printList(Node* head)
{
    Node* current = head;

    while (current != nullptr)
    {
        std::cout << current->data << " -> ";
        current = current->next;
    }

    std::cout << "nullptr\n";
}


Node* LinkedList::deleteNode(Node* head, int pos)
{
    if (head == nullptr || pos < 1)
    {
        return head;
    }

    Node* temp = head;

    // Delete head
    if (pos == 1)
    {
        head = head->next;
        delete temp;

        return head;
    }

    Node* prev = nullptr;

    // Traverse to position
    for (int i = 1; i < pos; i++)
    {
        if (temp == nullptr)
        {
            return head;
        }

        prev = temp;
        temp = temp->next;
    }

    // Position does not exist
    if (temp == nullptr)
    {
        return head;
    }

    // Skip over the node being deleted
    prev->next = temp->next;

    delete temp;

    return head;
}


void LinkedList::deleteList(Node*& head)
{
    while (head != nullptr)
    {
        Node* temp = head;
        head = head->next;

        delete temp;
    }
}


int main()
{
    LinkedList lst;

    Node* head = new Node(10);

    head->next = new Node(20);
    head->next->next = new Node(30);
    head->next->next->next = new Node(40);
    head->next->next->next->next = new Node(50);

    lst.printList(head);

    // Delete node at POSITION 2 (the node containing 20)
    head = lst.deleteNode(head, 2);

    lst.printList(head);

    // Delete every remaining node
    lst.deleteList(head);

    // Safe because deleteList changed main's head to nullptr
    lst.printList(head);

    return 0;
}