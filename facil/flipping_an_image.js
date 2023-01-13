// exercicio 832.
// Dada uma n x nmatriz binária image, inverta a imagem horizontalmente , depois inverta-a e retorne a imagem resultante .
// Virar uma imagem horizontalmente significa que cada linha da imagem é invertida.
// Por exemplo, virar [1,1,0]horizontalmente resulta em [0,1,1].
// Inverter uma imagem significa que cada um 0é substituído por 1, e cada um 1é substituído por 0.
// Por exemplo, inverter [0,1,1]resulta em [1,0,0].

/**
 * @param {number[][]} image
 * @return {number[][]}
 */
 var flipAndInvertImage = function(image) {
    // for ([inicialização]; [condição]; [expressão final])
    for (let i = 0; i < image.length; i++) {
        image[i].reverse()
        for (let j = 0; j < image[i].length; j++) {
            image[i][j] = image[i][j] == 0 ? 1 : 0
        }
    }
    return image;
};

console.log(flipAndInvertImage([1010]))
