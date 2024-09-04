package main

import (
	"fmt"
	"math/big"
	"time"
)

func main() {
	x := big.NewInt(2)
	modulus := big.NewInt(13)

	start := time.Now()
	for i := 0; i < 1000000000; i++ {
		x.Mul(x, x)
	    x.Mod(x, modulus)
	}
	elapsed := time.Since(start)
	fmt.Printf("Elapsed time: %f seconds\n", elapsed.Seconds())
}

// package main
//
// import (
// 	"fmt"
// 	"math/big"
// 	"sync"
// 	"time"
// )
//
// func main() {
// 	var wg sync.WaitGroup
// 	numRoutines := 10  // 사용할 고루틴의 수
// 	iterPerRoutine := 100000000  // 각 고루틴에서 처리할 반복 횟수
//
// 	start := time.Now()
// 	for i := 0; i < numRoutines; i++ {
// 		wg.Add(1)
// 		go func() {
// 			x := big.NewInt(2)
// 			modulus := big.NewInt(13)
// 			for j := 0; j < iterPerRoutine; j++ {
// 				x.Mul(x, x)
// 				x.Mod(x, modulus)
// 			}
// 			wg.Done()
// 		}()
// 	}
// 	wg.Wait()
// 	elapsed := time.Since(start)
// 	fmt.Printf("Elapsed time using goroutines: %f seconds\n", elapsed.Seconds())
// }

