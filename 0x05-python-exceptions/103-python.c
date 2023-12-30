#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    PyObject *size = PyObject_CallMethod(p, "__len__", NULL);
    PyObject *allocated = PyObject_GetAttrString(p, "allocated");

    if (size == NULL || allocated == NULL) {
        PyErr_Print();
        Py_XDECREF(size);
        Py_XDECREF(allocated);
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyLong_AsLong(size));
    printf("[*] Allocated = %ld\n", PyLong_AsLong(allocated));

    Py_XDECREF(size);
    Py_XDECREF(allocated);

    for (Py_ssize_t i = 0; i < PyList_Size(p); ++i) {
        PyObject *item = PyObject_GetItem(p, PyLong_FromSsize_t(i));
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        Py_XDECREF(item);
    }
}

void print_python_bytes(PyObject *p) {
    PyObject *size = PyObject_CallMethod(p, "__len__", NULL);
    PyObject *str_obj = PyObject_Str(p);

    if (size == NULL || str_obj == NULL) {
        PyErr_Print();
        Py_XDECREF(size);
        Py_XDECREF(str_obj);
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyLong_AsLong(size));
    printf("  trying string: %s\n", PyUnicode_AsUTF8(str_obj));

    printf("  first %ld bytes: ", (PyLong_AsLong(size) > 10) ? 10 : PyLong_AsLong(size));

    for (Py_ssize_t i = 0; i < ((PyLong_AsLong(size) > 10) ? 10 : PyLong_AsLong(size)); ++i) {
        printf("%02x ", (unsigned char)PyUnicode_AsUTF8(str_obj)[i]);
    }

    printf("\n");

    Py_XDECREF(size);
    Py_XDECREF(str_obj);
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
    PyObject *bytes = PyBytes_FromString("Python bytes");
    PyObject *py_float = PyFloat_FromDouble(3.14);

    PyList_SetItem(list, 0, PyBytes_FromString("Hello"));
    PyList_SetItem(list, 1, PyBytes_FromString("World"));
    PyList_SetItem(list, 2, PyLong_FromLong(42));

    print_python_list(list);
    print_python_bytes(bytes);
    print_python_float(py_float);

    // Cleanup
    Py_DECREF(list);
    Py_DECREF(bytes);
    Py_DECREF(py_float);

    Py_Finalize();

    return 0;
}
