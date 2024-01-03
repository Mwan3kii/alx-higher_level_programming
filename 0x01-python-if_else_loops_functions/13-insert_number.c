#include <stdlib.h>
#include "lists.h"
#include <unistd.h>
/**
 * insert_node - insert a number into a sorted list
 * @head: begining of linked list
 * @number: no to be inserted
 *
 * Return: pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (curr && curr->n < number)
		{
			temp = curr;
			curr = curr->next;
		}
		temp->next = new;
		new->next = curr;
	}
	return (new);
}
