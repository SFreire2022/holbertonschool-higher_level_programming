
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - Check elements of a listint_t list to detect palindrome list
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int *buff;
	ssize_t right = 0, left = 0;

	if (!*head || !((*head)->next))/* Check if just 0 or 1 element*/
		return (1);

	while (aux)/*traverse list to get the lenght*/
	{
		aux = aux->next;
		left++;
	}
	buff = malloc(sizeof(int) * left);/*malloc buffer to store elements*/
	left = 0;
	while (aux)/*traverse again to copy to buffer*/
	{
		buff[left] = aux->n;
		aux = aux->next;
		left++;
	}
	/*traverse again til the half list compairing to the mirror pos in buffer*/
	while (right <= (left - 1) / 2)
	{
		if (buff[right] != buff[left - right])
		{
			free(buff);
			return (0);
		}
		right++;
	}
	free(buff);
	return (1);
}
