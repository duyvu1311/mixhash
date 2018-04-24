#include <Python.h>

#include "lyra2REv2.h"

static PyObject *lyra2rev2_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    lyra2rev2_hash((char *)PyBytes_AsString((PyObject*) input), output);
#else
    lyra2rev2_hash((char *)PyString_AsString((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef lyra2REv2Methods[] = {
    { "getPoWHash", lyra2rev2_getpowhash, METH_VARARGS, "Returns the proof of work hash using Lyra2REv2 hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef lyra2REv2Module = {
    PyModuleDef_HEAD_INIT,
    "lyra2rev2_hash",
    "...",
    -1,
    lyra2REv2Methods
};

PyMODINIT_FUNC PyInit_lyra2rev2_hash(void) {
    return PyModule_Create(&lyra2REv2Module);
}

#else

PyMODINIT_FUNC initlyra2rev2_hash(void) {
    (void) Py_InitModule("lyra2rev2_hash", lyra2REv2Methods);
}
#endif
