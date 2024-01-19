# 0x02 Heap Insert :neckbeard:

> Technical interview challenges

## Tasks :heavy_check_mark:

Write a function that creates a binary tree node:

- Prototype: ```binary_tree_t *binary_tree_node(binary_tree_t *parent, int value);```

parent is a pointer to the parent node of the node to create
value is the value to put in the new node
When created, a node does not have any children
Your function must return a pointer to the new node, or NULL on failure

## Results :chart_with_upwards_trend:

| Filename |
| ------ |
| [0-binary_tree_node.c](https://github.com/Air-KS/holbertonschool-interview/blob/main/heap_insert/0-binary_tree_node.c)|
| [1-heap_insert.c](https://github.com/Air-KS/holbertonschool-interview/blob/main/heap_insert/1-heap_insert.c)|


## Additional info :construction:
### Resources

- C

### Try It On Your Machine :computer:
```bash
gcc -Wall -Wextra -Werror -pedantic binary_tree_print.c 0-main.c 0-binary_tree_node.c -o 0-node
./0-node

gcc -Wall -Wextra -Werror -pedantic binary_tree_print.c 1-main.c 1-heap_insert.c 0-binary_tree_node.c -o 1-heap_insert
./1-heap_insert
```
