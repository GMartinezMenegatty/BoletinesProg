public class Traballador2 extends Persoa {
    public double salario;
    public String estatura;

    public Traballador2 (String nome, String dni, int edade, double estatura, double salario, String estaturaT) {
        super(nome, dni, edade, estatura);
        this.salario = salario;
        this.estatura = estaturaT;
    }

    public void mostrarDatos (){
        super.mostrarDatos();
        System.out.println("Salario: " + salario + "\nEstatura: " + estatura);
    }

    @Override
    public boolean equals (Object outro) {
        Traballador2 outroTraballador = (Traballador2) outro;
        if (this.estatura.equals(outroTraballador.estatura)) return true;
        return false;
    }

    public static void main (String []args) {
        Traballador2 t = new Traballador2 ("Pepe", "1111H", 37, 1.81, 1490, "XL");
        Persoa p = new Persoa ("Pepe", "1111H", 37, 1.81);
        Persoa persoas [] = new Persoa [2];
        persoas[0] = p;
        persoas[1] = t;
        Persoa unTraballador = t;
        Traballador2 outroT = new Traballador2 ("Juan", "2222J", 46, 1.73, 1780, "M");
        System.out.println("Executando exemplo Traballador");
        System.out.println(persoas[1].estatura);
        System.out.println(unTraballador.estatura);
        System.out.println(t.estatura);
        unTraballador.mostrarDatos();
        t.mostrarDatos();
        if (outroT == unTraballador) System.out.println("Son iguales");
        else System.out.println("No son iguales");
    }
}
