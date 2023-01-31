// 1281 - Dado um número inteiro n, retorne a diferença entre o produto de seus dígitos e a soma de seus dígitos.

// link do submit: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/888773883/

/**
 * @param {number} n
 * @return {number}
 */
 function subtractProductAndSum(number) {
    const number_string = number.toString().split("");

    let soma = 0;
    let produto = 1;

    for (let i = 0; i < number_string.length; i++) {
        const number = parseInt(number_string[i]);
        
        soma += number;
        produto *= number;
    }


    return produto - soma;
}

// teste 
console.log(subtractProductAndSum(234))