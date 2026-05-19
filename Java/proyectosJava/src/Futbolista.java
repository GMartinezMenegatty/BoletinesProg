import java.util.Arrays;

public class Futbolista extends Persoa2{
    private int numGoles;

    public Futbolista(String nome, String dni, int edade, int numeroDeGoles){
        super(nome, dni, edade);
        this.numGoles = numeroDeGoles;

    }

    public int getNumDeGoles() {
        return numGoles;
    }

    public static void main(String [] args) {
        Futbolista equipo [] = new Futbolista [5];
        equipo [0] = new Futbolista("CR9", "1345J", 39, 3);
        equipo [1] = new Futbolista("Messi", "1355J", 35, 30);
        equipo [2] = new Futbolista("Pepe", "1365J", 37, 7);
        equipo [3] = new Futbolista("Duran", "1375J", 38, 22);
        equipo [4] = new Futbolista("Guerrero", "1385J", 36, 9);
        ComparadorGoles cg = new ComparadorGoles();
        Arrays.sort(equipo, cg);
        System.out.println(Arrays.toString(equipo));
        ComparadorGoles cn = new ComparadorGoles();
        Arrays.sort(equipo, cn);
        System.out.println(Arrays.toString(equipo));
    }
}
