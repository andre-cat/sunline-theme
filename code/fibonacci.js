/** Fibonacci generator */
const MAX_LIMIT = 10000;

function fibonacci(n, cache = new Map()) {
    if (n <= 1) return n;
    if (cache.has(n)) return cache.get(n);
    const result = fibonacci(n - 1, cache) + fibonacci(n - 2, cache);
    cache.set(n, result);
    return result;
}

class FibonacciGenerator {
    constructor(limit = MAX_LIMIT) {
        this.limit = limit;
    }
    
    async generate(count = 10) {
        return Array.from({ length: count }, (_, i) => fibonacci(i));
    }
}

const gen = new FibonacciGenerator(1000);
gen.generate(10).then(seq => console.log(`Result: ${seq}`));
