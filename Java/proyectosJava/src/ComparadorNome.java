import java.util.Comparator;

public class ComparadorNome implements Comparator<Persoa2> {
    public int compare(Persoa2 p1, Persoa2 p2) {
        return p1.nome.compareTo(p2.nome);
    }
}
