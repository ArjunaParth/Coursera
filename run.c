#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int square(int x)
{
    return x * x;
}

int main(void)
{
    printf("=== C Compiler Test ===\n\n");

    // Variables
    int a = 5;
    printf("Variables: OK (%d)\n", a);

    // Loop
    printf("Loop: ");
    for (int i = 1; i <= 5; i++)
    {
        printf("%d ", i);
    }
    printf("\n");

    // Function
    printf("Function: square(5) = %d\n", square(5));

    // Math library
    printf("Math Library: sqrt(144) = %.2f\n", sqrt(144));

    // Memory allocation
    int *ptr = malloc(10 * sizeof(int));

    if (ptr == NULL)
    {
        printf("Memory Allocation: FAILED\n");
        return 1;
    }

    printf("Memory Allocation: OK\n");
    free(ptr);

    // File handling
    FILE *file = fopen("compiler_test.txt", "w");

    if (file == NULL)
    {
        printf("File Handling: FAILED\n");
        return 1;
    }

    fprintf(file, "Compiler test successful!\n");
    fclose(file);

    printf("File Handling: OK\n");

    printf("\n=== ALL TESTS PASSED ===\n");

    return 0;
}