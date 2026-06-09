//public abstract class Persoa2 implements Comparable<Persoa2>{
//    //declaracion de propiedades
//    public String nome;
//    public String dni;
//    public int edade;
//
//    public Persoa2 (String nome, String dni, int edade){
//        this.nome = this.nome;
//        this.dni = this.dni;
//        this.edade = this.edade;
//    }
//
//    public String getNome() {
//        return this.nome;
//    }
//
//    public void setNome(String nome) {
//        this.nome = nome;
//    }
//    public void mostrarDatos () {
//        System.out.println("Nome: " + nome + "\nDni: " + dni + "\nEdade: " + edade);
//    }
//
//    @Override
//    public int compareTo(Persoa2 outro) {
////        int resultadoCom = this.dni.compareTo(outro.dni);
////        System.out.println(resultadoCom);
////        if (resultadoCom > 0) return 1;
////        else if (resultadoCom < 0) return -1;
////        return 0;
//        return this.dni.compareTo(outro.dni);
//    }
//
//    public abstract int compareTo(Socio o);
//
//    public String toString(){
//        return nome + ", " + dni + ", " + edade ;
//    }
//
////    public static void main(String [] args) {
////        Persoa2 p1 = new Persoa2();
////        Persoa2 p2 = new Persoa2("Manuel", "4456U", 45, 1.70);
////        Persoa2 p3 = new Persoa2("Pepe", "4567H", 35, 1.64);
////        System.out.println(p1.nome);
////        System.out.println(p2.nome + " " + p2.dni + " " + p2.edade);
////        System.out.println(p2.compareTo(p3));
////        ComparadorEdadesPersoa compEdades = new ComparadorEdadesPersoa();
////        System.out.println(compEdades.compare(p2, p3));
////        Persoa2 [] individuos = new Persoa2 [3];
////        individuos[0] = p2;
////        individuos[1] = p1;
////        individuos[2] = p3;
////        System.out.println(Arrays.toString(individuos));
////        Arrays.sort(individuos);
////        System.out.println(Arrays.toString(individuos));
////        Arrays.sort (individuos, compEdades);
////        System.out.println(Arrays.toString(individuos));
////    }
//
//
//}
//
//
//
