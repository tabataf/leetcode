// Dado um inteiro x, retorne true se x for um palíndromo, e false caso contrário .

// link do submit: https://leetcode.com/problems/palindrome-number/submissions/888772003/
/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    let teste = null
    let x_string = String(x)
    let x_separado = x_string.split("")
    let x_invertido = x_separado.reverse()
    let novo_x = x_invertido.join("")
    
    if(x_string === novo_x) {
        teste = true
        }
    else {
        teste = false
        }
    return teste
    }

// teste 
console.log(isPalindrome(65))
