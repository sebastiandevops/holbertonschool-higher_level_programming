#include "lists.h"
/**
 * insert_node - function that inserts a number
 * into a sorted singly linked list.
 * @head: list header.
 * @number: integer.
 *
 * Return: integer.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = malloc(sizeof(listint_t));

	newNode->n = number;
	newNode->next = NULL;
	if (*head == NULL)
		*head = newNode;
	else
	{
		listint_t *nodeA = *head;
		listint_t *nodeB = nodeA->next;

		while (nodeA->next != NULL)
		{
			if (nodeB->n > number)
			{
				nodeA->next = newNode;
				newNode->next = nodeB;
				break;
			}
			else
				nodeA = nodeB;
				nodeB = nodeB->next;
		}
		if (newNode->next == NULL)
			nodeA->next = newNode;
	}
	return (&(*newNode));
}
