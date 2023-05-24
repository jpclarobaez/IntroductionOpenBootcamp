/*
En este ejercicio practicarás las estructuras de control, para ello deberás crear:

- Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
    Pista: Los números inferiores a 0 son negativos y los superiores, positivos.
- Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3,
    el bloque de código que tendrá el bucle deberá:
- Incrementar el valor de la variable en uno cada vez que se ejecute.
- Mostrarlo por pantalla cada vez que se ejecute.

Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.
Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable
    sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.

Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año.
Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la
que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.

*/


import javax.swing.plaf.synth.SynthTextAreaUI;

public class Ejercicio4 {

    public String compareWithIf(int numeroIf){
        String result;
        if (numeroIf > 0) {
            result = "positivo";
        }
        else if (numeroIf == 0) {
            result = "0";
        }
        else {
            result = "negativo";
        }
        return result;
    }

    public void loopWhile(int limit){
        int i = 0;
        while (i < limit){
            i++;
            System.out.println(i);
        }
    }

    public void loopDoWhile(int limit){
        int i = 0;
        do {
            System.out.println(i);
            i++;
        }
        while (i < limit);
    }


    public void loopFor (int limit){
        for (int numeroFor = 0; numeroFor < limit; numeroFor++){
            System.out.println(numeroFor);
        }
    }


    public void switchEstaciones(String estacion){
        switch (estacion){
            case "Invierno":
                System.out.println("\tEstamos en Invierno");
                break;
            case "Primavera":
                System.out.println("\tEstamos en Primavera");
                break;
            case "Verano":
                System.out.println("\tEstamos en Verano");
                break;
            case "Otoño":
                System.out.println("\tEstamos en Otoño");
                break;
            default:
                System.out.println("\tParece que " + estacion + " no es una estación");
        }

    }


    public static void main(String[] args){
        int num = 6;
        String resultIf = "";
        Ejercicio4 ejerObj = new Ejercicio4();

        // If Example
        resultIf = ejerObj.compareWithIf(num);
        System.out.println("\tExample of IF");
        System.out.println("El número " + num + " es " + resultIf);

        // While Example
        System.out.println("\n\tExample of WHILE");
        ejerObj.loopWhile(3);

        // Do While Example
        System.out.println("\n\tExample of DO WHILE");
        ejerObj.loopDoWhile(1);

        // For loop Example
        System.out.println("\n\tExample of FOR");
        ejerObj.loopFor(3);

        // Switch Example
        System.out.println("\n\tExample of Switch");
        System.out.println("Para input Invierno:");
        ejerObj.switchEstaciones("Invierno");
        System.out.println("Para input Verano:");
        ejerObj.switchEstaciones("Verano");
        System.out.println("Para input Erróneo (test):");
        ejerObj.switchEstaciones("test");

    }
}
