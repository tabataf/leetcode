// 2396 - Um inteiro né estritamente palindrômico se, para cada base bentre 2e n - 2( inclusive ), a representação de string do inteiro nem base bé palindrômica .

// Dado um número inteiro n, retorna true se n for estritamente palíndromo e false caso contrário .

// Uma string é palindrômica se lê a mesma para frente e para trás.

/**
 * @param {number} n
 * @return {boolean}
 */
 var isStrictlyPalindromic = function(n) {
    base = 2
    while(base<=n-2){
        palindromo= findBase(n,base)
        if(isPallindrome(palindromo)){
            num = true;
            base++;
        }else{
            return false;
        }
    }return num;
};

var findBase = function(n,base){
    return n.toString(base);
}
var isPallindrome = function(n){
    n_invertido = String(n).split('').reverse().join('');
    return n==n_invertido;
};

// teste 
n = 9
console.log(isStrictlyPalindromic(n))