/*
Crea una clase Persona con las siguientes variables:

La edad
El nombre
El teléfono

Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable
    credito solo para esa clase.
Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito,
    tienes que darles valor y mostrarlas por pantalla.
Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo
tenga la clase Trabajador.
*/

public class ejercicio9 {
    public static void main(String[] args){
        Cliente cliente1 = new Cliente();
        cliente1.setEdad(18);
        cliente1.setTelefono(600700800);
        cliente1.setNombre("Pedro");
        cliente1.setCredito(125.36);
        System.out.println(cliente1.giveInfo());


        Trabajador trabajador1 = new Trabajador();
        trabajador1.setEdad(33);
        trabajador1.setTelefono(666999333);
        trabajador1.setNombre("José Miguel");
        trabajador1.setSalario(45000);
        System.out.println(trabajador1.giveInfo());
    }
}


class Persona {
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

    public String giveInfo(){
        String info;
        info = "\nHola, me llamo " + this.getNombre() + " y tengo " + this.getEdad() + " años.";
        info += "\nMi número de teléfono es " + this.getTelefono();
        return info;
    }
}

class Cliente extends Persona{
    private double credito;

    public void setCredito(double credito){
        this.credito = credito;
    }
    public double getCredito(){
        return this.credito;
    }
    public String giveInfo(){
        return super.giveInfo() + " y tengo " + this.getCredito() + " euros en el banco";
    }
}

class Trabajador extends Persona{
    private double salario;

    public void setSalario(double salario){
        this.salario = salario;
    }
    public double getSalario(){
        return this.salario;
    }
    public String giveInfo(){
        return super.giveInfo() + " y cobro " + this.getSalario() + " euros al año";
    }
}