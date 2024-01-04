#include "lists.h"
/**
 * check_cycle - checks if singly linked list has cycle in it
 * @list: list to be checked
 *
 * Return: 0 if there is no cycle
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *does, *doesnt;

	if (!list || !list->next)
		return (0);
	does = list;
	doesnt = list;
	while (doesnt != NULL && does != NULL && does->next != NULL)
	{
		doesnt = doesnt->next;
		does = does->next->next;
		if (doesnt == does)
		{
			return (1);
		}
	}
	return (0);
}
