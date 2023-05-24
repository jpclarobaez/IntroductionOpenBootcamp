/*Segunda parte:
        Crear una clase coche.
        Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
        Una función que incremente el número de puertas que tiene el coche.
        Crear un objeto miCoche en el main y añadirle una puerta.
        Mostrar el número de puertas que tiene el objeto.*/

public class Coche {
    public int puertas;

    public void addDoors(){
        puertas += 1;
    }
    public static void main(String[] args){
        Coche miCoche = new Coche();
        miCoche.addDoors();
        System.out.print("El objeto miCoche tiene " + miCoche.puertas + " puerta(s)");
    }
}
