public class Persoa {
    //declaracion de propiedades
    public String nome;
    public String dni;
    public int edade;
    public double estatura;

    public Persoa() {
        nome = "";
        dni = "0000000T";
        edade = 0;
        estatura = 0;
    }
    public Persoa (String nome, String dni, int edade, double estatura){
        this.nome = nome;
        this.dni = dni;
        this.edade = edade;
        this.estatura = estatura;
    }

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public void mostrarDatos () {
        System.out.println("Nome: " + nome + "\nDni: " + dni + "\nEdade: " + edade + "\nEstatura: " + estatura);
    }

    @Override
    public boolean equals (Object outro) {
        Persoa outraPersoa = (Persoa) outro;
        if (this.estatura == outraPersoa.estatura) return true;
        return false;
    }

    public static void main(String [] args) {
        Persoa p1 = new Persoa();
        Persoa p2 = new Persoa("Manuel", "44556U", 45, 1.70);
        System.out.println(p1.nome);
        System.out.println(p2.nome + " " + p2.dni + " " + p2.edade);
    }
}


