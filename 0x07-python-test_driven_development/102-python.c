#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints information about a Python string object.
 *
 * @p: Pointer to the Python string object.
 * Return: No return value.
 */
void print_python_string(PyObject *p)
{
	PyObject *str, *repr;

	(void)repr;
	printf("[.] String object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  Type: Compact ASCII\n");
	else
		printf("  Type: Compact Unicode object\n");

	repr = PyObject_Repr(p);
	str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  Length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  Value: %s\n", PyBytes_AsString(str));
}
