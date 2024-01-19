#include "binary_trees.h"

/**
 * binary_tree_size - function that return the size of a tree
 * @tree: tree to check
 * Return: size of tree
 */

size_t binary_tree_size(const binary_tree_t *tree)
{
	size_t size = 0, left = 0, right = 0;

	// Checks if the tree is empty.
	if (tree == NULL)
	{
		return (0);
	}
	else
	{
		left = binary_tree_size(tree->left);
		right = binary_tree_size(tree->right);
		size = left + right + 1;
	}

	return (size);
}

/**
 * insert_ordered - Inserts node level ordered
 * @tree: Type binary_tree pointer of the parent node
 * @value: Type int value of value inserted into node
 * @idx: Type int index of the node
 * @n_leaf: Type int node array position (parent formula: idx / 2)
 * Return: Node inserted
 */
heap_t *insert_ordered(binary_tree_t *tree, int value, int idx, int n_leaf)
{
	heap_t *node;

	// Checks if the tree is empty.
	if (tree == NULL)
	{
		return (NULL);
	}

	// Position for the new node and insert it as a left or right child.
	if (idx + 1 == n_leaf / 2)
	{
		if (n_leaf & 1)
		{
			tree->right = binary_tree_node(tree, value);
			return (tree->right);
		}
		else
		{
			tree->left = binary_tree_node(tree, value);
			return (tree->left);
		}
	}

	// Attempt to insert in the left subtree.
	node = insert_ordered(tree->left, value, 2 * idx + 1, n_leaf);

	// If insertion in the left subtree didn't happen, try the right subtree.
	if (node != 0)
	{
		return (node);
	}
	else
	{
		return (insert_ordered(tree->right, value, 2 * idx + 2, n_leaf));
	}
}

/**
 * heap_insert - Insert a node into a Max binary heap
 * @root: Type heap_t pointer of the parent node
 * @value: Type int of value inserted into node
 * Return: Node inserted
 */
heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *node;

	// If the heap is empty, create a new root node.
	if (*root == NULL)
	{
		*root = binary_tree_node(NULL, value);
		return (*root);
	}

	// Insert the new node in an ordered manner.
	node = insert_ordered(*root, value, 0, binary_tree_size(*root) + 1);

	// Rearrange the heap if necessary to maintain the max-heap property.
	while (node->parent && node->n > node->parent->n)
	{
		node->n = node->parent->n;
		node->parent->n = value;
		node = node->parent;
	}

	return (node);
}
