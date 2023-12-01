#include "hash_tables.h"

/**
 * hash_table_create - creates a hash table with a given size
 *
 * @size: size of the hash table
 * Return: the created hash table, or NULL if function fails
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *hash_table;
	hash_node_t **hash_array;
	unsigned long int z;

	hash_table = malloc(sizeof(hash_table_t));
	if (hash_table == NULL)
		return (NULL);

	hash_array = malloc(sizeof(hash_node_t *) * size);
	if (hash_array == NULL)
		return (NULL);

	for (z = 0; z < size; z++)
		hash_array[z] = NULL;

	hash_table->array = hash_array;
	hash_table->size = size;

	return (hash_table);
