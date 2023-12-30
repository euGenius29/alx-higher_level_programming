#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p)) {
		fprintf(stderr, "[*] Python list info\n [ERROR} Invalid List Object\n");
		return;
	}
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p)) {
        fprintf(stderr, "[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %ld bytes: ", (size > 10) ? 10 : size);
    for (Py_ssize_t i = 0; i < ((size > 10) ? 10 : size); ++i) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    double value = PyFloat_AsDouble(p);

    printf("[.] float object info\n");
    printf("  value: %f\n", value);
}

int main() {
    Py_Initialize();

    // Example usage:
    PyObject *list = PyList_New(3);
    PyList_SetItem(list, 0, PyBytes_FromString("Hello"));
    PyList_SetItem(list, 1, PyBytes_FromString("World"));
    PyList_SetItem(list, 2, PyLong_FromLong(42));

    print_python_list(list);

    PyObject *bytes = PyBytes_FromString("Python bytes");
    print_python_bytes(bytes);

    PyObject *py_float = PyFloat_FromDouble(3.14);
    print_python_float(py_float);

    // Cleanup
    Py_DECREF(list);
    Py_DECREF(bytes);
    Py_DECREF(py_float);

    Py_Finalize();

    return 0;
}
