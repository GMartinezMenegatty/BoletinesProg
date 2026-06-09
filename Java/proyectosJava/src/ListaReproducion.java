//import java.util.ArrayList;
//
//public class ListaReproducion extends Cancion{
//    private String nome;
//    private ArrayList<Cancion> cancions;
//    public int numMaxCancions;
//
//    public ListaReproducion (String nome, int numMaxCancions) {
//        this.nome = nome;
//        this.numMaxCancions = numMaxCancions;
//        ArrayList<Cancion> cancions = new ArrayList<>();
//    }
//
//    public String getNome () {
//        return nome;
//    }
//    public Cancion getCancion (String titulo) {
//        for (Cancion cancion : this.cancions) {
//            if (titulo.equals(cancion.getTitulo())) {
//                return cancion;
//            }
//        }
//        return null;
//    }
//    public boolean addCancion (Cancion c) {
//        if (this.cancions.size() < this.numMaxCancions) {
//            this.cancions.add(c);
//            return true;
//        }
//        return false;
//    }
//    ArrayList<Cancion> getCancionsArtista (String artista) {
//        ArrayList<Cancion> cancions = new ArrayList<>();
//        for (Cancion cancion : this.cancions) {
//            if (artista.equals(cancion.getArtista())) {
//                cancions.add(cancion);
//            }
//        }
//        return cancions;
//    }
//    public void reproducirCancion (Cancion c) {
//        if (c.equals(cancions)){
//            addNumReproducciones();
//        }
//    }
//    public void mostrarListaReproduccion () {
//        System.out.println(nome + " " + cancions);
//    }
//}
