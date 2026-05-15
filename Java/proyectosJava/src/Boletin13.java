import java.util.*;

public class Boletin13 {

    public static ArrayList<Integer> crearListaCenNumerosAleatorios(){
        //Parte do exercicio 2
        ArrayList<Integer> lista = new ArrayList<>();
        Random r = new Random();
        int n;
        for (int i=0; i<100; i++){
            n = r.nextInt(10)+1;
            lista.add(new Integer(n));
        }
        return lista;
    }

    public static void eliminaCincosSetesEnLista(ArrayList<Integer> l){
        /* No funciona
        for (Integer n: l){
            if (n==5 || n==7) l.remove(n);
        }
         */
        /* Si funciona
        for (int i=0; i<l.size(); i++){
            Integer n = l.get(i);
            if (n==5 || n==7) {
                l.remove(i);
                i--;
            }
        }
        */
        /* Si funciona
        Iterator<Integer> it = l.iterator();
        while (it.hasNext()){
            Integer n = it.next();
            if (n==5 || n==7) it.remove();
        }
         */
        /* No funciona
        ListIterator<Integer> lstIterator = l.listIterator();
        while (lstIterator.hasNext()){
            Integer n = lstIterator.next();
            if (n==5 || n==7)l.remove(n);
        }
         */
        l.removeIf( n -> n == 5 || n == 7);
    }

    public static void main(String[] args) {
        ArrayList<Integer> listaAleatoria = crearListaCenNumerosAleatorios();
        System.out.println(listaAleatoria);
        eliminaCincosSetesEnLista(listaAleatoria);
        System.out.println(listaAleatoria);
    }
}
