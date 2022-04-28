#include "lists.h"

/**
 * check_cycle - Check if loop on linkedlists
 * Using Floyd’s Cycle detection algorithm
 * @list: Linkedlist head *
 * Return: 1 if cycle found or 0 if not cycle found
 */
int check_cycle(listint_t *list)
{
	/* Aux nodes declaration and initialization */
	listint_t *slow_p = list, *fast_p = list;

	/* Traverse list with two aux pointers at diferent speeds */
	while (slow_p && fast_p && fast_p->next)/* While list not end */
	{
		slow_p = slow_p->next;/* Traverse node by node */
		fast_p = fast_p->next->next;/* Traverse in steps of two */
		if (slow_p == fast_p)/* If both points to same node */
			return (1);/* Infinite loop detected */
	}
	return (0);/* Otherwise end of list reached without loop */
}
