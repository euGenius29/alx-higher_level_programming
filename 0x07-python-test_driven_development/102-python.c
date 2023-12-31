#include <Python.h>

/**
 * print_python_string - Prints info on python strings.
 * @p: The python string object
 * Return: void
 */
void print_python_string(PyObject *p)
{
	ssize_t size;
	printf("[.] string object info\n");

	if (strcmp((p->ob_type)->tp_name, "str") != 0)
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");

	size = ((PyASCIIObject *)p)->length;
	printf(" lenght: %ld\n", size);
	printf(" value: %ls\n", PyUnicode_AsWideCharString(p, &size));
}
