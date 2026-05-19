import java.util.Arrays;

public class Persoa implements Comparable<Persoa>{
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

    @Override
    public int compareTo(Persoa outro) {
//        int resultadoCom = this.dni.compareTo(outro.dni);
//        System.out.println(resultadoCom);
//        if (resultadoCom > 0) return 1;
//        else if (resultadoCom < 0) return -1;
//        return 0;
        return this.dni.compareTo(outro.dni);
    }

    public String toString(){
        return nome + ", " + dni + ", " + edade + ", " + estatura;
    }

    public static void main(String [] args) {
        Persoa p1 = new Persoa();
        Persoa p2 = new Persoa("Manuel", "4456U", 45, 1.70);
        Persoa p3 = new Persoa("Pepe", "4567H", 35, 1.64);
        System.out.println(p1.nome);
        System.out.println(p2.nome + " " + p2.dni + " " + p2.edade);
        System.out.println(p2.compareTo(p3));
        ComparadorEdadesPersoa compEdades = new ComparadorEdadesPersoa();
        System.out.println(compEdades.compare(p2, p3));
        Persoa [] individuos = new Persoa [3];
        individuos[0] = p2;
        individuos[1] = p1;
        individuos[2] = p3;
        System.out.println(Arrays.toString(individuos));
        Arrays.sort(individuos);
        System.out.println(Arrays.toString(individuos));
        Arrays.sort (individuos, compEdades);
        System.out.println(Arrays.toString(individuos));
    }


}


