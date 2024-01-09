#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int s_ize = PyList_Size(p);
	int j;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", s_ize);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (j = 0; j < s_ize; j++)
		printf("Element %i: %s\n", j, Py_TYPE(obj->ob_item[j])->tp_name);
}
