#include <stdio.h>

void main() {
    int array[] = {10, 12, 14, 16, 18};
    int len = sizeof(array) / 4;

    for (int i = 0; i < len; i++) {
        printf("Place %d is %d\n", i, array[i]);
    }
}
