#include <Python.h>

/*
 * print_python_list_info - Print dkchii li lheeh
 * @p: object
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *ob;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		ob = PyList_Getltem(p, i);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
}
