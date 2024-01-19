# Insert in sorted linked list :neckbeard:

> Technical interview challenges

## Tasks :heavy_check_mark:

Write a function in C that inserts a number into a sorted singly linked list.

- Prototype: ```listint_t *insert_node(listint_t **head, int number);```
- Return: the address of the new node, or NULL if it failed

## Results :chart_with_upwards_trend:

| Filename |
| ------ |
| [0-insert_number.c](https://github.com/Air-KS/holbertonschool-interview/blob/main/insert_in_sorted_linked_list/0-insert_number.c)|

## Additional info :construction:
### Resources

- C

### Try It On Your Machine :computer:

<details>
<summary>0-main.c</summary>
<br>

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 0);
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 4);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 402);
    add_nodeint_end(&head, 1024);
    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, 27);

    print_listint(head);

    free_listint(head);

    return (0);
}

```
</details>

<details>

<summary>Test File</summary>
<br>

```bash
cd insert_in_sorted_linked_list
gcc -Wall -Werror -Wextra -pedantic 0-main.c linked_lists.c 0-insert_number.c -o insert
./insert
```
</details>

------------------------------

# Author
ROGERET Kevin<br>
> Project carried out within the framework of the school **[Holberton School](https://www.holbertonschool.com/).**<br>
