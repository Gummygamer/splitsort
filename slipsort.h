// splitsort.h

#ifdef _WIN32
#define DLLEXPORT __declspec(dllexport)
#else
#define DLLEXPORT
#endif

// Function declaration
DLLEXPORT void splitSort(int arr[], int n);
