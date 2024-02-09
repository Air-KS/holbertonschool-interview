#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;
	listint_t *stack = NULL, *temp;
	int isPalin = 1;

	/* une liste vide est considérée comme un palindrome */
	if (!head || !*head || !(*head)->next)
	{
		return (1);
	}

	/* Utiliser deux pointeurs pour trouver le milieur de la liste */
	while (fast && fast->next)
	{
		fast = fast->next->next;

		/* Empiler la première moitié des éléments */
		temp = slow;
		slow = slow->next;
		temp->next = stack;
		stack = temp;
	}

	/* Si la liste a un nombre impaire d'éléments, sauter l'éléments du milieu */
	if (fast)
	{
		slow = slow->next;
	}

	/* Compare les élément de la pile avec la seconde moitié de la list */
	while (slow)
	{
		if (stack->n != slow->n)
		{
			isPalin = 0;
			break;
		}
		slow = slow->next;
		temp = stack;
		stack = stack->next;
	}

	/* Libérer la pile si necessaire */
	while (stack)
	{
		temp = stack->next;
		free(stack);
		stack = temp;
	}

	return (isPalin);
}
