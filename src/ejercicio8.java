public class ejercicio8 {
    public static void main(String[] args){
        System.out.println("Hola");
        Persona persona1 = new Persona();
        persona1.setEdad(18);
        persona1.setTelefono(600700800);
        persona1.setNombre("Juan");

        System.out.println("La persona creada se llama " + persona1.getNombre() + " y tiene " + persona1.getEdad());
        System.out.println("Su número de teléfono es " + persona1.getTelefono());

    };
};


class Persona8 {
    private int edad;
    private String nombre;
    private int telefono;

    public void setEdad(int edad){
        this.edad = edad;
    }
    public int getEdad(){
        return this.edad;
    }
    public void setTelefono(int telefono){
        this.telefono = telefono;
    }
    public int getTelefono(){
        return this.telefono;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public String getNombre(){
        return this.nombre;
    }
}