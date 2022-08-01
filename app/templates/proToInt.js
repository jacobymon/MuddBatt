// def numToBaseB(N, B):
// """takes a non negative interger 'N' (in base 10) and a base 'B' and returns
// that number in base B"""
// if N == 0:
//     return ''
// else:
//     return   numToBaseB(N//B, B) + str(N%B)
    function numToBaseB(N, B) {
        if(N==0) {
            return ''
        }
        else{
            return numToBaseB(Math.floor(N/B), B) + String(N%B)
        }
    }



    function numToBin(N) {
        if (N==0){
            return ''
        }
        let a = numToBaseB(Math.floor(N/2), 2) + String(N%2)
        while (a.length != 8) {
            if (a.length > 8) {
                return "Error, the length of the base 10 int in binary is longer than 8."
            }
            let b = String(0) + a
            a = b
        }
        return a
    }
    function myFunction() {
        let y = document.getElementById("a").innerHTML
        //y.parseInt()
        //let x = document.getElementById("a").value
        var array=[]
        for (let i = 0; i < y.length; i++) {
            let b = y[i].charCodeAt(0)
            array.push(b)
        }
        var array1=[]
        for (let x = 0; x < array.length; x++) {
            let c = numToBin(array[x])
            array1.push(c)
        }
        document.getElementById("test").innerHTML = array1.join('');
    }  