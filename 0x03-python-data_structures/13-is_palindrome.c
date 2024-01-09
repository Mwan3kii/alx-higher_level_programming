#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
void reverse(listint_t **head);
int compare_lists(listint_t *head, listint_t *middle, int len);
/**
 * is_palindrome - checks singly linked list
 *
 * @head: start of node
 *
 * Return: 0 if palindrome isnt detected and if yes
 */
int is_palindrome(listint_t **head)
{
	int len, j;
	listint_t *temp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	middle = *head;

	for (len = 0; temp != NULL; len++)
		temp = temp->next;
	len = len / 2;

	for (j = 1; j < len; j++)
		middle = middle->next;
	if (len % 2 != 0 && len != 1)
	{
		middle = middle->next;
		len = len -1;
	}
	reverse(&middle);
	j = compare_lists(*head, middle, len);
	return (j);
}
/**
 * compare_lists - compare two lists
 * @head: pointer to head node
 * @middle: pointer to middle node
 * @len: length of list
 *
 * Return: if the same 1, if not 0
 */
int compare_lists(listint_t *head, listint_t *middle, int len)
{
	int k;

	if (head == NULL || middle == NULL)
		return (1);
	for (k = 0; k < len; k++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);
}
/**
 * reverse - reverses a list
 * @head: pointer to the head to reverse
 */
void reverse(listint_t **head)
{
	listint_t *curr;
	listint_t *next;
	listint_t *prev;

	if (head == NULL || *head == NULL)
		return;
	prev = NULL;
	curr = *head;
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;
}
