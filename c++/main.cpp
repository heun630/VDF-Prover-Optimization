//#include <stdio.h>
//#include <time.h>
//
//int main() {
//    unsigned long long x = 2;
//    unsigned long long modulus = 13;
//    clock_t start = clock();
//    for (int i = 0; i < 1000000000; i++) {
//        x = (x * x) % modulus;
//    }
//    clock_t end = clock();
//    double elapsed_time = (double)(end - start) / CLOCKS_PER_SEC;
//    printf("Elapsed time: %f seconds\n", elapsed_time);
//    return 0;
//}

#include <stdio.h>
#include <gmp.h>
#include <time.h>

int main() {
    mpz_t x, modulus;
    mpz_init_set_ui(x, 2);       // x를 2로 초기화
    mpz_init_set_ui(modulus, 13); // modulus를 13으로 초기화

    clock_t start = clock();
    for (int i = 0; i < 1000000000; i++) {
        mpz_mul(x, x, x);           // x = x * x
        mpz_mod(x, x, modulus);     // x = x % modulus
    }
    clock_t end = clock();

    double elapsed_time = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Elapsed time: %f seconds\n", elapsed_time);

    mpz_clear(x);
    mpz_clear(modulus);
    return 0;
}
